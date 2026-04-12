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
  version: "1.3"
  license: MIT
---

# DeepTutor v5 — Academic Advisor Investigation System

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

## Model Capability Detection & Version Selection

DeepTutor has two investigation modes. The right mode depends on the model running it.

### Auto-Detection Rule

**Full Version (完整版)** — run without asking:
- Claude Opus 4.6+, Claude Sonnet 4.6+, Codex series, and future Claude models of equivalent or higher capability

**Prompt user to choose** — for all other models (GPT-4o, Gemini, GLM, MiniMax, Haiku, etc.), display:

> ⚠️ **DeepTutor 模式选择**
> 检测到当前模型非 Opus/Sonnet 4.6 级别。
> - **完整版**: 10阶段/11维度/18节报告（推荐高端模型）
> - **轻量版**: 6阶段/7维度/7节报告（Token约完整版40%，可能遗漏部分信息）
> 请选择：完整版 or 轻量版？

### Lite Version: 6-Phase Workflow

If the user chooses Lite, read `references/lite_mode.md` for the full specification. Key differences:
- **6 phases** (skip co-author network, funding analysis, macro trend deep dive, retirement risk)
- **7 scoring dimensions** (merge and drop 4 dimensions, re-weight)
- **Simplified Sharp Critique** (5-line template instead of 7-question framework)
- **7-section report** (instead of 18)

### Report Generation (Both Versions)

Both Full and Lite versions should output structured JSON and use `scripts/generate_report.py` for HTML rendering:

```bash
# Model outputs investigation data as JSON → script renders HTML
python scripts/generate_report.py report_data.json -o report.html
```

This separates investigation (model's job) from rendering (script's job). Even Full version benefits from this — the model focuses on analysis, not wrestling with CSS.

---

## 10-Phase Investigation Workflow (Full Version)

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

### Phase 6.5: Field Macro Trend Analysis (行业宏观趋势判断)

> **方向不对，再好的导师也帮不了你。**

在完成社会评价搜索后、打分之前，必须对导师所在研究领域进行宏观趋势判断。这不是简单的"hotspot or not"，而是系统性地评估这个领域对学生未来5-10年职业发展的影响。

**必须回答的5个核心问题：**

1. **生命周期定位**：这个领域处于什么阶段？
   - 🌱 萌芽期（Emerging）：新技术/新概念，论文少但增长快，风险高回报高
   - 📈 上升期（Growth）：资金涌入，招聘旺盛，竞争加剧但机会多
   - 📊 成熟期（Mature）：方法论稳定，工业化应用，增量创新为主
   - 📉 衰退期（Declining）：资金缩减，人才外流，被新技术替代
   - ☠️ 夕阳期（Sunset）：几乎无新资金，从业者转行，学生就业极难

2. **资金趋势**：近5年该领域的国家级基金（NSFC/NIH/ERC）资助数量和金额是增是减？有没有新的专项计划？

3. **就业市场前景**：
   - 学术界：该领域的faculty招聘岗位是否在增加？
   - 工业界：对口企业/岗位有哪些？薪资水平？招聘趋势？
   - 医疗/政府：是否有对口的临床或政策岗位？

4. **技术颠覆风险**：该领域是否面临被AI/新技术/新方法论替代的风险？（如：传统组学分析 vs AI驱动的组学，传统药物筛选 vs AI drug discovery）

5. **中国/国际差异**：同一个领域在国内和国际的发展阶段可能不同（如：某领域在国内是政策热点但国际已趋于饱和，或反之）

**信息来源：**
- 领域顶刊的发表量年度趋势（PubMed/Scopus统计）
- 国家基金资助项目数量趋势（NSFC/NIH Reporter）
- 行业报告和市场分析（招聘网站、行业白皮书）
- 领域顶级会议的参会规模变化
- 知名课题组的方向转移信号

**输出格式：**
给出明确的趋势判断标签（萌芽/上升/成熟/衰退/夕阳）+ 置信度 + 关键证据 + 对学生的具体影响。

### Phase 7: Multi-Dimensional Scoring

Read `references/advisor_evaluation_framework.md` for detailed rubrics.

**Chinese context — 11 dimensions:**

