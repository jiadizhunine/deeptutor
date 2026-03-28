<div align="center">

**English** | [简体中文](./README.md)

</div>

<div align="center">

# DeepTutor

### Comprehensive Academic Advisor Investigation & Evaluation System

Before committing years of your life to a graduate advisor, let AI run a deep due diligence investigation. DeepTutor automatically searches a professor's publications, student outcomes, social reputation, and lab culture, then delivers a standalone HTML report to help you make a smarter decision.

![Version](https://img.shields.io/badge/version-v1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Claude_Code-purple)

<!-- screenshot of example report -->

</div>

---

## Features

- **9-Phase Investigation Pipeline** — Identity verification, student tracking, publication analysis, co-author network mapping, funding analysis, social reputation search, multi-dimensional scoring, red/green flag check, and report generation
- **Dual China/International Strategy** — Automatically detects the institution's region and switches search engines and evaluation criteria accordingly
  - **Chinese advisors**: Zhihu, Xiaomuchong, Baidu Scholar, Baoyan Forum, Xiaohongshu, Kaoyanba
  - **International advisors**: Reddit, RateMyProfessors, GradCafe, LinkedIn, Glassdoor
  - **Hong Kong / Macau / Taiwan**: Hybrid approach combining both tracks, plus PTT, LIHKG, and Dcard
- **Multilingual Output** — Ask in English, get an English report. Ask in Chinese, get a Chinese report. Works with any language.
- **5 Advisor Type Classifications** — Research-Focused, Grant/Project-Driven, Semi-Independent, Mentorship-Heavy, and Hands-Off
- **The Ceiling Principle** — Student outcomes are the single most predictive signal: your ceiling equals your seniors' ceiling
- **PUA/Exploitation Risk Assessment** — Identifies patterns of overwork, manipulation, and toxic lab culture from social platforms and student trajectories
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

DeepTutor scores advisors across 9 weighted dimensions (International version):

| # | Dimension | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Research Direction & Prospects | 10% | Field momentum, interdisciplinary potential, funding landscape |
| 2 | Publication Output & Quality | 15% | Total output, h-index, journal tier distribution, trends |
| 3 | Student Outcome Track Record | 15% | Alumni placements, time-to-degree, student publications |
| 4 | Institution & Lab Resources | 15% | Funding, equipment, collaborations, department ranking |
| 5 | Mentorship & Independence Balance | 10% | Meeting frequency, project autonomy, first-author opportunities |
| 6 | Career Trajectory & Momentum | 5% | Promotion pace, awards, growing influence |
| 7 | Toxicity / Exploitation Risk | 10% | Online reports, attrition rate, overwork signals |
| 8 | Work-Life Balance & Flexibility | 10% | Vacation policy, expected hours, conference and internship support |
| 9 | Goal-Advisor Match | 10% | Alignment between advisor style and your career goals |

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
├── SKILL.md                  # Core skill definition
├── README.md                 # Chinese README (default)
├── README.en.md              # English README
├── LICENSE                   # MIT License
├── references/               # Reference documents
│   ├── advisor_evaluation_framework.md
│   ├── chinese_academic_system.md
│   ├── international_academic_system.md
│   ├── publication_search_protocol.md
│   └── report_template.md
└── examples/                 # Sample reports
    ├── 张伟_北京大学.html
    └── sarah_mitchell_MIT.html
```

---

## License

This project is open-sourced under the [MIT License](./LICENSE).

---

## Credits

- Built with [Claude Code](https://claude.ai/claude-code)
- Powered by [Anthropic Claude](https://www.anthropic.com)
- Following [agentskills.io](https://agentskills.io) specification
