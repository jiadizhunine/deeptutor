<div align="center">

**English** | [简体中文](./README.md)

</div>

<div align="center">

# DeepTutor

### Comprehensive Academic Advisor Investigation & Evaluation System

Before committing years of your life to a graduate advisor, let AI run a deep due diligence investigation. DeepTutor automatically searches a professor's publications, student outcomes, social reputation, and lab culture, then delivers a standalone HTML report to help you make a smarter decision.

![Version](https://img.shields.io/badge/version-v1.3-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Claude_Code%20|%20Cursor%20|%20OpenClaw%20|%20OpenCode-purple)

<!-- screenshot of example report -->

</div>

---

## Features

- **10-Phase Investigation Pipeline** — Identity verification, student tracking, publication analysis, co-author network mapping, funding analysis, social reputation search, field macro trend analysis, multi-dimensional scoring, sharp critique, and report generation
- **Dual China/International Strategy** — Automatically detects the institution's region and switches search engines and evaluation criteria accordingly
  - **Chinese advisors**: Zhihu, Xiaomuchong, Baidu Scholar, Baoyan Forum, Xiaohongshu, Kaoyanba
  - **International advisors**: Reddit, RateMyProfessors, GradCafe, LinkedIn, Glassdoor
  - **Hong Kong / Macau / Taiwan**: Hybrid approach combining both tracks, plus PTT, LIHKG, and Dcard
- **Multilingual Output** — Ask in English, get an English report. Ask in Chinese, get a Chinese report. Works with any language.
- **5 Advisor Type Classifications** — Research-Focused, Grant/Project-Driven, Semi-Independent, Mentorship-Heavy, and Hands-Off
- **The Ceiling Principle** — Student outcomes are the single most predictive signal: your ceiling equals your seniors' ceiling
- **PUA/Exploitation Risk Assessment** — Identifies patterns of overwork, manipulation, and toxic lab culture from social platforms and student trajectories
- **Sharp Critique (v1.1)** — 7-question deep analysis + Deal-Breaker veto mechanism, gives clear recommend/don't-recommend verdicts
- **Field Macro Trend (v1.1)** — Lifecycle positioning (Emerging/Growth/Mature/Declining/Sunset) + job market outlook + tech disruption risk
- **Retirement & Stability Risk (v1.1)** — Assesses whether the advisor will remain active for the student's full degree
- **Multi-Advisor Comparison Mode** — Side-by-side comparison of multiple professors with a synthesized recommendation
- **Standalone HTML Reports** — Single-file delivery with zero external dependencies, viewable offline

---

## Installation

```bash
# Method 1: npx (recommended)
npx skills add jiadizhunine/deeptutor

# Method 2: Git Clone
git clone https://github.com/jiadizhunine/deeptutor.git ~/.claude/skills/deeptutor

# Method 3: Manual Download
# Download the latest release from GitHub Releases and extract to ~/.claude/skills/deeptutor/
```

---

## Usage

Simply type a natural language prompt in Claude Code:

```
Investigate Prof. Smith at MIT Biology department
```

```
帮我调查一下北京大学生命科学学院的张教授
```

```
Compare these three advisors: Prof. Wang at Peking University, Prof. Li at Tsinghua, and Prof. Johnson at Stanford
```

DeepTutor automatically detects the language and region, launches the appropriate investigation pipeline, and generates a standalone `.html` report.

---

## Report Examples

- [English Case: Sarah Mitchell, MIT](https://jiadizhunine.github.io/deeptutor/examples/sarah_mitchell_MIT.html)
- [中文案例：张伟\_北京大学](https://jiadizhunine.github.io/deeptutor/examples/张伟_北京大学.html)

---

## Evaluation Dimensions

DeepTutor scores advisors across **11 weighted dimensions** (International version):

| # | Dimension | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Field Macro Trend | 10% | Lifecycle positioning, funding trends, job market, tech disruption risk |
| 2 | Publication Output & Quality | 12% | Total output, h-index, journal tier distribution, trends |
| 3 | Student Outcome Track Record | 13% | Alumni placements, time-to-degree, student publications |
| 4 | Institution & Lab Resources | 12% | Funding, equipment, collaborations, department ranking |
| 5 | Mentorship & Independence Balance | 8% | Meeting frequency, project autonomy, first-author opportunities |
| 6 | Career Trajectory & Momentum | 5% | Promotion pace, awards, growing influence |
| 7 | Toxicity / Exploitation Risk | 10% | Online reports, attrition rate, overwork signals |
| 8 | Work-Life Balance & Flexibility | 8% | Vacation policy, expected hours, conference and internship support |
| 9 | Goal-Advisor Match | 7% | Alignment between advisor style and your career goals |
| 10 | **Advisor Sharp Critique** | 10% | 7-question deep analysis, Deal-Breaker veto, synthesized verdict |
| 11 | **Retirement & Stability Risk** | 5% | Age, tenure status, funding expiry, succession planning |

> The Chinese version uses adapted dimensions (e.g., "时间自由度" evaluates freedom for civil service exams and internships). See [SKILL.md](./SKILL.md) for the full specification.

---

## Advisor Types

| Type | Description | Best For |
|------|-------------|----------|
| Research-Focused | Deep academic focus, pushes for top-tier publications | Students aiming for academic careers and high-impact papers |
| Grant/Project-Driven | Funded by applied or industry projects | Students seeking project experience and industry connections |
| Semi-Independent | Moderate guidance with room to explore | Self-motivated students who want flexibility |
| Mentorship-Heavy | Hands-on guidance, frequent meetings, structured feedback | Students new to research or who thrive with structure |
| Hands-Off | Minimal supervision, students largely self-directed | Students with clear goals and strong self-discipline; risky otherwise |

---

## Project Structure

```
deeptutor/
├── SKILL.md                          # Core skill definition
├── .claude/skills/deeptutor/SKILL.md # Claude Code adapter
├── .agents/skills/deeptutor/SKILL.md # AGENTS.md ecosystem
├── .cursor/rules/deeptutor.mdc       # Cursor IDE adapter
├── .openclaw/AGENTS.md               # OpenClaw adapter
├── .opencode/AGENTS.md               # OpenCode adapter
├── scripts/                          # Self-contained tools (zero dependencies)
│   ├── robust_fetch.py               # Anti-bot web fetch (3-layer fallback)
│   ├── search_social.py              # Chinese social platform search
│   └── generate_report.py            # JSON → HTML report renderer
├── references/                       # Reference documents
│   ├── advisor_evaluation_framework.md
│   ├── chinese_academic_system.md
│   ├── international_academic_system.md
│   ├── publication_search_protocol.md
│   ├── report_template.md
│   ├── web_rooter_integration.md     # Web access fallback strategy
│   └── lite_mode.md                  # Lite mode specification
└── examples/                         # Sample reports
```

---

## License

This project is open-sourced under the [MIT License](./LICENSE).

---

## Credits

- Built with [Claude Code](https://claude.ai/claude-code)
- Powered by [Anthropic Claude](https://www.anthropic.com)
- Web access capabilities powered by [Web-Rooter](https://github.com/pinkpixel-dev/web-rooter) (MIT License)
- Following [agentskills.io](https://agentskills.io) specification
