# Advisor Evaluation Framework

Detailed scoring rubric for each dimension of the DeepTutor evaluation.
Supports both Chinese (国内) and International evaluation contexts.

---

## Scoring Framework (Chinese Context)

### Dimension 1: 领域宏观趋势 Field Macro Trend (10%)

> **方向不对，再好的导师也帮不了你。这个维度评估的不是导师个人，而是导师所在赛道的未来。**

#### 生命周期定位矩阵

| 阶段 | 标识 | 发表量趋势 | 资金趋势 | 就业前景 | 对学生的意义 |
|------|------|-----------|---------|---------|------------|
| 萌芽期 | 🌱 | 少但年增>30% | 开始出现专项 | 不确定，高风险高回报 | 适合赌性大的学生，可能成为领域先驱 |
| 上升期 | 📈 | 快速增长 | 大量涌入 | 供不应求 | **最佳入场时机**，竞争在加剧但机会更多 |
| 成熟期 | 📊 | 稳定 | 稳定或微降 | 充足但竞争激烈 | 安全选择，但难以做出突破性成果 |
| 衰退期 | 📉 | 下降 | 明显缩减 | 岗位减少 | 谨慎选择，考虑转方向的灵活性 |
| 夕阳期 | ☠️ | 大幅下降 | 几乎无新资金 | 极度困难 | **强烈不推荐**，除非有明确的转行计划 |

#### 就业市场前景评估

| 方向 | 评估内容 |
|------|---------|
| 学术界 | 近3年该领域faculty招聘数量趋势；国内vs国际的差异 |
| 工业界 | 对口企业/岗位清单；薪资范围；招聘趋势（增/减/稳） |
| 医疗/政府 | 对口的临床/政策岗位；体制内招聘趋势 |
| 转行灵活性 | 该领域训练出的技能是否可迁移到其他领域？ |

#### 技术颠覆风险评估

| 风险等级 | 描述 | 举例 |
|---------|------|------|
| 高 | 核心方法论正在被AI/新技术替代 | 传统统计遗传学 → AI基因组学 |
| 中 | 部分工具链在更新，但核心逻辑不变 | 传统测序分析 → 长读长+AI辅助 |
| 低 | 方法论稳定，AI是辅助而非替代 | 临床试验、动物模型 |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | 上升期领域；资金充裕且持续增长；就业供不应求；低技术颠覆风险；中国和国际前景均好 |
| 4 | 上升期或成熟初期；资金稳定；就业前景良好；可能有轻微的技术更新压力 |
| 3 | 成熟期；资金和就业稳定但增量有限；竞争激烈；需要差异化定位 |
| 2 | 衰退期或严重内卷的成熟期；资金缩减；就业岗位减少；高技术颠覆风险 |
| 1 | 夕阳期；几乎无新资金；从业者大量转行；被新技术全面替代 |

### Dimension 2: 发表成果与质量 Publication Output & Quality (15%)

#### Benchmarks by Career Stage (Biomedical Sciences, China)

| Rank | Expected H-index | Expected Papers | Top Journal Count |
|------|------------------|-----------------|-------------------|
| Lecturer/Assistant Prof | 3-8 | 5-15 | 0-2 |
| Associate Professor | 8-15 | 15-40 | 2-5 |
| Full Professor | 15-30 | 40-80 | 5-15 |
| Distinguished Prof (杰青/长江) | 25-50+ | 60-150+ | 10-30+ |

#### Journal Tier Classification (Biomedical)

| Tier | Examples | IF Range |
|------|---------|----------|
| CNS | Nature, Science, Cell | 30+ |
| Top specialty | Immunity, Cancer Cell, Hepatology, J Clin Invest | 15-30 |
| High | Cell Mol Immunol, J Virol, PNAS | 8-15 |
| Good | Eur J Immunol, Front Immunol, J Immunol | 4-8 |
| Standard | J Interf Cytok Res, Biochem Biophys Res Commun | 2-4 |

#### Publication Gap Detection (关键检查项)

| Gap Pattern | Interpretation | Severity |
|-------------|---------------|----------|
| 无gap，持续产出 | 正常，稳定产出 | 无风险 |
| 1年gap | 可能在转方向或申请大项目 | 低风险 |
| 2年gap | 需要调查原因（行政？经费？转型？） | 中风险 |
| 3年以上gap | 可能已不做科研或面临严重困难 | 高风险/红灯 |
| 最近2年无新论文 | **必须在报告中标注为红灯信号** | 红灯 |
| 学生一作论文gap 2年以上 | 学生无法产出，培养能力存疑 | 红灯 |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | H-index top 10% for rank; multiple CNS/top specialty papers; accelerating output; no gaps |
| 4 | H-index above average; several high-IF papers; stable or growing output |
| 3 | H-index at average; mix of good and standard journals; stable output |
| 2 | H-index below average; mostly standard journals; declining or stagnant; gaps present |
| 1 | Very low output; no high-IF papers; long publication gaps; recent gap > 2 years |

