#!/usr/bin/env python3
"""
robust_fetch.py — 自包含的抗反爬网页获取工具
从 Web-Rooter (MIT License, github.com/pinkpixel-dev/web-rooter) 提取并简化。

零强制依赖（仅用 Python 标准库即可运行），可选增强：
  - curl_cffi: TLS 指纹伪装，绕过反爬
  - playwright: JS 渲染，获取动态内容

用法:
  python robust_fetch.py <URL> [--js] [--output markdown|html|text] [--timeout 30]

退出码:
  0: 成功
  1: 所有策略均失败
"""

import argparse
import json
import random
import re
import sys
import time
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# ---------------------------------------------------------------------------
# 配置常量（源自 Web-Rooter core/crawler.py）
# ---------------------------------------------------------------------------

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
]

ACCEPT_LANGUAGES = [
    "zh-CN,zh;q=0.9,en;q=0.8",
    "en-US,en;q=0.9,zh;q=0.7",
]

BLOCKED_STATUS = {401, 403, 406, 429, 451, 503, 520, 521, 522, 523}

BLOCKED_KEYWORDS = [
    "cloudflare", "cf-challenge", "captcha", "access denied",
    "forbidden", "bot detection", "robot check", "please verify you are human",
]

TLS_BROWSERS = ("chrome", "edge", "safari")

# ---------------------------------------------------------------------------
# HTML → 纯文本转换器（轻量级，无外部依赖）
# ---------------------------------------------------------------------------

class HTMLToText(HTMLParser):
    """将 HTML 转为可读纯文本。"""

    SKIP_TAGS = {"script", "style", "head", "noscript", "svg", "nav", "footer", "header"}

    def __init__(self):
        super().__init__()
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.SKIP_TAGS:
            self._skip_depth += 1
        if tag.lower() in ("br", "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr"):
            self._parts.append("\n")

    def handle_endtag(self, tag):
        if tag.lower() in self.SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)

    def handle_data(self, data):
        if self._skip_depth == 0:
            self._parts.append(data)

    def get_text(self) -> str:
        raw = "".join(self._parts)
        # 合并多余空行
        return re.sub(r"\n{3,}", "\n\n", raw).strip()


def html_to_text(html: str) -> str:
    parser = HTMLToText()
    parser.feed(html)
    return parser.get_text()


# ---------------------------------------------------------------------------
# 构建请求头（模拟真实浏览器）
# ---------------------------------------------------------------------------

def build_headers(url: str, attempt: int = 0) -> dict:
    """构建接近真实浏览器的请求头。"""
    ua = USER_AGENTS[attempt % len(USER_AGENTS)]
    headers = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": ACCEPT_LANGUAGES[attempt % len(ACCEPT_LANGUAGES)],
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Sec-Fetch-Site": "none" if attempt == 0 else "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }
    # Chrome 特有的 Client Hints
    if "Chrome" in ua:
        headers["sec-ch-ua"] = '"Chromium";v="126", "Google Chrome";v="126", "Not.A/Brand";v="24"'
        headers["sec-ch-ua-mobile"] = "?0"
        platform = '"Windows"' if "Windows" in ua else '"macOS"' if "Macintosh" in ua else '"Linux"'
        headers["sec-ch-ua-platform"] = platform

    # 构造看起来合理的 Referer
    host = urlparse(url).hostname or ""
    parts = [p for p in host.split(".") if p]
    if len(parts) >= 2:
        headers["Referer"] = f"https://www.google.com/search?q={parts[-2]}"

    return headers


def is_blocked(status: int, body: str) -> bool:
    """检测是否被反爬拦截。"""
    if status in BLOCKED_STATUS:
        return True
    lowered = body.lower()
    return any(kw in lowered for kw in BLOCKED_KEYWORDS)


# ---------------------------------------------------------------------------
# Layer 1: urllib（标准库，零依赖）
# ---------------------------------------------------------------------------

def fetch_urllib(url: str, timeout: int = 30) -> tuple[int, str]:
    """用 Python 标准库 urllib 获取页面。"""
    headers = build_headers(url, attempt=0)
    req = Request(url, headers=headers)
    try:
        import gzip
        import io
        resp = urlopen(req, timeout=timeout)
        status = resp.getcode()
        data = resp.read()
        # 处理 gzip
        if resp.headers.get("Content-Encoding") == "gzip":
            data = gzip.GzipFile(fileobj=io.BytesIO(data)).read()
        # 检测编码
        content_type = resp.headers.get("Content-Type", "")
        charset = "utf-8"
        if "charset=" in content_type:
            charset = content_type.split("charset=")[-1].split(";")[0].strip()
        body = data.decode(charset, errors="replace")
        return status, body
    except HTTPError as e:
        return e.code, ""
    except (URLError, TimeoutError, OSError) as e:
        return 0, f"Error: {e}"


