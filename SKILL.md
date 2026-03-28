---
name: deeptutor
description: >
  Comprehensive academic advisor investigation and evaluation system for graduate school decisions.
  Investigates professors at any institution worldwide — searches publications (PubMed/Scopus/Scholar/OpenAlex),
  maps co-author networks, tracks student trajectories (the #1 predictive signal), classifies advisor type,
  and assesses exploitation/toxicity risk. Automatically applies region-specific search strategies: Chinese
  institutions (mainland China) use 知乎/小木虫/百度学术/CNKI; international institutions use Reddit/RateMyProfessors/
  GradCafe/LinkedIn. Outputs a standalone .html report in the user's language — Chinese input produces Chinese
  report, English input produces English report, and so on for any language.

  Use this skill whenever evaluating a professor as a potential graduate advisor — including when users say
  "调查导师", "评估教授", "选导师", "导师怎么样", "能不能跟这个老师读研", "这个导师push吗",
  "investigate this advisor", "should I join this lab", "evaluate professor", "is this prof good",
  "rate my potential advisor", "review this PI", or provide a professor's name + institution for evaluation.
  Also triggers on comparative requests ("帮我对比这三个导师", "compare these advisors").
metadata:
  author: jiadizhu
  version: "1.0"
  license: MIT
---

# DeepTutor v4 — Academic Advisor Investigation System

## Core Principle

> **Your ceiling = your seniors' ceiling.**

Student outcomes are the single most predictive signal for advisor quality. A professor with stellar publications but whose students consistently end up in unclear positions is a red flag. A professor with modest metrics but whose students thrive is gold. Always weight student trajectory evidence above all other dimensions.

## Language & Region Detection

### Language Rule
Respond in whatever language the user writes in. If the user writes in Chinese, the entire report — titles, analysis, recommendations — must be in Chinese. If in English, everything in English. If in Japanese, Korean, or any other language, follow that language throughout. Never mix languages within a report unless quoting original source text.

### Region Detection
Determine region from the institution name. This affects which search platforms to use and which evaluation criteria apply.

| Region | Institutions | Strategy |
|--------|-------------|----------|
| **Mainland China** | Any university/institute in 中国大陆 | Chinese strategy → `references/chinese_academic_system.md` |
| **International** | US, EU, UK, Japan, Korea, Australia, Singapore, etc. | International strategy → `references/international_academic_system.md` |
| **Hong Kong / Macau / Taiwan** | HKU, CUHK, HKUST, NTU, NTHU, etc. | Hybrid — use both Chinese social platforms AND international academic platforms |

When uncertain about region, ask the user.

## Input Requirements

**Minimum input**: Professor name + institution name.

If the user hasn't provided these, ask:

1. **Career goal** (shapes the Goal-Advisor Match scoring dimension)
   - **Chinese context**: 读博深造 / 考公考编 / 进大厂 / 药企CRO / 进医院 / 纯拿学位
   - **International context**: Academic career (tenure-track) / Industry R&D / Consulting & Finance / Government & Policy / Startup / Just get degree
2. **Risk tolerance**: Conservative / Moderate / Aggressive
3. **Specific concerns** (optional): e.g., "I heard the lab has high turnover"

If the user doesn't provide career goal or risk tolerance, proceed with a balanced evaluation and note that the Goal-Match dimension couldn't be fully scored.

---

## 9-Phase Investigation Workflow

### Phase 1: Identity Resolution

Establish the professor's verified identity across platforms. This prevents investigating the wrong person (especially common with Chinese names that have many romanization variants).

**For all regions:**
- Official faculty page (university website)
- Google Scholar profile
- Scopus Author ID / ORCID
- Semantic Scholar

**Chinese-specific additions:**
- Baidu Scholar (百度学术)
- ResearchGate
- X-MOL faculty profile
- NSFC funded project database (kd.nsfc.cn)
- ScholarMate

**International-specific additions:**
- DBLP (for CS)
- Web of Science ResearcherID
- Personal/lab website
- GitHub (for computational fields)

**Key verification**: Cross-reference at least 3 platforms. Confirm institution, department, research area, and photo (if available) all align. For Chinese scholars, generate ALL name romanization variants — see `references/publication_search_protocol.md` for the template.

### Phase 2: Student Trajectory Tracking (THE MOST IMPORTANT PHASE)

This phase implements the "ceiling principle." Track as many current and former students as possible.

**How to find students:**
- Lab/group website "Members" or "Alumni" page
- Co-authored papers (students are typically first authors)
- University thesis/dissertation databases
- **Chinese**: CNKI/万方 thesis search, 小木虫 lab discussions
- **International**: LinkedIn (search "[professor name] lab" or "[university] [department]"), ProQuest Dissertations, university digital repositories

**What to track for each student:**
| Field | Description |
|-------|-------------|
| Name | Student's name |
| Period | Years in the lab (start–end) |
| Degree | Master's / PhD / Postdoc |
| First-author papers | Count and quality (journal tier) |
| Current position | Where they are now |
| Time to degree | Normal or extended? |

**Ceiling/Floor analysis:**
- **High ceiling**: Multiple students in tenure-track faculty, top-tier postdocs, or leadership roles in industry
- **Mid ceiling**: Students in decent positions but not exceptional
- **Low ceiling**: Students in unclear/untraceable positions, frequent attrition
- **Red flag**: Cannot find ANY student outcomes — either very new PI or students don't want to be associated

### Phase 3: Publication Analysis

Follow the protocol in `references/publication_search_protocol.md` EXACTLY. The mandatory rule: always start with a BROAD search (no field keywords), then narrow down.

**Search sequence:**
1. Broad PubMed/Scopus/Scholar search with name + institution (NO topic keywords)
2. Author ID-anchored search (Scopus ID, ORCID, Semantic Scholar)
3. All name variants from the romanization template
4. Cross-database verification (minimum 3 databases)

**Analyze:**
- Total output, h-index, i10-index
- Publication trend (increasing/stable/declining)
- Journal quality distribution (top-tier / mid-tier / low-tier)
- Student first-authorship ratio
- Publication gaps (use the 6-step verification checklist before concluding any gap)
- Preprint activity (bioRxiv, arXiv, medRxiv)

### Phase 4: Co-Author Network & Advisor Classification

Build a co-author frequency table from the publication record. Classify relationships:
- Internal collaborators (same institution)
- External academic collaborators
- Clinical/industry collaborators
- Student/postdoc co-authors

**Advisor Type Classification:**

| Type | Chinese Label | Description | Key Signal |
|------|--------------|-------------|------------|
| Research-Focused | 学术型 | Deep academic focus, pushes for top publications | Students publish well but may face high pressure |
| Grant/Project-Driven | 项目型 | Funded by applied/industry projects | Students may do project work instead of thesis research |
| Semi-Independent | 半放养型 | Gives moderate guidance, allows flexibility | Good for self-motivated students |
| Mentorship-Heavy | 指导型 | Hands-on guidance, frequent meetings | Great for students needing structure |
| Hands-Off | 纯放养型 | Minimal guidance, students largely on their own | Good if you have clear goals; risky otherwise |

Classify based on: meeting frequency, student authorship patterns, project types (basic vs applied), student independence signals.

### Phase 5: Funding Analysis

**Chinese institutions** → Read `references/chinese_academic_system.md`:
- NSFC grants (青年/面上/重点/杰青/优青)
- Ministry-level programs (973, National Key R&D)
- Provincial and university internal grants
- Industry/hospital collaboration (横向) funding

**International institutions** → Read `references/international_academic_system.md`:
- Government grants (NIH R01/R21, NSF CAREER, ERC Starting/Consolidator/Advanced, EPSRC, DFG, JSPS)
- Foundation grants (HHMI, Wellcome Trust, Gates Foundation)
- Industry funding and consulting
- Startup funds (common for new faculty)

**Assess:**
- Continuous vs sporadic funding
- Funding trajectory (growing or shrinking)
- Diversity of funding sources
- Whether funding supports student stipends and research

### Phase 6: Contextual Intelligence — Social & Reputation Search

This phase uses region-specific platforms to gather student reviews and lab culture signals.

#### Chinese Mainland Strategy

Search these platforms for: `"导师名" + 评价/怎么样/读研/课题组/实验室/push/pua`

| Platform | URL Pattern | What to Find |
|----------|-------------|-------------|
| 知乎 | zhihu.com | Lab culture, student experiences, detailed reviews |
| 小木虫 | emuch.net | Grad student discussions, lab reputation |
| 保研论坛 | baoyan.net | Recommendation letters, interview experiences |
| 小红书 | xiaohongshu.com | Recent student experiences (newer platform) |
| 百度贴吧 | tieba.baidu.com | University-specific discussions |
| 考研帮 | kaoyan.com | Exam and advisor selection discussions |

Also search: university BBS, WeChat public accounts (if accessible), news articles about the professor.

#### International Strategy

Search these platforms for: `"professor name" + "university" + review/advisor/lab/experience/toxic`

| Platform | URL Pattern | What to Find |
|----------|-------------|-------------|
| Reddit | r/GradSchool, r/AskAcademia, r/PhD, field-specific subs | Lab culture, warnings, experiences |
| RateMyProfessors | ratemyprofessors.com | Teaching quality (proxy for mentoring style) |
| GradCafe | thegradcafe.com | Admission discussions, lab reputation |
| Glassdoor | glassdoor.com | For industry-adjacent labs, postdoc reviews |
| Twitter/X | x.com | Academic community discussions, controversies |
| LinkedIn | linkedin.com | Student trajectory, lab alumni network |
| Quora | quora.com | Occasional advisor reviews |

Also search: department-specific student surveys (some universities publish these), news articles, academic misconduct databases (Retraction Watch).

#### Hong Kong / Macau / Taiwan Strategy
Combine BOTH Chinese and international platforms, plus:
- PTT (Taiwan: ptt.cc)
- LIHKG (Hong Kong: lihkg.com)
- Dcard (Taiwan/HK student platform)
- 小红书 and 知乎 (many HK/TW students post here)

### Phase 7: Multi-Dimensional Scoring

Read `references/advisor_evaluation_framework.md` for detailed rubrics.

**Chinese context — 9 dimensions:**

| # | Dimension | Weight |
|---|-----------|--------|
| 1 | Research Direction & Prospects (研究方向与前景) | 10% |
| 2 | Publication Output & Quality (发表成果与质量) | 15% |
| 3 | Student Cultivation Track Record (学生培养实绩) | 15% |
| 4 | Platform & Resources (平台与资源) | 15% |
| 5 | Independence & Growth Space (独立性与成长空间) | 10% |
| 6 | Career Trajectory & Momentum (职业轨迹与势头) | 5% |
| 7 | PUA/Exploitation Risk (PUA/PUSH风险) | 10% |
| 8 | Time Freedom (时间自由度) | 10% |
| 9 | Goal-Advisor Match (毕业目标匹配) | 10% |

**International context — 9 dimensions:**

| # | Dimension | Weight |
|---|-----------|--------|
| 1 | Research Direction & Prospects | 10% |
| 2 | Publication Output & Quality | 15% |
| 3 | Student Outcome Track Record | 15% |
| 4 | Institution & Lab Resources | 15% |
| 5 | Mentorship & Independence Balance | 10% |
| 6 | Career Trajectory & Momentum | 5% |
| 7 | Toxicity / Exploitation Risk | 10% |
| 8 | Work-Life Balance & Flexibility | 10% |
| 9 | Goal-Advisor Match | 10% |

Key difference: The Chinese "时间自由度" dimension evaluates freedom for 考公/考编/实习, which is irrelevant for international students. The international "Work-Life Balance" evaluates vacation policy, expected work hours, remote flexibility, and support for career development activities (conferences, internships, courses).

### Phase 8: Red / Green Flag Check

Run through the flag checklists in `references/advisor_evaluation_framework.md`. Region-specific flags:

**Universal red flags:**
- No traceable student outcomes
- Extended time-to-degree pattern
- Students leaving mid-program
- No papers in 2+ years
- Funding gaps > 3 years
- Multiple PUA/toxicity reports online
- Retracted papers

**Chinese-specific red flags:**
- 横向 projects with no student benefit
- Only 硕导 but recruiting PhD-track students
- Excessive graduation requirements beyond norms
- No internship permission despite students wanting industry careers

**International-specific red flags:**
- High postdoc churn rate
- Lab members rarely listed as first/corresponding author
- No conference travel support
- Visa sponsorship issues for international students
- Advisor takes credit for student work (scooping)
- "Revolving door" lab (many short-tenure members)
- Glassdoor/Reddit reports of toxic culture

**Universal green flags:**
- Multiple student first-author papers in good journals
- Clear, positive student outcomes
- Recent promotion or awards
- Conference support for students
- Reasonable stipends
- Positive online reviews from current/former students

### Phase 9: Report Generation

Generate a standalone HTML report following `references/report_template.md`.

**Critical rules:**
- Output language matches user's input language — NO exceptions
- Single .html file, all CSS inline, no external dependencies
- Every claim must cite a source (URL, database, platform)
- Distinguish fact from inference (use "据观察/Based on available evidence" for inferences)
- Include composite score prominently
- All URLs must be clickable
- Must be printable (hide nav in @media print)
- Footer: "Generated by DeepTutor v4 — Powered by Claude"

---

## Parallel Search Strategy

To maximize efficiency, launch searches in parallel batches:

**Batch 1 — Identity + Students:**
- Faculty page scrape
- Google Scholar profile
- Lab website (members/alumni)
- Thesis database search

**Batch 2 — Publications (BROAD first):**
- PubMed broad search (name + institution, NO keywords)
- Scopus/OpenAlex author search
- Name variant searches
- Preprint server search

**Batch 3 — Context + Funding:**
- Social platform searches (region-specific)
- News article search
- Funding database queries
- Retraction Watch check

**Batch 4 — Verification:**
- Cross-validate publication counts across databases
- Verify student outcomes via LinkedIn/CNKI
- Confirm funding status
- Fill any gaps from Batches 1-3

---

## Quality Rules

1. **Every claim needs a source.** No unsourced assertions.
2. **Distinguish fact from inference.** Mark speculative conclusions explicitly.
3. **Cross-validate metrics.** Use ≥3 databases for publication counts.
4. **Weight recent evidence.** Last 5 years matter more than career totals.
5. **No fabrication.** If information is unavailable, say so — don't guess.
6. **Be balanced.** Report both strengths and weaknesses.
7. **Score vs peers.** Compare against others at the same institution and rank.
8. **Student signals > publication metrics.** Always.
9. **PUA/toxicity evidence is critical.** Don't downplay concerning signals.
10. **Publication gap verification.** Complete the 6-step checklist before concluding any gap.

---

## Comparative Mode

When the user asks to compare multiple advisors:
1. Investigate each advisor independently using the full 9-phase workflow
2. Generate individual reports for each
3. Add a comparison section at the end with:
   - Side-by-side scoring table (all dimensions)
   - Composite score comparison
   - Specific recommendation based on user's career goal
   - Trade-off analysis ("Advisor A is better for X, but Advisor B offers Y")

---

## Integration with Other Skills

Leverage these skills when available:
- `pubmed-database`, `openalex-database` — Publication searches
- `deep-research`, `exa-search` — Web research and social platform mining
- `biorxiv-database`, `arxiv-database` — Preprint searches
- `scientific-visualization`, `matplotlib` — Charts in report
- `literature-review` — Systematic publication analysis
- `citation-management` — Reference verification