### Dimension 3: 学生培养实绩 Student Cultivation Track Record (15%)

> **核心法则：你的天花板 = 你师兄姐的天花板**

#### Key Indicators

| Indicator | Strong Signal | Weak Signal | Red Flag |
|-----------|--------------|-------------|----------|
| Graduate placement | Faculty positions, top-tier postdocs | Unknown/untraceable | All untraceable |
| Time to degree | 4-5 years (PhD) | 7+ years | Multiple students overtime |
| Student first-author papers | 2+ per PhD student | 0-1 | No student papers in 2+ years |
| Student awards | Thesis awards, fellowships | None found | - |
| Lab alumni network | Active, supportive community | No evidence | Evidence of conflict |
| Post-graduation success | Students go to better or equal institutions | Downward trajectory | Consistently poor outcomes |

#### Ceiling Principle Assessment (天花板法则)

| Outcome Pattern | Interpretation |
|----------------|---------------|
| 师兄姐去了好学校/好企业 | 你有机会达到同等水平或更高 |
| 师兄姐去向一般 | 你的预期上限就是这个水平 |
| 师兄姐去向不明/失联 | **红灯: 极有可能去向不好，不愿公开** |
| 无可追踪的毕业生 | **红灯: 可能带学生经验不足或学生未正常毕业** |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Multiple alumni in faculty/top postdoc positions; students publish in top journals; ceiling is high |
| 4 | Most students graduate on time with good papers; several known successful outcomes |
| 3 | Students graduate and find employment; average publication record |
| 2 | Few traceable outcomes; some signs of delayed graduation; student papers rare |
| 1 | Evidence of student attrition; very few graduates; no traceable outcomes; ceiling unknown |

### Dimension 4: 平台与资源 Platform & Resources (15%)

#### University Tier (China)

| Tier | Examples |
|------|---------|
| Top 5 | Peking, Tsinghua, Fudan, SJTU, Zhejiang |
| C9 League | + Nanjing, USTC, Harbin IT, Xi'an Jiaotong |
| 985 Project | + Wuhan, Sun Yat-sen, Sichuan, etc. |
| 211 Project | Broader set of key universities |
| Other | Provincial universities, medical colleges |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Top-5 university; state key lab; hospital/clinical partnerships; international collaborations |
| 4 | C9/985 university; well-equipped department; some clinical connections |
| 3 | 211 university or strong department at lesser institution; adequate facilities |
| 2 | Average university; limited equipment; isolated research group |
| 1 | Unknown institution; no visible resources or collaborations |

### Dimension 5: 独立性与成长空间 Independence & Growth Space (10%)

#### Lab Size Considerations

| Lab Size | Pros | Cons |
|----------|------|------|
| Small (1-3 students) | High advisor attention; close mentorship | Limited peer support; narrow perspective |
| Medium (4-8 students) | Balanced attention; good peer learning | Competition for resources |
| Large (10+ students) | Broad network; resource-rich | Risk of "advisor abandonment"; assembly-line mentoring |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Optimal lab size; advisor is accessible; students have intellectual freedom; clear career support |
| 4 | Good balance; students can develop independence while getting guidance |
| 3 | Average; some constraints but workable |
| 2 | Too large (neglect) or too constrained (micromanagement); limited autonomy |
| 1 | Evidence of problematic dynamics; advisor inaccessible; no student agency |

### Dimension 6: 职业轨迹与势头 Career Trajectory & Momentum (5%)

#### Promotion Timeline Benchmarks (China)

| Transition | Fast | Normal | Slow |
|------------|------|--------|------|
| PhD -> Lecturer | 0 years (留校) | 1-2 years | 3+ years |
| Lecturer -> Associate Prof | 3-5 years | 5-8 years | 8+ years |
| Associate Prof -> Full Prof | 5-8 years | 8-12 years | 12+ years |
| To 杰青/优青 | Within 5 years of eligibility | Varies | Never obtained |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Rapid promotion; major talent titles; rising star trajectory |
| 4 | On-track promotion; recent achievements; positive momentum |
| 3 | Normal progression; stable but not exceptional |
| 2 | Slow promotion; stagnant period; limited recent achievements |
| 1 | Career plateau; no advancement in 10+ years; declining metrics |