# ---------------------------------------------------------------------------
# Layer 2: curl_cffi TLS 指纹伪装（可选）
# ---------------------------------------------------------------------------

def fetch_curl_cffi(url: str, timeout: int = 30) -> tuple[int, str] | None:
    """用 curl_cffi 发起带 TLS 指纹伪装的请求。"""
    try:
        from curl_cffi import requests as curl_requests
    except ImportError:
        return None

    for attempt in range(3):
        browser = TLS_BROWSERS[attempt % len(TLS_BROWSERS)]
        headers = build_headers(url, attempt=attempt + 1)
        try:
            resp = curl_requests.get(
                url,
                headers=headers,
                timeout=timeout,
                allow_redirects=True,
                impersonate=browser,
            )
            status = resp.status_code
            body = resp.text or ""
            if not is_blocked(status, body):
                return status, body
            # 被拦截则换个浏览器指纹重试
            time.sleep(0.3 + attempt * 0.3 + random.uniform(0.05, 0.3))
        except Exception:
            time.sleep(0.3 + attempt * 0.3)
    return None


# ---------------------------------------------------------------------------
# Layer 3: Playwright 浏览器渲染（可选）
# ---------------------------------------------------------------------------

def fetch_playwright(url: str, timeout: int = 30) -> tuple[int, str] | None:
    """用 Playwright 无头浏览器获取 JS 渲染后的页面。"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent=random.choice(USER_AGENTS),
                viewport={"width": 1920, "height": 1080},
                locale="zh-CN",
            )
            page = context.new_page()
            resp = page.goto(url, wait_until="networkidle", timeout=timeout * 1000)
            status = resp.status if resp else 0
            body = page.content()
            browser.close()
            return status, body
    except Exception as e:
        return None


# ---------------------------------------------------------------------------
# 主逻辑：分层降级
# ---------------------------------------------------------------------------

def fetch(url: str, use_js: bool = False, timeout: int = 30) -> dict:
    """
    分层降级获取网页内容。

    返回 dict:
      success: bool
      url: str
      status: int
      html: str
      text: str
      layer: str  — 成功使用的策略层
      error: str | None
    """
    result = {"success": False, "url": url, "status": 0, "html": "", "text": "", "layer": "", "error": None}

    # 如果指定 --js，直接跳到 Playwright
    if use_js:
        pw_result = fetch_playwright(url, timeout)
        if pw_result:
            status, body = pw_result
            if status == 200 and body and not is_blocked(status, body):
                result.update(success=True, status=status, html=body, text=html_to_text(body), layer="playwright")
                return result
        result["error"] = "Playwright fetch failed or not installed (pip install playwright && playwright install chromium)"
        return result

    # Layer 1: urllib（标准库）
    status, body = fetch_urllib(url, timeout)
    if status == 200 and body and not is_blocked(status, body):
        result.update(success=True, status=status, html=body, text=html_to_text(body), layer="urllib")
        return result

    # Layer 2: curl_cffi TLS 伪装
    cffi_result = fetch_curl_cffi(url, timeout)
    if cffi_result:
        status, body = cffi_result
        if status == 200 and body and not is_blocked(status, body):
            result.update(success=True, status=status, html=body, text=html_to_text(body), layer="curl_cffi")
            return result

    # Layer 3: Playwright 浏览器渲染
    pw_result = fetch_playwright(url, timeout)
    if pw_result:
        status, body = pw_result
        if status == 200 and body and not is_blocked(status, body):
            result.update(success=True, status=status, html=body, text=html_to_text(body), layer="playwright")
            return result

    # 全部失败
    result["error"] = f"All layers failed. Last status: {status}"
    result["status"] = status
    return result


# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Robust web page fetcher with anti-bot fallback")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--js", action="store_true", help="Force Playwright JS rendering")
    parser.add_argument("--output", choices=["html", "text", "json"], default="text",
                        help="Output format (default: text)")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout in seconds (default: 30)")
    args = parser.parse_args()

    result = fetch(args.url, use_js=args.js, timeout=args.timeout)

    if args.output == "json":
        # json 模式输出完整结果（不含 html 以节省空间）
        out = {k: v for k, v in result.items() if k != "html"}
        print(json.dumps(out, ensure_ascii=False, indent=2))
    elif args.output == "html":
        if result["success"]:
            print(result["html"])
        else:
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)
    else:  # text
        if result["success"]:
            print(result["text"])
        else:
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)

    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
