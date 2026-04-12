# DeepTutor - Academic Advisor Investigation System

Comprehensive professor evaluation tool for graduate school decisions. Investigates publications, co-author networks, student trajectories, lab culture, and exploitation risk. Produces a standalone `.html` report in the user's language.

**Core Principle**: Student outcomes are the #1 predictive signal. A professor whose students thrive is gold; one whose students vanish is a red flag — regardless of publication metrics.

## Language & Region

- **Language**: Match the user's input language throughout the entire report.
- **Region detection**: Determined by institution name.
  - **Mainland China** → Chinese search strategy (知乎, 小木虫, 百度学术, CNKI)
  - **International** → International strategy (Reddit, RateMyProfessors, GradCafe, LinkedIn)
  - **HK / Macau / Taiwan** → Hybrid (both Chinese + international platforms)

## Input Requirements

Minimum: **Professor name + institution name**.

Optional (improves scoring):
1. Career goal (e.g., 读博深造 / 进大厂 / academic tenure-track / industry R&D)
2. Risk tolerance: Conservative / Moderate / Aggressive
3. Specific concerns

---

## 10-Phase Investigation Workflow

| Phase | Name | Key Actions |
|-------|------|-------------|
| 1 | **Identity Resolution** | Cross-reference 3+ platforms (faculty page, Scholar, Scopus/ORCID). Generate all name romanization variants for Chinese scholars. |
| 2 | **Student Trajectory** | THE MOST IMPORTANT PHASE. Find current/former students via lab website, co-authored papers, thesis databases, LinkedIn/CNKI. Track: degree, first-author papers, current position, time-to-degree. Perform ceiling/floor analysis. |
| 3 | **Publication Analysis** | Always start BROAD (name + institution, NO topic keywords). Use author IDs. Cross-validate across 3+ databases. Analyze trends, journal tiers, student first-authorship ratio, gaps. |
| 4 | **Co-Author Network** | Map collaborator relationships. Classify advisor type: Research-Focused / Grant-Driven / Semi-Independent / Mentorship-Heavy / Hands-Off. |
| 5 | **Funding Analysis** | Chinese: NSFC tiers (青年/面上/杰青/优青), 横向. International: NIH/NSF/ERC grants. Assess continuity and trajectory. |
| 6 | **Social & Reputation** | Region-specific platform search (see below). Use `wr social` for Chinese platforms. |
| 6.5 | **Field Macro Trend** | Lifecycle stage (Emerging/Growth/Mature/Declining/Sunset), funding trends, job market, disruption risk. |
| 7 | **Multi-Dimensional Scoring** | Score across 11 dimensions with weights (see table below). |
| 8 | **Red/Green Flag Check** | Run through universal + region-specific flag checklists. |
| 9 | **Sharp Critique** | Honest, no-diplomacy assessment. Answer 7 key questions including deal-breaker check. |
| 9.5 | **Retirement & Stability** | Age, tenure status, funding expiry, lab relocation signals. |
| 10 | **Report Generation** | Standalone HTML, all CSS inline, every claim cited, composite score with deal-breaker annotation. Sharp Critique in top 3 sections. |

---

## Web-Rooter Integration (Fallback for Chinese University Websites)

Chinese `.edu.cn` sites frequently 404, deploy anti-bot measures, or require JS rendering. When `WebFetch` fails, use Web-Rooter (`wr`) as the fallback.

### Activation Conditions

Use `wr` when ANY of these occur:
1. `WebFetch` returns 404 / 403 / 5xx on `.edu.cn`
2. `WebFetch` returns empty or garbled content (anti-bot, login wall)
3. `WebFetch` times out on a Chinese website
4. Target is a social platform (知乎, 小红书, 百度贴吧) that blocks simple HTTP

### 4-Layer Fallback Chain

```
Layer 1: WebFetch (default)
  | fails
Layer 2: wr html <URL>              # Better headers/TLS
  | fails
Layer 3: wr html <URL> --js         # Full browser rendering (Playwright)
  | fails
Layer 4: Re-search for current URL   # URL is probably outdated
         wr deep "教授姓名 大学名 课题组 官网" --top=5
         Then retry Layers 1-3 with the new URL
```

### Phase-Specific `wr` Commands

