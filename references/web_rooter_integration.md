# Web Access Strategy: Chinese University & Social Platform Fallback

Chinese university websites (`.edu.cn`) frequently restructure URLs, deploy anti-bot measures, or require JavaScript rendering. DeepTutor bundles self-contained scripts (derived from [Web-Rooter](https://github.com/pinkpixel-dev/web-rooter), MIT License) to handle these cases without external dependencies.

## Bundled Scripts

| Script | Purpose | Dependencies |
|--------|---------|-------------|
| `scripts/robust_fetch.py` | Anti-bot web fetch with 3-layer fallback | None (stdlib only; curl_cffi and playwright optional) |
| `scripts/search_social.py` | Chinese social platform search via search engine proxy | None (stdlib only) |

## Activation Conditions

Use the bundled scripts when ANY of the following occurs:
1. `WebFetch` returns **404 / 403 / 5xx** on a `.edu.cn` domain
2. `WebFetch` returns **empty or garbled content** (anti-bot page, login wall)
3. `WebFetch` **times out** on a Chinese website
4. You need to search **social platforms** (知乎, 小红书, 小木虫) for professor reviews

## Faculty Page Fetch: 3-Layer Fallback

When `WebFetch` fails on a faculty page, use `robust_fetch.py`:

```bash
# Layer 1-3 automatic fallback: urllib → curl_cffi → playwright
python scripts/robust_fetch.py "https://example.edu.cn/faculty/page.htm"

# Force JS rendering (skip straight to Playwright)
python scripts/robust_fetch.py "https://example.edu.cn/faculty/page.htm" --js

# Get full JSON result with metadata
python scripts/robust_fetch.py "https://example.edu.cn/faculty/page.htm" --output json
```

**Fallback chain inside the script:**
```
Layer 1: urllib (stdlib) — better headers, UA rotation, Sec-Fetch hints
  ↓ blocked/failed
Layer 2: curl_cffi — TLS fingerprint impersonation (Chrome/Edge/Safari)
  ↓ blocked/failed
Layer 3: Playwright — full headless browser rendering
```

If ALL layers fail, the URL itself is probably outdated. Re-search:
```bash
# Use WebSearch to find the current URL
WebSearch("site:example.edu.cn 教授姓名")
# Then retry with the new URL
```

## Social Platform Search (Phase 6)

For professor reviews on Chinese social platforms, use `search_social.py`:

```bash
# Search 知乎 + 小红书 + 小木虫 (defaults)
python scripts/search_social.py "导师名 大学名"

# Specify platforms
python scripts/search_social.py "导师名 大学名" --platforms zhihu,xiaohongshu,emuch,tieba,baoyan,kaoyan

# JSON output for structured processing
python scripts/search_social.py "导师名 大学名" --format json --top 10
```

**How it works:** Instead of directly scraping social platforms (which require login/signing), the script searches via Bing and Sogou using `site:` queries. Search engine caches provide public content snippets even for login-gated platforms.

**Supported platforms:**

| Key | Platform | What to Find |
|-----|----------|-------------|
| `zhihu` | 知乎 | Lab culture, student experiences, detailed reviews |
| `xiaohongshu` | 小红书 | Recent student experiences |
| `emuch` | 小木虫 | Grad student discussions, lab reputation |
| `tieba` | 百度贴吧 | University-specific discussions |
| `baoyan` | 保研论坛 | Recommendation letters, interview experiences |
| `kaoyan` | 考研帮 | Advisor selection discussions |

## Phase-Specific Usage

| Phase | When to Use | Command |
|-------|------------|---------|
| **Phase 1: Identity** | Faculty page 404/empty | `python scripts/robust_fetch.py <URL>` |
| **Phase 2: Students** | Lab member page behind JS | `python scripts/robust_fetch.py <lab-url> --js` |
| **Phase 5: Funding** | NSFC database blocks | `python scripts/robust_fetch.py <URL> --js` |
| **Phase 6: Social** | Professor reviews | `python scripts/search_social.py "导师名 大学"` |

## URL Freshness Rule

Chinese university URLs go stale fast. When Phase 1 identifies a professor:

1. First try the URL from search results via `WebFetch`
2. If fails → retry with `python scripts/robust_fetch.py <URL>`
3. If still fails → re-search: `WebSearch("site:<university-domain> 教授姓名")`
4. If still fails → navigate from the university's faculty directory listing page

## Optional Enhancement

If the user has [Web-Rooter](https://github.com/pinkpixel-dev/web-rooter) installed (`wr` command available), prefer using `wr` commands for even better results:
- `wr html <URL> --js` instead of `robust_fetch.py --js`
- `wr social "query" --platform=zhihu,xiaohongshu` instead of `search_social.py`
- `wr doctor` for environment diagnostics
