# DeepTutor Lite Mode — Streamlined Investigation for Lower-Capability Models

## 6-Phase Lite Workflow

| Lite Phase | Maps to Full Phase | What to Do |
|-----------|-------------------|-----------|
| L1: Identity | Phase 1 | Faculty page + Google Scholar only (skip 3-platform cross-verification) |
| L2: Students | Phase 2 | Lab website members page only (skip thesis DB / LinkedIn deep search) |
| L3: Publications | Phase 3 | Single database (PubMed or Scholar), skip name variant explosion |
| L4: Social | Phase 6 | `scripts/search_social.py` only (skip manual platform-by-platform search) |
| L5: Scoring | Phase 7 | 7 dimensions (see below) |
| L6: Report | Phase 10 | Generate JSON → `scripts/generate_report.py` (model never writes HTML) |

**Phases skipped in Lite mode:**
- Phase 4 (Co-Author Network) — requires multi-source cross-referencing
- Phase 5 (Funding Analysis) — requires grant database querying
- Phase 6.5 (Field Macro Trend) — simplified to a single lifecycle label
- Phase 8 (Red/Green Flag Check) — merged into L5 scoring
- Phase 9 (Sharp Critique) — simplified template (see below)
- Phase 9.5 (Retirement Risk) — dropped from scoring

## Lite Scoring Dimensions (7 instead of 11)

| # | Dimension | Weight | What to Assess |
|---|-----------|--------|---------------|
| 1 | 领域宏观趋势 / Field Trend | 15% | Single lifecycle label (萌芽/上升/成熟/衰退/夕阳) with brief justification |
| 2 | 发表成果与质量 / Publications | 15% | Total count, h-index, best journal tier |
| 3 | 学生培养实绩 / Student Outcomes | 20% | Known student destinations (THE most important) |
| 4 | 平台与资源 / Platform & Resources | 15% | Institution tier, lab size, basic equipment |
| 5 | PUA/PUSH风险 / Exploitation Risk | 15% | Social platform search results summary |
| 6 | 导师锐评 / Sharp Critique | 15% | Simplified 5-line template (see below) |
| 7 | 毕业目标匹配 / Goal Match | 5% | Basic compatibility check |

## Lite Sharp Critique Template

Instead of the full 7-question framework, use this structured fill-in:

```
一句话判决：[推荐/谨慎/不推荐] — [一句话理由]
最大优点：[基于证据的一句话]
最大风险：[基于证据的一句话]
适合什么样的学生：[一句话]
不适合什么样的学生：[一句话]
```

English version:
```
Verdict: [Recommended/Caution/Not Recommended] — [one sentence reason]
Top strength: [one evidence-based sentence]
Top risk: [one evidence-based sentence]
Best suited for: [one sentence]
Not suited for: [one sentence]
```

## Lite Report Sections (7 instead of 18)

The Lite HTML report includes only these sections:

1. **Sharp Critique** — Simplified 5-line template
2. **Scoring** — 7 dimensions with composite score
3. **Student Outcomes** — Known students table
4. **Key Flags** — Combined red/green flags (from social search + obvious signals)
5. **Basic Info** — Name, title, institution, contact
6. **Publications** — Count, h-index, top 3 papers
7. **Summary & Next Steps** — 2-3 actionable items

## Lite Report Generation

The model outputs JSON in the same format as the Full version (see `scripts/generate_report.py`), but with fewer populated fields. The script handles missing fields gracefully — it shows "信息不足" for sections without data.

```bash
python scripts/generate_report.py lite_report.json -o report.html
```

## Quality Rules (Lite-Specific)

1. **Never fabricate.** With fewer data sources, the temptation to fill gaps is higher. Say "信息不足" rather than guess.
2. **Student outcomes are still #1.** Even in Lite mode, student trajectories outweigh everything else.
3. **Use the scripts.** Always use `search_social.py` for social search and `generate_report.py` for HTML — never hand-write HTML or scrape platforms manually.
4. **Single-source is OK.** Lite mode allows single-database publication counts (unlike Full which requires 3+ databases). Note the source explicitly.
5. **Cite everything.** Every claim still needs a URL source, even with fewer claims total.
