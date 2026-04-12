#!/usr/bin/env python3
"""
search_social.py — 中国社交平台搜索工具（导师评价专用）
从 Web-Rooter (MIT License, github.com/pinkpixel-dev/web-rooter) 的社交搜索理念简化而来。

通过搜索引擎中转搜索知乎、小红书、小木虫、百度贴吧等平台的导师评价，
无需登录、无需 Cookie、无需专用 API。

用法:
  python search_social.py "导师名 学校" [--platforms zhihu,xiaohongshu,emuch,tieba] [--top 10]

原理:
  不直接爬社交平台（需要登录/签名），而是通过搜索引擎 site: 搜索来获取公开内容。
  这是最稳健的方式——搜索引擎的缓存即使原页面需要登录也能提供摘要。
"""

import argparse
import json
import re
import sys
import time
import random
from urllib.parse import quote_plus, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# ---------------------------------------------------------------------------
# 平台配置
# ---------------------------------------------------------------------------

PLATFORMS = {
    "zhihu": {
        "name": "知乎",
        "site": "zhihu.com",
        "keywords": ["评价", "怎么样", "读研", "课题组", "实验室"],
    },
    "xiaohongshu": {
        "name": "小红书",
        "site": "xiaohongshu.com",
        "keywords": ["导师", "读研", "课题组", "实验室"],
    },
    "emuch": {
        "name": "小木虫",
        "site": "emuch.net",
        "keywords": ["导师", "实验室", "课题组", "评价"],
    },
    "tieba": {
        "name": "百度贴吧",
        "site": "tieba.baidu.com",
        "keywords": ["导师", "评价", "怎么样"],
    },
    "baoyan": {
        "name": "保研论坛",
        "site": "baoyan.net",
        "keywords": ["导师", "推免", "夏令营"],
    },
    "kaoyan": {
        "name": "考研帮",
        "site": "kaoyan.com",
        "keywords": ["导师", "选导师", "研究生"],
    },
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
]


# ---------------------------------------------------------------------------
# 搜索引擎中转
# ---------------------------------------------------------------------------

def search_via_bing(query: str, site: str, top: int = 5) -> list[dict]:
    """
    通过 Bing 搜索获取指定平台的公开内容。
    Bing 对 site: 搜索的限制比 Google 宽松，不容易触发验证码。
    """
    search_query = f"site:{site} {query}"
    encoded = quote_plus(search_query)
    url = f"https://www.bing.com/search?q={encoded}&count={top}"

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    try:
        req = Request(url, headers=headers)
        resp = urlopen(req, timeout=15)
        html = resp.read().decode("utf-8", errors="replace")
        return parse_bing_results(html, site)
    except (HTTPError, URLError, TimeoutError) as e:
        return [{"error": f"Bing search failed: {e}"}]


