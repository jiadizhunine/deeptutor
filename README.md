<div align="center">

[English](./README.en.md) | **简体中文**

</div>

<div align="center">

# DeepTutor

### 学术导师综合调查评估系统

在选择研究生导师之前，用 AI 做一次深度尽职调查。DeepTutor 自动检索导师的学术成果、学生去向、社交舆情与实验室文化，生成一份独立的 HTML 评估报告，帮你做出更明智的读研决策。

![Version](https://img.shields.io/badge/version-v1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Claude_Code-purple)

<!-- screenshot of example report -->

</div>

---

## 功能特色

- **9 阶段调查流程** — 身份验证 → 学生追踪 → 发表分析 → 合作网络 → 经费分析 → 社交舆情 → 多维评分 → 红绿灯检查 → 报告生成
- **中国/国际双轨策略** — 自动识别机构所在地区，切换对应的搜索引擎与评估维度
  - **中国导师**：知乎、小木虫、百度学术、保研论坛、小红书、考研帮
  - **国际导师**：Reddit、RateMyProfessors、GradCafe、LinkedIn、Glassdoor
  - **港澳台导师**：双轨混合，兼顾 PTT、LIHKG、Dcard
- **多语言支持** — 中文提问生成中文报告，英文提问生成英文报告，以此类推
- **5 种导师类型分类** — 学术型 / 项目型 / 半放养型 / 指导型 / 纯放养型
- **天花板法则** — 学生去向是最重要的评估信号：你的上限 = 师兄师姐的上限
- **PUA/PUSH 风险评估** — 从社交平台与学生轨迹中识别压榨与精神控制风险
- **多导师对比模式** — 并排对比多位导师，输出综合推荐
- **独立 HTML 报告** — 单文件交付，无外部依赖，可离线浏览

---

## 安装方法

```bash
# 方法一：npx（推荐）
npx skills add jiadizhunine/deeptutor

# 方法二：Git Clone
git clone https://github.com/jiadizhunine/deeptutor.git ~/.claude/skills/deeptutor

# 方法三：手动下载
# 从 GitHub Releases 下载最新版本，解压到 ~/.claude/skills/deeptutor/
```

---

## 使用方法

在 Claude Code 中直接输入自然语言即可触发调查：

```
帮我调查一下北京大学生命科学学院的张教授
```

```
Investigate Prof. Smith at MIT Biology department
```

```
帮我对比这三个导师：A大学的王教授、B大学的李教授、C大学的Prof. Johnson
```

系统会自动识别语言和地区，启动对应的调查流程，最终生成一份独立的 `.html` 报告。

---

## 报告示例

- [中文案例：张伟\_北京大学](https://jiadizhunine.github.io/deeptutor/examples/张伟_北京大学.html)
- [English Case: Sarah Mitchell, MIT](https://jiadizhunine.github.io/deeptutor/examples/sarah_mitchell_MIT.html)

---

## 评估维度

DeepTutor 从 9 个维度对导师进行量化评估（中国版本）：

| # | 维度 | 权重 | 说明 |
|---|------|------|------|
| 1 | 研究方向与前景 | 10% | 领域热度、发展趋势、交叉潜力 |
| 2 | 发表成果与质量 | 15% | 总产出、h-index、期刊层次分布 |
| 3 | 学生培养实绩 | 15% | 毕业生去向、学位完成时间、学生发表 |
| 4 | 平台与资源 | 15% | 经费、设备、合作网络、学科排名 |
| 5 | 独立性与成长空间 | 10% | 课题自主权、一作/通讯机会 |
| 6 | 职业轨迹与势头 | 5% | 职称晋升速度、奖项荣誉、学术影响力趋势 |
| 7 | PUA/PUSH 风险 | 10% | 网络舆情、学生流失率、毕业延期比例 |
| 8 | 时间自由度 | 10% | 是否允许实习/考公/副业、作息要求 |
| 9 | 毕业目标匹配 | 10% | 导师风格与你的职业目标的契合度 |

> 国际版本使用经过调整的维度体系（如"Work-Life Balance"替代"时间自由度"），详见 [SKILL.md](./SKILL.md)。

---

## 导师类型

| 类型 | 标签 | 特征 | 适合人群 |
|------|------|------|----------|
| 学术型 | Research-Focused | 追求顶刊发表，学术要求高 | 志在学术深造、追求高水平论文的学生 |
| 项目型 | Grant/Project-Driven | 横向/纵向项目多，偏应用导向 | 想积累项目经验、偏工程方向的学生 |
| 半放养型 | Semi-Independent | 适度指导，给予一定自由度 | 有一定自驱力、希望灵活安排的学生 |
| 指导型 | Mentorship-Heavy | 手把手带，会议频繁，反馈及时 | 需要结构化指导、科研新手 |
| 纯放养型 | Hands-Off | 几乎不管，靠学生自己摸索 | 目标明确且自律的学生；否则风险极大 |

---

## 项目结构

```
deeptutor/
├── SKILL.md                  # 核心技能定义
├── README.md                 # 中文说明（默认）
├── README.en.md              # English README
├── LICENSE                   # MIT 许可证
├── references/               # 参考文档
│   ├── advisor_evaluation_framework.md
│   ├── chinese_academic_system.md
│   ├── international_academic_system.md
│   ├── publication_search_protocol.md
│   └── report_template.md
└── examples/                 # 虚拟案例
    ├── 张伟_北京大学.html
    └── sarah_mitchell_MIT.html
```

---

## 许可证

本项目采用 [MIT 许可证](./LICENSE) 开源。

---

## 致谢

- Built with [Claude Code](https://claude.ai/claude-code)
- Powered by [Anthropic Claude](https://www.anthropic.com)
- Following [agentskills.io](https://agentskills.io) specification