### Dimension 7: PUA/PUSH风险 (10%)

> **此维度评估实验室安全性，与学术水平同等重要。**

#### Assessment Signals

| Signal | Source | Severity |
|--------|--------|----------|
| 学生在知乎/小木虫投诉 | Forum search | High |
| 多名学生中途退出/转导师 | Publication patterns, forums | High |
| 导师要求做与学位无关的横向项目 | Publication analysis, forums | Medium-High |
| 学生毕业时间普遍超时 | Thesis databases, publication gaps | Medium |
| 无学生能外出实习 | Forums, student contacts | Medium |
| 毕业要求远超学校最低标准 | Comparison with dept requirements | Medium |
| 组会频率异常高（每日汇报） | Forums, student contacts | Medium |
| 导师社交媒体/公开场合有不当言论 | Web search | Medium |
| 无任何负面信息 | - | Neutral (absence ≠ evidence) |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | No red flags; students report positive experience; reasonable expectations; healthy lab culture |
| 4 | Minor concerns but no evidence of systemic issues; generally positive reputation |
| 3 | Some ambiguous signals; no clear evidence either way; data insufficient |
| 2 | Warning signs: students leave, complaints found, excessive workload, 横向剥削 |
| 1 | Clear evidence of PUA/PUSH: multiple student complaints, unreasonable demands, exploitation, toxicity |

### Dimension 8: 时间自由度 (10%)

> **对于考公/进大厂/需要实习的学生，此维度可能是最重要的。**

#### Assessment Signals

| Signal | Interpretation |
|--------|---------------|
| 学生在简历上有实习经历 | 导师允许实习 |
| 学生仅在毕业后才有非学术经历 | 在读期间可能不允许实习 |
| 学生参加学术会议记录 | 有会议资助 |
| 组会频率/考勤制度 | 影响可支配时间 |
| 横向项目时间占比 | 挤压学生自由时间 |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Students freely intern, attend conferences, prepare for jobs; flexible schedule |
| 4 | Internship allowed in final year; reasonable schedule; some flexibility |
| 3 | Group meetings regular but some personal time; internship status unclear |
| 2 | Tight schedule; internship discouraged; frequent mandatory activities |
| 1 | 996/007 workload; no internship allowed; no personal time; excessive oversight |

### Dimension 9: 毕业目标匹配 (10%)

> **不同导师适合不同目标的学生。此维度必须根据用户声明的目标来评分。**

#### Goal-Advisor Type Match Matrix (毕业目标匹配矩阵)

| 毕业目标 | 最佳导师类型 | 可接受 | 最差选择 | 关键需求 |
|----------|------------|--------|---------|---------|
| **读博深造** | 学术型、指导型 | 半放养型 | 纯放养型、项目型 | 高水平产出、学术人脉 |
| **考公/考编** | 纯放养型 | 半放养型 | 学术型(996) | 充足的自由时间复习 |
| **进大厂** | 半放养型(允许实习) | 指导型 | 项目型(占时间) | 实习自由、技能积累 |
| **药企/CRO** | 有临床/企业合作 | 学术型 | 纯基础无转化 | 行业人脉、转化经验 |
| **进医院** | 有临床资源 | 半放养型 | 纯基础研究 | 临床合作、MD资源 |
| **纯拿学位** | 纯放养型 | 半放养型 | 学术型(高要求) | 低门槛毕业、无压力 |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Advisor type perfectly matches user's goal; all key needs met |
| 4 | Good match; most key needs met; minor misalignment |
| 3 | Neutral; could work but not ideal for the specific goal |
| 2 | Poor match; user's goal will be harder to achieve with this advisor |
| 1 | Worst possible match; this advisor type actively hinders user's goal |

---

## Scoring Framework (International Context)

### Dimension 1: Research Direction & Prospects (10%)

#### Scoring Criteria

| Score | Criteria |
|-------|---------|
| 5 | Field is a current hotspot with strong funding (NIH, NSF, ERC); high translational potential; broad career relevance across academia, industry, and government |
| 4 | Active research area with stable funding; good career prospects in multiple sectors |
| 3 | Established field with moderate competition; adequate funding opportunities |
| 2 | Niche or declining field; limited funding; narrow career applicability |
| 1 | Obsolete methodology; no foreseeable funding; extremely limited career paths |

#### Assessment Checklist
- Is the field growing, stable, or shrinking? (Check publication volume trends, NIH/NSF funding trends)
- Are there major funding programs targeting this area (NIH R01, NSF CAREER, ERC, Wellcome Trust)?
- What industry sectors hire in this area (pharma, biotech, tech, finance, consulting)?
- Does the research lend itself to industry collaboration or startup opportunities?
- Is the PI opening new subfields or stuck in one narrow topic?