def parse_bing_results(html: str, site: str) -> list[dict]:
    """从 Bing 搜索结果 HTML 中提取标题、链接、摘要。"""
    results = []

    # 匹配 Bing 搜索结果块（<li class="b_algo" ...>）
    blocks = re.findall(r'<li class="b_algo"[^>]*>(.*?)</li>', html, re.DOTALL)

    for block in blocks:
        # 提取链接和标题
        link_match = re.search(r'<a\s[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
        if not link_match:
            continue

        url = link_match.group(1)
        title = re.sub(r"<[^>]+>", "", link_match.group(2)).strip()

        # 只保留目标平台的结果
        if site not in url:
            continue

        # 清理标题：移除 Bing 添加的域名前缀（如 "zhihu.comhttps://..."）
        title = re.sub(r'^[a-z]+\.[a-z]+\.?[a-z]*https?://[^\s]*', '', title).strip()
        if not title:
            title = "(无标题)"

        # 提取摘要
        snippet_match = re.search(r'<p[^>]*>(.*?)</p>', block, re.DOTALL)
        snippet = ""
        if snippet_match:
            snippet = re.sub(r"<[^>]+>", "", snippet_match.group(1)).strip()

        results.append({
            "title": title,
            "url": url,
            "snippet": snippet,
        })

    return results


def search_via_sogou(query: str, site: str, top: int = 5) -> list[dict]:
    """
    搜狗搜索备用方案。搜狗是微信公众号的官方搜索引擎，
    对中文内容的覆盖比 Bing 更好。
    """
    search_query = f"site:{site} {query}"
    encoded = quote_plus(search_query)
    url = f"https://www.sogou.com/web?query={encoded}&num={top}"

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    try:
        req = Request(url, headers=headers)
        resp = urlopen(req, timeout=15)
        html = resp.read().decode("utf-8", errors="replace")
        return parse_sogou_results(html, site)
    except (HTTPError, URLError, TimeoutError) as e:
        return [{"error": f"Sogou search failed: {e}"}]


def parse_sogou_results(html: str, site: str) -> list[dict]:
    """从搜狗搜索结果中提取内容。"""
    results = []
    blocks = re.findall(r'<div class="vrwrap">(.*?)</div>\s*</div>', html, re.DOTALL)
    if not blocks:
        blocks = re.findall(r'<div class="rb">(.*?)</div>', html, re.DOTALL)

    for block in blocks:
        link_match = re.search(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
        if not link_match:
            continue

        url = link_match.group(1)
        title = re.sub(r"<[^>]+>", "", link_match.group(2)).strip()

        snippet = ""
        for pattern in [r'<p class="str[^"]*">(.*?)</p>', r'<div class="ft">(.*?)</div>']:
            match = re.search(pattern, block, re.DOTALL)
            if match:
                snippet = re.sub(r"<[^>]+>", "", match.group(1)).strip()
                break

        results.append({"title": title, "url": url, "snippet": snippet})

    return results


# ---------------------------------------------------------------------------
# 主搜索逻辑
# ---------------------------------------------------------------------------

def search_professor_reviews(
    query: str,
    platforms: list[str] | None = None,
    top: int = 5,
) -> dict:
    """
    在指定的中国社交平台上搜索导师评价。

    Args:
        query: 搜索词（如 "张教授 北京大学"）
        platforms: 平台列表（默认全部）
        top: 每个平台返回的最大结果数

    Returns:
        dict: {platform_name: [results], ...}
    """
    if platforms is None:
        platforms = list(PLATFORMS.keys())

    all_results = {}

    for platform_key in platforms:
        if platform_key not in PLATFORMS:
            all_results[platform_key] = [{"error": f"Unknown platform: {platform_key}"}]
            continue

        platform = PLATFORMS[platform_key]
        # 构建搜索词：原始查询 + 平台特定关键词（取前2个）
        keywords = " ".join(platform["keywords"][:2])
        full_query = f"{query} {keywords}"

        # 优先 Bing，失败则 搜狗
        results = search_via_bing(full_query, platform["site"], top)
        if not results or (len(results) == 1 and "error" in results[0]):
            time.sleep(0.5)
            results = search_via_sogou(full_query, platform["site"], top)

        all_results[platform["name"]] = results

        # 礼貌性延迟，避免被搜索引擎封
        time.sleep(0.5 + random.uniform(0.1, 0.5))

    return all_results


# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Search Chinese social platforms for professor reviews"
    )
    parser.add_argument("query", help="Search query (e.g., '张教授 北京大学')")
    parser.add_argument(
        "--platforms",
        default="zhihu,xiaohongshu,emuch",
        help="Comma-separated platform list (default: zhihu,xiaohongshu,emuch)",
    )
    parser.add_argument("--top", type=int, default=5, help="Max results per platform (default: 5)")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format")
    args = parser.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",")]
    results = search_professor_reviews(args.query, platforms, args.top)

    if args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for platform_name, items in results.items():
            print(f"\n{'='*60}")
            print(f" {platform_name}")
            print(f"{'='*60}")
            if not items:
                print("  (无结果)")
                continue
            for i, item in enumerate(items, 1):
                if "error" in item:
                    print(f"  Error: {item['error']}")
                    continue
                print(f"\n  [{i}] {item.get('title', '(无标题)')}")
                print(f"      {item.get('url', '')}")
                if item.get("snippet"):
                    print(f"      {item['snippet'][:200]}")


if __name__ == "__main__":
    main()
