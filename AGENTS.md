# DeepTutor — Academic Advisor Investigation System

> Single source of truth for [agents.md](https://agents.md/) compliant tools (Codex CLI, OpenCode, OpenClaw, Aider, Cline, Continue, etc.). For Claude Code and Cursor, see `SKILL.md` and `.cursor/rules/deeptutor.mdc` — both reference this file's workflow.

Comprehensive professor evaluation tool for graduate-school decisions. Investigates publications, co-author networks, **student trajectories** (the single most predictive signal), lab culture, and exploitation/PUA risk. Produces a standalone `.html` report in the user's language.

**Core principle**: *Your ceiling = your seniors' ceiling.* A professor whose students thrive is gold; one whose students vanish is a red flag — regardless of publication metrics.

---

## What this repo is

This is **not a traditional code project** — it is an AI "skill" / agent prompt-pack. There is nothing to `build` or `npm install`. When a user asks the assistant to evaluate a professor, the assistant should:

1. Detect language and region from the user's input.
2. Run the 10-phase investigation workflow below (or the 6-phase Lite variant for lower-capability models).
3. Output structured JSON, then render to HTML via `scripts/generate_report.py`.

The Python scripts in `scripts/` are self-contained helpers — call them as needed; do not require additional pip installs beyond Python's standard library and (optionally) `playwright` for JS rendering.

---

## When to trigger

Activate this workflow whenever a user asks to investigate, evaluate, or compare graduate advisors. Trigger phrases include:

- Chinese: `调查导师`, `评估教授`, `选导师`, `导师怎么样`, `能不能跟这个老师读研`, `这个导师push吗`, `帮我看看XX老师`, `对比这几个导师`
- English: `investigate this advisor`, `should I join this lab`, `evaluate professor`, `is this prof good`, `rate my potential advisor`, `review this PI`, `compare these advisors`
- Implicit: user provides `<professor name> + <institution>` with any evaluation intent.

Minimum input: **professor name + institution**. If missing, ask. Optionally ask for career goal, risk tolerance, and specific concerns to improve scoring.

---

## Language & Region

- **Language**: Match the user's input language throughout the entire report (titles, analysis, recommendations). Never mix languages except when quoting original sources.
- **Region detection** (determines search platforms and scoring weights):

| Region | Examples | Strategy |
|--------|----------|----------|
| Mainland China | 北大、清华、中科院、苏州大学等 | 知乎 / 小木虫 / 百度学术 / CNKI / 保研论坛 / 小红书 / 考研帮 |
| International | MIT, Stanford, ETH, UTokyo, NUS… | Reddit / RateMyProfessors / GradCafe / LinkedIn / Glassdoor / Retraction Watch |
| HK / Macau / Taiwan | HKU, CUHK, NTU, NTHU… | Hybrid (both Chinese and international platforms) + PTT / LIHKG / Dcard |

When uncertain, ask the user.

---

## Model capability — choose Full or Lite

| Model class | Mode | Behavior |
|-------------|------|----------|
| Claude Opus 4.6+, Claude Sonnet 4.6+, GPT-5 / GPT-5-Codex, Gemini 2.5 Pro, and equivalent | **Full** | Run without asking |
| GPT-4o, Gemini Flash, GLM, MiniMax, Claude Haiku, smaller open models | **Prompt user** | Offer choice: Full (10 phases / 11 dimensions / 18 sections) vs Lite (6 phases / 7 dimensions / 7 sections, ~40% of tokens) |

If unsure of model class, default to prompting. Lite specification: `references/lite_mode.md`.

---

## 10-Phase Investigation Workflow (Full)

| Phase | Name | Key Actions |
|-------|------|-------------|
| 1 | **Identity Resolution** | Cross-reference 3+ platforms (faculty page, Scholar, Scopus/ORCID, Semantic Scholar). Generate all name romanization variants for Chinese scholars — see `references/publication_search_protocol.md`. |
| 2 | **Student Trajectory** ⭐ | THE MOST IMPORTANT PHASE. Find current/former students via lab page, co-authored papers, theses (CNKI/万方/ProQuest), LinkedIn. Track degree, first-author papers, current position, time-to-degree. Perform ceiling/floor analysis. |
| 3 | **Publication Analysis** | Always start BROAD (name + institution, NO topic keywords). Use author IDs. Cross-validate across 3+ databases. Analyze trends, journal tiers, student first-authorship ratio, gaps (use the 6-step gap-verification checklist before concluding any gap). |
| 4 | **Co-Author Network** | Map collaborator relationships. Classify advisor type: Research-Focused (学术型) / Grant-Driven (项目型) / Semi-Independent (半放养型) / Mentorship-Heavy (指导型) / Hands-Off (纯放养型). |
| 5 | **Funding Analysis** | Chinese: NSFC tiers (青年/面上/重点/杰青/优青), 横向, 973, 重点研发. International: NIH R01/R21, NSF CAREER, ERC, EPSRC, DFG, JSPS, HHMI, Wellcome, Gates. Assess continuity, trajectory, diversity. |
| 6 | **Social & Reputation** | Region-specific platform search (see below). Prefer `wr social` for Chinese platforms when `WebFetch` is blocked. |
| 6.5 | **Field Macro Trend** | Lifecycle stage (Emerging 🌱 / Growth 📈 / Mature 📊 / Declining 📉 / Sunset ☠️), funding trends, job market, AI/tech disruption risk, China-vs-international divergence. |
| 7 | **Multi-Dimensional Scoring** | Score across 11 weighted dimensions (see table below). Detailed rubrics: `references/advisor_evaluation_framework.md`. |
| 8 | **Red/Green Flag Check** | Universal + region-specific flag checklists. |
| 9 | **Advisor Sharp Critique (锐评)** | Honest, no-diplomacy assessment. Answer 7 key questions including the deal-breaker check. *"Don't let diplomatic scoring hurt the student — they need a clear go/no-go signal, not 3.7 vs 4.1."* |
| 9.5 | **Retirement & Stability** | Age, tenure status, funding expiry, lab relocation signals, health/productivity trend. |
| 10 | **Report Generation** | Output structured JSON → render via `python scripts/generate_report.py report_data.json -o "教授名_机构.html"`. Standalone HTML, all CSS inline, every claim cited, Sharp Critique in top 3 sections. Schema: `references/report_template.md`. |

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

Each dimension is scored 1–5. Region difference: CN D8 evaluates freedom for 考公/考编/实习; International D8 evaluates vacation policy, work hours, remote flexibility, conference support.

---

## Deal-Breaker Conditions (One-Vote Veto)

If ANY of these are true, the final report MUST be annotated with `⚠️ 存在一票否决风险` regardless of composite score:

1. Multiple independent PUA/toxicity complaints (one is anecdotal; multiple is systemic).
2. Advisor retiring within 3 years with no succession plan.
3. No funding AND no publications in the last 3 years.
4. Multiple documented cases of students dropping out or significantly extended degrees.

---

## Web-Rooter Integration (Fallback for Chinese University Websites)

Chinese `.edu.cn` sites frequently return 404, deploy anti-bot, or require JS rendering. When `WebFetch` fails, escalate via Web-Rooter (`wr`).

### Activation conditions
- `WebFetch` returns 404 / 403 / 5xx on `.edu.cn`
- Empty / garbled content (anti-bot, login wall)
- Timeout on a Chinese website
- Target is a social platform (知乎, 小红书, 百度贴吧) that blocks simple HTTP

### 4-Layer fallback chain

```
Layer 1: WebFetch (default)
  ↓ fails
Layer 2: wr html <URL>              # Better headers/TLS
  ↓ fails
Layer 3: wr html <URL> --js         # Full browser rendering (Playwright)
  ↓ fails
Layer 4: Re-search for current URL  # URL is probably outdated
         wr deep "教授姓名 大学名 课题组 官网" --top=5
         Then retry Layers 1–3 with the new URL
```

### Phase-specific commands

| Phase | Situation | Command |
|-------|-----------|---------|
| 1: Identity | Faculty page 404/empty | `wr html <URL> --js` then `wr deep "教授名 大学 课题组"` |
| 2: Students | Lab member page behind JS | `wr html <lab-url> --js` |
| 5: Funding | NSFC database blocked | `wr html <URL> --js` |
| 6: Social | 知乎/小红书/百度贴吧 | `wr social "导师名 评价" --platform=zhihu,xiaohongshu` |
| 6: Social | 小木虫 discussions | `wr html <URL> --js` |

If `wr` is not installed, fall back to the bundled self-contained scripts:

```bash
python scripts/robust_fetch.py "<URL>"             # auto fallback (3 layers)
python scripts/robust_fetch.py "<URL>" --js        # force browser
python scripts/search_social.py "导师名 大学名" --platforms zhihu,xiaohongshu,emuch
```

Details: `references/web_rooter_integration.md`.

---

## Quality Rules (non-negotiable)

1. **Every claim needs a source.** No unsourced assertions.
2. **Distinguish fact from inference.** Mark speculative conclusions explicitly ("据观察 / Based on available evidence").
3. **Cross-validate metrics.** Use ≥ 3 databases for publication counts.
4. **Weight recent evidence.** Last 5 years matter more than career totals.
5. **No fabrication.** If information is unavailable, say so — don't guess.
6. **Be balanced.** Report both strengths and weaknesses.
7. **Score vs peers.** Compare against others at the same institution and rank.
8. **Student signals > publication metrics.** Always.
9. **PUA/toxicity evidence is critical.** Never downplay concerning signals.
10. **Publication gap verification.** Complete the 6-step checklist before concluding any gap.

---

## Parallel search batching

Maximize efficiency by launching searches in parallel batches:

- **Batch 1**: Faculty page + Google Scholar + lab website + thesis database
- **Batch 2**: PubMed broad + Scopus/OpenAlex + name variants + preprints (bioRxiv/arXiv/medRxiv)
- **Batch 3**: Social platforms + news + funding databases + Retraction Watch
- **Batch 4**: Cross-validation and gap-filling

---

## Report output

- Single standalone `.html` file, all CSS inline, no external dependencies.
- Sharp Critique (锐评) appears in **top 3 sections**, not buried at the end.
- All URLs clickable; printable layout.
- Filename pattern: `教授名_机构.html` (CN) or `firstname_lastname_institution.html` (EN).
- Footer: `Generated by DeepTutor — Powered by <model>`.

Use `scripts/generate_report.py` — output JSON, let the script render HTML. This separates investigation (the model's job) from rendering (deterministic code).

---

## Comparative mode

When comparing multiple advisors: investigate each independently with the full workflow, generate individual reports, then add a side-by-side scoring table with trade-off analysis and a career-goal-specific recommendation card.

---

## Related skills (use if available)

`pubmed-database`, `openalex-database`, `deep-research`, `exa-search`, `biorxiv-database`, `arxiv-database`, `scientific-visualization`, `matplotlib`, `literature-review`, `citation-management`, `web-rooter`.

---

## File layout (for tools that index this repo)

```
deeptutor/
├── AGENTS.md                          ← you are here (Codex CLI / agents.md spec entry)
├── SKILL.md                           ← Claude Code / agentskills.io entry (longer, same content)
├── .cursor/rules/deeptutor.mdc        ← Cursor entry (short pointer)
├── .opencode/AGENTS.md → ../AGENTS.md ← symlink
├── .openclaw/AGENTS.md → ../AGENTS.md ← symlink
├── scripts/
│   ├── generate_report.py             ← JSON → HTML renderer
│   ├── robust_fetch.py                ← anti-bot fetch fallback
│   └── search_social.py               ← Chinese social-platform search
├── references/
│   ├── advisor_evaluation_framework.md  ← scoring rubrics
│   ├── chinese_academic_system.md       ← China-specific strategy
│   ├── international_academic_system.md ← Int'l-specific strategy
│   ├── publication_search_protocol.md   ← name-variant + broad-search rules
│   ├── report_template.md               ← JSON schema + 18-section structure
│   ├── lite_mode.md                     ← 6-phase Lite spec
│   └── web_rooter_integration.md        ← wr fallback details
└── examples/                          ← reference reports (HTML)
```