### Dimension 2: Publication Output & Quality (15%)

#### Benchmarks by Career Stage (International, Biomedical Sciences)

| Rank | Expected H-index | Expected Papers | Top Journal Count |
|------|------------------|-----------------|-------------------|
| Assistant Professor | 5-12 | 10-25 | 1-4 |
| Associate Professor | 12-25 | 25-60 | 4-10 |
| Full Professor | 25-45 | 60-120 | 10-25 |
| Endowed Chair / HHMI | 40-80+ | 100-250+ | 20-50+ |

#### Journal Tier Classification (International Biomedical)

| Tier | Examples | IF Range |
|------|---------|----------|
| CNS | Nature, Science, Cell | 30+ |
| Top specialty | NEJM, Lancet, Immunity, Cancer Cell, J Clin Invest | 15-30 |
| High | PNAS, eLife, Nature Communications, Genome Research | 8-15 |
| Good | PLoS Genetics, Nucleic Acids Research, BMC Biology | 4-8 |
| Standard | PLoS ONE, BMC Genomics, Scientific Reports | 2-4 |

#### Publication Gap Detection

| Gap Pattern | Interpretation | Severity |
|-------------|---------------|----------|
| No gap, continuous output | Normal, stable productivity | No risk |
| 1-year gap | May be transitioning fields or on sabbatical | Low risk |
| 2-year gap | Investigate cause (admin role? funding lapse? health?) | Medium risk |
| 3+ year gap | May have stopped active research or facing serious difficulties | High risk |
| No new papers in last 2 years | **Must flag as red signal in report** | Red flag |
| No student first-author papers in 2+ years | Student output capability in question | Red flag |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | H-index top 10% for rank; multiple CNS/top specialty papers; accelerating output; no gaps |
| 4 | H-index above average; several high-IF papers; stable or growing output |
| 3 | H-index at average; mix of good and standard journals; stable output |
| 2 | H-index below average; mostly standard journals; declining or stagnant; gaps present |
| 1 | Very low output; no high-IF papers; long publication gaps; recent gap > 2 years |

### Dimension 3: Student Outcome Track Record (15%)

> **Core principle: Your ceiling = your senior lab members' ceiling. Track alumni on LinkedIn.**

#### Key Indicators

| Indicator | Strong Signal | Weak Signal | Red Flag |
|-----------|--------------|-------------|----------|
| Graduate placement | Faculty positions at R1 universities, top industry labs (Google, Meta, Genentech) | Unknown/untraceable | All untraceable or downward trajectory |
| Time to degree | 4-6 years (PhD, field-dependent) | 7+ years | Multiple students overtime |
| Student first-author papers | 2+ per PhD student in good journals | 0-1 | No student papers in 2+ years |
| Student awards | NSF GRFP, NIH F31, best paper awards | None found | - |
| LinkedIn alumni outcomes | Clear career progression, positive about lab | Sparse profiles | Negative comments, career stagnation |
| Lab alumni network | Active Slack/Discord, alumni help with jobs | No evidence | Evidence of conflict or estrangement |

#### Alumni Outcome Assessment

| Outcome Pattern | Interpretation |
|----------------|---------------|
| Alumni hold faculty positions at R1/R2 universities | High ceiling; advisor trains future PIs |
| Alumni at top industry labs (FAANG, big pharma R&D) | Strong industry pipeline; good recommendation letters |
| Alumni outcomes mixed but traceable | Normal variation; assess whether pattern matches your goal |
| Alumni untraceable on LinkedIn/Google Scholar | **Red flag: likely poor outcomes or very new lab** |
| Multiple students left the lab without finishing | **Red flag: potential toxicity or impossible expectations** |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Multiple alumni in faculty/top industry positions; students publish in top journals; clear LinkedIn success stories |
| 4 | Most students graduate on time with good papers; several known successful outcomes |
| 3 | Students graduate and find employment; average publication record |
| 2 | Few traceable outcomes; some signs of delayed graduation; student papers rare |
| 1 | Evidence of student attrition; very few graduates; no traceable outcomes; ceiling unknown |

### Dimension 4: Institution & Lab Resources (15%)

#### University Tier (International)