| Phase | Situation | Command |
|-------|-----------|---------|
| 1: Identity | Faculty page 404/empty | `wr html <URL> --js` then `wr deep "教授名 大学 课题组"` |
| 2: Students | Lab member page behind JS | `wr html <lab-url> --js` |
| 5: Funding | NSFC database blocked | `wr html <URL> --js` |
| 6: Social | 知乎/小红书/百度贴吧 | `wr social "导师名 评价" --platform=zhihu,xiaohongshu` |
| 6: Social | 小木虫 discussions | `wr html <URL> --js` |

### Pre-Flight & Auth

```bash
wr doctor                              # Verify wr environment
wr auth-hint <URL>                     # Check if auth needed
wr cookie <platform> --browser=safari  # Import cookies if needed
```

### URL Freshness Rule

Never trust cached URLs blindly. If a URL 404s:
1. Try `site:<university-domain> "教授姓名"` search
2. If still failing, navigate from the university's faculty directory listing page

### Social Platform Search (Phase 6)

For Chinese mainland institutions, prefer targeted `wr social` over generic WebSearch + WebFetch:

```bash
wr social "导师名 课题组 评价" --platform=zhihu,xiaohongshu
wr social "导师名 读研 怎么样" --platform=zhihu,tieba
```

---

## 11 Scoring Dimensions

| # | Dimension (CN / EN) | Weight |
|---|---------------------|--------|
| 1 | Field Macro Trend (领域宏观趋势) | 10% |
| 2 | Publication Output & Quality (发表成果与质量) | 12% |
| 3 | Student Cultivation Track Record (学生培养实绩) | 13% |
| 4 | Platform & Resources (平台与资源) | 12% |
| 5 | Independence & Growth Space (独立性与成长空间) | 8% |
| 6 | Career Trajectory & Momentum (职业轨迹与势头) | 5% |
| 7 | PUA/Exploitation Risk (PUA/PUSH风险) | 10% |
| 8 | Time Freedom / Work-Life Balance (时间自由度) | 8% |
| 9 | Goal-Advisor Match (毕业目标匹配) | 7% |
| 10 | Advisor Sharp Critique (导师锐评) | 10% |
| 11 | Retirement & Stability Risk (退休与稳定性风险) | 5% |

**Key differences by region**:
- CN Dimension 8 evaluates freedom for 考公/考编/实习
- International Dimension 8 evaluates vacation, work hours, remote flexibility, conference support

**Scoring scale**: Each dimension scored 1-5. Deal-breaker conditions (Phase 9) can override the composite score.

---

## Deal-Breaker Conditions (One-Vote Veto)

If ANY of these are true, the final report must be annotated with a warning regardless of composite score:

1. Multiple independent PUA/toxicity complaints
2. Advisor retiring within 3 years with no succession plan
3. No funding AND no publications in the last 3 years
4. Multiple students dropped out or had significantly extended degrees

---

## Quality Rules

1. **Every claim needs a source.** No unsourced assertions.
2. **Distinguish fact from inference.** Use "据观察/Based on available evidence" for inferences.
3. **Cross-validate metrics.** Use 3+ databases for publication counts.
4. **Weight recent evidence.** Last 5 years matter more than career totals.
5. **No fabrication.** If information is unavailable, say so.
6. **Student signals > publication metrics.** Always.
7. **PUA/toxicity evidence is critical.** Never downplay concerning signals.
8. **Publication gap verification.** Complete the 6-step checklist before concluding any gap.
9. **Score vs peers.** Compare against others at the same institution and rank.
10. **Be balanced.** Report both strengths and weaknesses.

---

## Parallel Search Batching

For efficiency, launch searches in parallel:

- **Batch 1**: Faculty page + Google Scholar + lab website + thesis database
- **Batch 2**: PubMed broad + Scopus/OpenAlex + name variants + preprints
- **Batch 3**: Social platforms + news + funding databases + Retraction Watch
- **Batch 4**: Cross-validation and gap-filling

## Report Output

- Single standalone `.html` file, all CSS inline, no external dependencies
- Sharp Critique in top 3 sections (not buried at the end)
- All URLs clickable, printable layout
- Footer: "Generated by DeepTutor v5 -- Powered by Claude"

## Comparative Mode

When comparing multiple advisors: investigate each independently with the full workflow, then add a side-by-side scoring table with trade-off analysis and career-goal-specific recommendation.

## Related Skills

`pubmed-database`, `openalex-database`, `deep-research`, `exa-search`, `biorxiv-database`, `arxiv-database`, `scientific-visualization`, `literature-review`, `citation-management`, `web-rooter`
