# 📽️ PPTX Expert - Enterprise PowerPoint Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-green)](https://openclaw.ai)

专业的 PowerPoint 自动化技能，支持完整的模板系统、智能布局推荐和企业级设计预设。

## ✨ 核心功能

### 🎨 模板系统
- **保存模板** - 从任意 PPTX 创建可复用模板
- **智能提取** - 自动提取颜色、字体、布局、Logo
- **模板管理** - 列表、查看、删除模板
- **一键应用** - 使用模板快速创建新演示文稿

### 🤖 AI 增强
- **内容质量检查** - 自动检测内容问题并给出建议
- **智能布局推荐** - 根据内容类型推荐最佳布局
- **内容优化** - 自动优化文字长度和格式

### 🎯 企业级特性
- **专业设计预设** - 6+ 企业级配色方案
- **图表美化** - 专业图表样式配置
- **Logo 自动应用** - 品牌标识一致性强
- **多语言支持** - 中英文混合内容处理

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/141319co/ppt-expert.git
cd ppt-expert

# 安装依赖
pip install -r requirements.txt
```

### 基础使用

```bash
# 1. 保存你的模板
python scripts/template_manager.py save company_template.pptx -n "公司品牌" -d "官方模板"

# 2. 查看可用模板
python scripts/template_manager.py list

# 3. 使用模板创建演示文稿
python scripts/create_pptx.py --outline outline.md -t "公司品牌" -o output.pptx

# 4. 从主题自动生成
python scripts/create_pptx.py --topic "AI 发展趋势" --slides 8 -o ai.pptx
```

## 📖 详细文档

### 模板管理

```bash
# 保存模板
python scripts/template_manager.py save template.pptx -n "名称" -d "描述"

# 列出模板
python scripts/template_manager.py list

# 查看模板详情
python scripts/template_manager.py get <template_id>

# 删除模板
python scripts/template_manager.py delete <template_id>

# 获取模板路径
python scripts/template_manager.py path <template_id>
```

### 创建演示文稿

```bash
# 从 Markdown 大纲
python scripts/create_pptx.py --outline outline.md -o output.pptx

# 使用模板
python scripts/create_pptx.py --outline outline.md -t "公司品牌" -o output.pptx

# 从主题生成
python scripts/create_pptx.py --topic "产品发布" --slides 10 -o launch.pptx

# 质量检查
python scripts/create_pptx.py --outline outline.md -o output.pptx -q

# 详细输出
python scripts/create_pptx.py --outline outline.md -o output.pptx -v
```

### 分析模板

```bash
# 分析模板
python scripts/analyze_template.py template.pptx -o info.json

# JSON 输出
python scripts/analyze_template.py template.pptx --json
```

## 📝 Markdown 大纲格式

```markdown
# 演示文稿标题
subtitle: 副标题
author: 作者

## 简介
- 欢迎和议程
- 主要目标

## 市场分析
- 市场增长 25%
- 竞争格局变化

## 财务摘要
- Q4 表现强劲
- 收入目标超额
```

## 🎨 设计预设

内置 6 种专业配色方案：

| 预设名称 | 描述 | 适用场景 |
|---------|------|---------|
| `corporate_blue` | 专业蓝色 | 企业汇报、商务演示 |
| `modern_tech` | 现代科技 | 科技公司、产品发布 |
| `executive_gold` | 优雅金色 | 高管会议、年度报告 |
| `healthcare_green` | 医疗绿色 | 医疗健康、 wellness |
| `startup_purple` | 活力紫色 | 初创公司、创意机构 |
| `minimal_dark` | 极简深色 | 现代演示、技术分享 |

## 📁 项目结构

```
ppt-expert/
├── scripts/
│   ├── create_pptx.py       # 主创建脚本
│   ├── template_manager.py  # 模板管理
│   ├── analyze_template.py  # 模板分析
│   ├── config.py            # 配置管理
│   ├── design_presets.py    # 设计预设
│   ├── content_enhancer.py  # 内容增强
│   └── office/
│       ├── unpack.py        # 解包工具
│       ├── pack.py          # 打包工具
│       └── ...
├── templates/                # 模板存储
├── requirements.txt          # 依赖
├── SKILL.md                 # OpenClaw 技能文档
└── README.md                # 本文件
```

## ⚙️ 配置

创建 `~/.pptx-skill/config.json`：

```json
{
  "template_dir": "~/.openclaw/skills/pptx/templates",
  "default_template": "公司品牌",
  "logo_position": "top_right",
  "logo_size": 0.8,
  "default_font_heading": "Arial",
  "default_font_body": "Calibri",
  "log_level": "INFO"
}
```

或使用环境变量：

```bash
export PPTX_SKILL_DEFAULT_TEMPLATE="公司品牌"
export PPTX_SKILL_LOG_LEVEL="DEBUG"
```

## 🔧 开发

```bash
# 安装开发依赖
pip install -r requirements.txt
pip install pytest black flake8

# 运行测试
pytest tests/

# 代码格式化
black scripts/

# 代码检查
flake8 scripts/
```

## 📊 质量检查

内置质量检查功能：

- ✅ 标题长度检查 (<50 字符)
- ✅ 项目符号数量检查 (4-6 个)
- ✅ 项目符号长度检查 (<100 字符)
- ✅ 对比度检查 (WCAG AA 标准)
- ✅ 布局一致性检查

## 🤝 贡献

欢迎贡献！请遵循以下步骤：

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 📄 许可

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [python-pptx](https://github.com/scanny/python-pptx) - PowerPoint 操作库
- [OpenClaw](https://openclaw.ai) - AI 助手框架
- [Anthropics Skills](https://github.com/anthropics/skills) - 灵感来源

## 📬 联系方式

- GitHub: [@141319co](https://github.com/141319co)
- Issues: [GitHub Issues](https://github.com/141319co/ppt-expert/issues)

---

<div align="center">

**Made with ❤️ for better presentations**

[⭐ Star this repo](https://github.com/141319co/ppt-expert) if you find it useful!

</div>