| # | Dimension | Weight |
|---|-----------|--------|
| 1 | Field Macro Trend (领域宏观趋势) | 10% |
| 2 | Publication Output & Quality (发表成果与质量) | 12% |
| 3 | Student Cultivation Track Record (学生培养实绩) | 13% |
| 4 | Platform & Resources (平台与资源) | 12% |
| 5 | Independence & Growth Space (独立性与成长空间) | 8% |
| 6 | Career Trajectory & Momentum (职业轨迹与势头) | 5% |
| 7 | PUA/Exploitation Risk (PUA/PUSH风险) | 10% |
| 8 | Time Freedom (时间自由度) | 8% |
| 9 | Goal-Advisor Match (毕业目标匹配) | 7% |
| 10 | Advisor Sharp Critique (导师锐评) | 10% |
| 11 | Retirement & Stability Risk (退休与稳定性风险) | 5% |

**International context — 11 dimensions:**

| # | Dimension | Weight |
|---|-----------|--------|
| 1 | Field Macro Trend | 10% |
| 2 | Publication Output & Quality | 12% |
| 3 | Student Outcome Track Record | 13% |
| 4 | Institution & Lab Resources | 12% |
| 5 | Mentorship & Independence Balance | 8% |
| 6 | Career Trajectory & Momentum | 5% |
| 7 | Toxicity / Exploitation Risk | 10% |
| 8 | Work-Life Balance & Flexibility | 8% |
| 9 | Goal-Advisor Match | 7% |
| 10 | Advisor Sharp Critique | 10% |
| 11 | Retirement & Stability Risk | 5% |

**New dimensions explained:**
- **Field Macro Trend (D1)**: Replaces old "Research Direction & Prospects" with a much deeper, structured macro trend analysis (see Phase 6.5). Not just "is it a hotspot" but WHERE in the lifecycle, WHAT the job market looks like, and WHETHER the field faces disruption.
- **Advisor Sharp Critique (D10)**: A synthesized, honest assessment that cuts through diplomatic scoring. See Phase 9.5 for details.
- **Retirement & Stability Risk (D11)**: Evaluates whether the advisor will still be active and funded for the full duration of the student's degree.

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

### Phase 9: Advisor Sharp Critique (导师锐评)

> **不要让外交辞令害了学生。学生需要的不是3.8分还是4.1分的区别，而是"这个人到底能不能选"的直觉判断。**

这个阶段是整个评估的灵魂。在完成所有数据收集和机械化打分后，用以下框架对导师进行一次不留情面的直觉评估。

**锐评必须回答的7个问题：**

1. **一句话判决**：如果你的亲弟弟/亲妹妹问你能不能选这个导师，你会说什么？（不是写给学术委员会的，是写给家人的）

2. **导师的"人设"vs现实**：
   - 导师对外展示的形象是什么？（官网简介、招生宣传、公开讲话）
   - 数据和学生评价反映的现实是什么？
   - 两者之间有多大差距？差距越大越危险。

3. **最大的隐藏风险**：导师不会主动告诉你、但你入组后一定会遇到的问题是什么？（基于学生评价、出组率、发表模式推断）

4. **最被低估的优点**：导师身上被分数系统低估的、真正有价值的特质是什么？

5. **5年后预测**：根据导师的年龄、职称、资金、发表趋势、领域走向——5年后这个实验室会是什么状态？上升、稳定、还是衰退？

6. **替代方案建议**：如果不选这个导师，在同一领域/同一学校，还有什么替代选择值得考虑？（基于合作者网络和同院系信息推断）

7. **Deal-Breaker检查**：是否存在以下任何一个"一票否决"条件？
   - 多条独立的PUA/toxicity投诉（不是一条可能是个人恩怨，多条就是系统性问题）
   - 导师3年内即将退休但没有明确的接班安排
   - 近3年完全无经费且无新论文
   - 多名学生中途退组/延期毕业的明确证据
   - 如果触发任何一条，无论其他维度分数多高，总评必须标注为"⚠️ 存在一票否决风险"

**锐评的评分标准：**