| Tier | Examples |
|------|---------|
| Top 10 Global | MIT, Stanford, Harvard, Oxford, Cambridge, Caltech, etc. |
| Top 50 Global / R1 Elite | UC Berkeley, ETH Zurich, Johns Hopkins, U Toronto, etc. |
| R1 Research Universities | Most major state flagships, well-known private universities |
| R2 / Regional Universities | Smaller research universities with select strong departments |
| Teaching-focused / Unranked | Limited research infrastructure |

#### Resource Assessment

| Resource | Strong | Adequate | Weak |
|----------|--------|----------|------|
| Computing | Dedicated HPC cluster, cloud credits, GPU nodes | Shared departmental cluster | No dedicated computing |
| Equipment | Core facilities, latest instruments | Shared equipment with reasonable access | Outdated or no access |
| Funding | Multiple active R01/NSF grants, industry funding | One active grant | No current funding |
| Collaborations | International network, clinical partnerships | Some departmental collaborations | Isolated lab |
| Staff | Lab manager, research scientists, postdocs | Some support staff | PI and students only |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Top-10 global university; dedicated core facilities; strong computing; multiple active grants; international collaborations |
| 4 | Top-50 / R1 university; well-equipped department; active grants; some industry connections |
| 3 | R1 university or strong department at R2; adequate facilities; at least one active grant |
| 2 | Limited resources; outdated equipment; funding uncertain; isolated research group |
| 1 | No visible resources or collaborations; no active grants; teaching-focused institution |

### Dimension 5: Mentorship & Independence Balance (10%)

#### Mentorship Style Indicators

| Indicator | Mentorship-Heavy | Balanced | Hands-Off |
|-----------|-----------------|----------|-----------|
| Meeting frequency | Weekly 1-on-1 + group meeting | Biweekly 1-on-1, weekly group | Monthly or ad hoc |
| Writing feedback | Line-by-line edits on drafts | Structural feedback, student revises | Minimal feedback |
| Career guidance | Active job market mentoring, mock interviews | Some career advice | Student is on their own |
| Project ownership | PI defines and guides project | Collaborative direction-setting | Student defines own project |
| Conference travel | Regularly sends students to conferences | Occasional conference support | Students fund their own travel |

#### Lab Size Considerations

| Lab Size | Pros | Cons |
|----------|------|------|
| Small (1-3 students) | High advisor attention; close mentorship | Limited peer support; narrow perspective |
| Medium (4-8 students) | Balanced attention; good peer learning; senior students mentor juniors | Competition for advisor time |
| Large (10+ students) | Broad network; resource-rich; more collaboration opportunities | Risk of neglect; assembly-line mentoring |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Optimal lab size; regular meetings with meaningful feedback; clear career guidance; students develop independence with support |
| 4 | Good balance; students can develop independence while getting constructive guidance |
| 3 | Average; some constraints but workable mentorship relationship |
| 2 | Too large (neglect) or too constrained (micromanagement); limited constructive feedback |
| 1 | Evidence of problematic dynamics; advisor inaccessible or controlling; no career support |

### Dimension 6: Career Trajectory & Momentum (5%)

#### Career Stage Assessment (International)

| Indicator | Strong Signal | Neutral | Weak Signal |
|-----------|--------------|---------|-------------|
| Tenure status | Tenured (stable lab) | Tenure-track (motivated but risky) | Non-tenure-track / adjunct |
| Recent awards | NSF CAREER, NIH Director's Award, HHMI, Sloan | Standard grants | No recent awards |
| Promotions | Recently promoted | On-track timeline | Stalled at rank for 10+ years |
| Editorial boards | Top journal editor | Specialty journal reviewer | No editorial roles |
| Invited talks | Keynote at major conferences | Regular conference presentations | No recent talks |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Tenured; major awards (HHMI, NAS member); rising star or established leader; strong recent momentum |
| 4 | Tenure-track with strong trajectory; recent promotion or major grant; positive momentum |
| 3 | Normal progression; stable but not exceptional; adequate funding |
| 2 | Stalled promotion; limited recent achievements; funding concerns |
| 1 | Career plateau; no advancement in 10+ years; declining metrics; at risk of losing lab |

### Dimension 7: Toxicity / Exploitation Risk (10%)

> **This dimension assesses lab safety and is as important as academic quality.**

#### Assessment Signals (International Sources)