| Score | Criteria |
|-------|---------|
| 5 | 强烈推荐：数据和直觉都指向这是一个优秀的选择，几乎没有隐藏风险 |
| 4 | 推荐：整体良好，有小瑕疵但不影响大局，适合大多数学生 |
| 3 | 中性：有明显的优点也有明显的缺点，取决于学生个人情况和风险偏好 |
| 2 | 谨慎：存在显著风险信号，只推荐给特定类型的学生（如：极度自驱、不需要指导的） |
| 1 | 不推荐：多个红灯信号，或存在一票否决条件 |

**锐评的写作风格：**
- 说人话，不说学术套话
- 用具体事实支撑判断，不空谈
- 敢于给出明确的"推荐/不推荐"结论，不骑墙
- 如果信息不足无法判断，直说"信息不足，无法给出可靠的锐评"，不要硬编

### Phase 9.5: Retirement & Stability Risk Assessment

评估导师在学生就读期间是否会保持稳定。

**检查项：**
- 导师年龄/出生年份（推算退休时间）
- 是否临近退休年龄（中国：男60/女55，有延聘可能到65；国际：通常无强制退休但65+需关注）
- Tenure status（国际）：pre-tenure PI有被deny tenure导致实验室关闭的风险
- 经费连续性：当前经费何时到期？是否有续期迹象？
- 是否有实验室搬迁/跳槽迹象？（关注近期的职位变动、多个affiliation）
- 健康/精力信号：近年会议出席、论文产出是否有下降趋势

| Score | Criteria |
|-------|---------|
| 5 | 导师40-55岁，tenure/正教授，经费充足，至少10年稳定期 |
| 4 | 导师较年轻或中年，经费稳定，无退休/搬迁风险 |
| 3 | 有轻微风险信号（经费即将到期、pre-tenure），但总体可控 |
| 2 | 明显风险：导师55+岁无明确接班人，或pre-tenure且发表不够 |
| 1 | 高风险：导师即将退休、经费中断、或有跳槽/关闭实验室迹象 |

### Phase 10: Report Generation

Output all investigation data as structured JSON, then render via `scripts/generate_report.py`:

```bash
python scripts/generate_report.py report_data.json -o "教授名_机构.html"
```

The JSON schema and 18-section report structure are defined in `references/report_template.md`. Key rules: output language matches input, every claim cites a source, 锐评 must be in the top 3 sections.

---

## Parallel Search Strategy

Launch searches in parallel batches to maximize efficiency:
- **Batch 1**: Faculty page + Scholar profile + Lab website + Thesis DB
- **Batch 2**: PubMed broad (NO keywords) + Scopus/OpenAlex + Name variants + Preprints
- **Batch 3**: Social platforms + News + Funding DBs + Retraction Watch
- **Batch 4**: Cross-validate counts + Verify student outcomes + Fill gaps

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

When comparing multiple advisors: investigate each independently, generate individual reports, then add a comparison card with side-by-side scores, composite comparison, and trade-off analysis.

---

## Integration with Other Skills

Leverage these skills when available:
- `pubmed-database`, `openalex-database` — Publication searches
- `deep-research`, `exa-search` — Web research and social platform mining
- `biorxiv-database`, `arxiv-database` — Preprint searches
- `scientific-visualization`, `matplotlib` — Charts in report
- `literature-review` — Systematic publication analysis
- `citation-management` — Reference verification
- `scripts/robust_fetch.py` — Anti-bot web fetch with 3-layer fallback (derived from [Web-Rooter](https://github.com/pinkpixel-dev/web-rooter), MIT)
- `scripts/search_social.py` — Chinese social platform search (知乎/小红书/小木虫/贴吧/保研论坛/考研帮)

### Chinese Website Fallback (zero dependencies, details in `references/web_rooter_integration.md`)

```bash
python scripts/robust_fetch.py "<URL>"                                     # auto fallback
python scripts/robust_fetch.py "<URL>" --js                                # force browser
python scripts/search_social.py "导师名 大学名" --platforms zhihu,xiaohongshu,emuch  # social search
```

- **URL freshness**: if 404, re-search via `WebSearch("site:<domain> 教授姓名")`
- **If `wr` available**: prefer `wr html`/`wr social` (see `references/web_rooter_integration.md`)