| Signal | Source | Severity |
|--------|--------|----------|
| Student complaints on Reddit (r/GradSchool, r/AskAcademia) | Reddit search | High |
| Negative Glassdoor reviews for the lab/department | Glassdoor search | High |
| Retracted papers or misconduct allegations | Retraction Watch, PubPeer | High |
| Multiple students/postdocs leaving within 1 year | Publication patterns, LinkedIn | High |
| PI scoops student work (publishes without student credit) | Publication analysis, forums | High |
| Students never listed as first author | Publication analysis | Medium-High |
| Excessive work hour expectations (80+ hours/week) | Reddit, Glassdoor, word of mouth | Medium |
| No conference travel support | Student CVs, lab website | Medium |
| Lab members rarely acknowledged properly | Paper acknowledgments | Medium |
| PI has known visa manipulation tactics | Immigration forums, word of mouth | Medium |
| No information found | - | Neutral (absence ≠ evidence) |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | No red flags; students report positive experience; reasonable expectations; healthy lab culture |
| 4 | Minor concerns but no evidence of systemic issues; generally positive reputation |
| 3 | Some ambiguous signals; no clear evidence either way; data insufficient |
| 2 | Warning signs: students leave, complaints found, excessive workload, exploitation patterns |
| 1 | Clear evidence of toxicity: multiple complaints, retractions, scooping, exploitation, visa manipulation |

### Dimension 8: Work-Life Balance & Flexibility (10%)

> **Critical for students who value sustainable productivity and long-term career health.**

#### Assessment Signals

| Signal | Interpretation |
|--------|---------------|
| Students have internship experience on LinkedIn/CV | PI allows industry engagement during PhD |
| Conference travel records | PI funds and supports conference attendance |
| Lab has clear vacation policy | Healthy work-life boundary expectations |
| Students publish on weekdays only (commit timestamps) | Reasonable work hours |
| PI supports remote work / flexible schedule | Modern, trust-based management |
| Students mention mental health support | Lab culture prioritizes wellbeing |
| Lab social events, retreats | Positive community culture |
| Students working weekends/holidays (social media, Slack timestamps) | Potential overwork culture |

#### Key Factors

| Factor | Healthy | Concerning | Red Flag |
|--------|---------|------------|----------|
| Expected work hours | 40-50 hrs/week | 50-60 hrs/week | 70-80+ hrs/week |
| Vacation | 2-4 weeks/year, no guilt | Technically allowed, implicitly discouraged | No vacation or shamed for taking time off |
| Remote work | Flexible, trust-based | Some flexibility | Must be in lab 6-7 days/week |
| Conference travel | Funded, encouraged | Occasionally supported | Never funded or discouraged |
| Internships | Allowed and supported | Allowed in final year only | Explicitly forbidden |
| Mental health | PI proactively supportive | Neutral | Dismissive or hostile |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Reasonable hours; vacation supported; remote flexibility; conference travel funded; internships allowed; positive lab culture |
| 4 | Generally good balance; some flexibility; conference travel mostly funded; internship possible |
| 3 | Average; standard expectations; internship status unclear; some flexibility |
| 2 | Long hours expected; internship discouraged; limited conference support; rigid schedule |
| 1 | 80+ hour weeks; no vacation; no internships; no conference travel; toxic overwork culture |

### Dimension 9: Goal-Advisor Match (10%)

> **Different advisors suit different career goals. This dimension must be scored based on the user's stated goal.**

#### International Career Goals

| Career Goal | Description |
|-------------|-------------|
| **Academic (tenure-track)** | Aim for faculty position at research university; need strong publication record and teaching experience |
| **Industry R&D** | Research roles at pharma, biotech, tech companies; need practical skills and internship experience |
| **Consulting / Finance** | McKinsey, BCG, quant finance; need analytical skills and time for recruiting prep |
| **Government / Policy** | NIH, FDA, WHO, science policy; need broad knowledge and professional network |
| **Startup** | Launch own company or join early-stage; need independence, IP knowledge, entrepreneurial skills |
| **Just degree** | Complete PhD with minimal friction; need low-barrier graduation requirements |

#### Goal-Advisor Type Match Matrix (International)

| Goal | Research-Focused | Grant-Driven | Semi-Independent | Mentorship-Heavy | Hands-Off |
|------|-----------------|-------------|-----------------|-----------------|-----------|
| **Academic (tenure-track)** | Best | Good | Acceptable | Best | Poor |
| **Industry R&D** | Good | Acceptable | Best | Acceptable | Acceptable |
| **Consulting / Finance** | Poor | Poor | Acceptable | Poor | Best |
| **Government / Policy** | Acceptable | Good | Acceptable | Best | Poor |
| **Startup** | Acceptable | Acceptable | Best | Acceptable | Good |
| **Just degree** | Poor | Poor | Good | Acceptable | Best |

#### Match Rationale

| Goal | Why This Advisor Type? |
|------|----------------------|
| Academic career | Research-Focused PIs model what you need to become; Mentorship-Heavy PIs actively train you for the job market |
| Industry R&D | Semi-Independent PIs allow internships and industry collaborations without micromanaging your time |
| Consulting / Finance | Hands-Off PIs give you the time freedom needed for case prep, networking events, and recruiting cycles |
| Government / Policy | Mentorship-Heavy PIs provide network connections to agencies and policy organizations |
| Startup | Semi-Independent PIs foster the autonomy and creative thinking needed for entrepreneurship |
| Just degree | Hands-Off PIs have low overhead requirements, allowing you to graduate with minimal friction |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | Advisor type perfectly matches user's goal; all key needs met; proven track record of students achieving similar goals |
| 4 | Good match; most key needs met; minor misalignment |
| 3 | Neutral; could work but not ideal for the specific goal |
| 2 | Poor match; user's goal will be harder to achieve with this advisor |
| 1 | Worst possible match; this advisor type actively hinders user's goal |

---

## Red & Green Flags (Chinese)

### 红灯信号 (Red Flags)

- [ ] 近2年无学生一作论文
- [ ] 师兄姐去向完全不可追踪
- [ ] 有横向项目但学生不受益（无补贴、无署名、占用时间）
- [ ] 导师有行政职务但无学术产出
- [ ] 网上有多条学生投诉/PUA指控
- [ ] 近2年导师自身也无论文发表
- [ ] 学生毕业时间普遍超时（硕士>3.5年、博士>6年）
- [ ] 仅为硕导但招博士生（挂名情况）
- [ ] 经费长期中断（>3年无新基金）
- [ ] 学生无法外出实习
- [ ] 毕业要求远超学校最低标准
- [ ] 实验室有学生中途退出/转导师记录

### 绿灯信号 (Green Flags)

- [ ] 多名学生以一作发表高水平论文
- [ ] 近期获得晋升或人才称号（有动力、有资源）
- [ ] 临床/企业合作让学生受益（共同署名、实习机会）
- [ ] 师兄姐去向明确且优质
- [ ] 导师有海外经历（视野开阔）
- [ ] 实验室有定期组会但不过度
- [ ] 学生可以自由参加学术会议
- [ ] 学生有合理补贴
- [ ] 导师是博导且持续招生
- [ ] 导师愿意推荐学生实习/就业
- [ ] 毕业学生对导师有正面评价

---

## Red & Green Flags (International)

### Red Flags

- [ ] High postdoc churn rate (>2 postdocs leaving within 1 year)
- [ ] No student first-author papers in 2+ years
- [ ] Lab members rarely acknowledged properly in publications
- [ ] No conference travel support for students
- [ ] PI scoops student work (publishes student ideas without proper credit)
- [ ] Retracted papers or misconduct allegations (check Retraction Watch, PubPeer)
- [ ] Toxicity reports on Reddit (r/GradSchool, r/AskAcademia) or Glassdoor
- [ ] Visa manipulation or threats for international students
- [ ] Pre-tenure PI working students 80+ hours/week with unrealistic expectations
- [ ] No clear path to graduation (vague milestones, moving goalposts)
- [ ] Multiple students left the lab without finishing their degree
- [ ] No active grants (lab may close or lack resources)

### Green Flags

- [ ] Students publish as first author in top venues regularly
- [ ] Clear positive alumni outcomes on LinkedIn (faculty, top industry, successful careers)
- [ ] Conference travel funded and encouraged for all lab members
- [ ] Reasonable work hour expectations (no weekend/holiday pressure)
- [ ] Strong recommendation letters (verify by asking alumni directly)
- [ ] PI has tenure (stable lab, long-term commitment)
- [ ] Good teaching reviews on RateMyProfessors (indicates communication skills and respect for students)
- [ ] Active, positive lab culture visible on social media / lab website
- [ ] Students present at major conferences (not just the PI)
- [ ] Lab has clear onboarding process and written expectations
- [ ] PI supports internships and industry engagement during PhD
- [ ] Healthy alumni network that helps current students with job placement

---

## Composite Score Interpretation

| Range | Interpretation | Advice |
|-------|---------------|--------|
| 4.5-5.0 | Outstanding advisor for your goals | Highly competitive; apply early and prepare well |
| 4.0-4.4 | Excellent advisor | Strong choice; verify personal fit |
| 3.5-3.9 | Good advisor | Solid option; weigh against alternatives |
| 3.0-3.4 | Acceptable advisor | Depends on personal priorities and alternatives |
| 2.5-2.9 | Below average | Proceed with caution; ensure backup options |
| < 2.5 | Not recommended | Seek alternatives unless compelling personal reasons exist |

### Score Calculation Notes

- **Chinese context**: Use Chinese dimensions (Dim 1-11) with Chinese-specific benchmarks, university tiers, promotion timelines, and PUA/PUSH signals.
- **International context**: Use International dimensions (Dim 1-11) with international benchmarks, university rankings, tenure-track timelines, and toxicity signals.
- **Weighted composite**: Sum of (dimension score x weight) across all 11 dimensions.
- **Context detection**: Automatically select Chinese or International framework based on the advisor's institution country. For advisors at Chinese institutions abroad (e.g., joint programs), consider both frameworks.
- **Deal-Breaker override**: If ANY deal-breaker condition is triggered (see Phase 9 in SKILL.md), the composite score must be capped at 2.5 regardless of other dimensions, and the report must display a prominent warning banner.

---

## New Dimensions (v5): Sharp Critique & Retirement Risk

### Dimension 10: 导师锐评 / Advisor Sharp Critique (10%)

> **这不是一个数据维度，而是一个综合直觉判断维度。它强制报告给出明确的推荐/不推荐结论，而不是躲在分数后面。**

#### 评估框架（7问锐评）

| 问题 | 目的 | 信息来源 |
|------|------|---------|
| 1. 一句话判决 | 去掉所有修辞，给出最直接的判断 | 所有维度的综合 |
| 2. "人设"vs现实 | 识别导师对外形象与实际之间的差距 | 官网简介 vs 学生评价/发表数据 |
| 3. 最大隐藏风险 | 导师不会告诉你但你必须知道的事 | 学生评价、出组率、横向项目比例 |
| 4. 最被低估的优点 | 分数系统可能没有捕捉到的真正价值 | 学生去向中的异常好结果、独特资源 |
| 5. 5年后预测 | 实验室的发展轨迹判断 | 年龄+职称+资金+发表趋势+领域走向 |
| 6. 替代方案建议 | 给学生提供比较基准 | 同院系/同领域其他导师 |
| 7. Deal-Breaker检查 | 是否触发一票否决 | 红灯信号列表 |

#### Deal-Breaker条件（触发任何一条 → 总评上限2.5分）

- [ ] 多条独立的PUA/toxicity投诉（≥2条来自不同来源）
- [ ] 导师3年内退休且无明确接班安排
- [ ] 近3年完全无经费且无新论文
- [ ] 多名学生中途退组/延期毕业的明确证据（≥2名）
- [ ] 有被撤稿或学术不端的确认记录

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | 强烈推荐：数据和直觉一致指向优秀，几乎没有隐藏风险，"人设"与现实高度一致 |
| 4 | 推荐：整体良好，小瑕疵但不影响大局，适合大多数学生 |
| 3 | 中性：明显优缺点并存，取决于学生个人情况和风险偏好 |
| 2 | 谨慎：显著风险信号，只推荐给特定类型的学生 |
| 1 | 不推荐：触发deal-breaker或多个严重红灯 |

### Dimension 11: 退休与稳定性风险 / Retirement & Stability Risk (5%)

> **读研3-5年，如果导师中途退休/跳槽/关闭实验室，学生的损失是灾难性的。**

#### 风险因素评估

| 因素 | 低风险 | 中风险 | 高风险 |
|------|--------|--------|--------|
| 导师年龄 | 35-50岁 | 50-58岁 | 58+岁（国内）/ 65+岁（国际） |
| Tenure状态 | 已tenure / 正教授 | Tenure-track第3-5年 | Pre-tenure第1-2年 / 非tenure |
| 经费到期 | 有3年以上剩余经费 | 经费1-2年内到期但有续期迹象 | 经费已断 / 1年内到期无续期 |
| 实验室规模趋势 | 持续招生，人数稳定或增长 | 减少招生 | 不再招生或大量人员流失 |
| 跳槽信号 | 单一affiliation，稳定 | 近期有访问/兼职 | 近期换过机构 / 多个affiliation |
| 接班安排 | 有明确的副PI/co-advisor | 不明确 | 无接班人且即将退休 |

#### Scoring

| Score | Criteria |
|-------|---------|
| 5 | 导师40-55岁，已tenure/正教授，经费充足，至少10年稳定期 |
| 4 | 中年或tenure-track后期（即将tenure），经费稳定，无退休/搬迁风险 |
| 3 | 有轻微风险（经费即将到期、pre-tenure但进展良好），总体可控 |
| 2 | 明显风险：55+岁无接班人，或pre-tenure且发表/资金不够 |
| 1 | 高风险：即将退休、经费中断、有跳槽/关闭实验室迹象 |
