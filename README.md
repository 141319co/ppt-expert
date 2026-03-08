# PPTX Skill - 完整的 PowerPoint 模板系统

📽️ 创建、编辑和管理 PowerPoint 演示文稿，支持完整的模板系统。

## ✨ 功能特性

### 模板系统

- ✅ **保存模板** - 从任意 PPTX 创建可复用模板
- ✅ **提取设计** - 自动提取颜色、字体、布局、Logo
- ✅ **模板列表** - 查看所有可用模板
- ✅ **模板选择** - 交互式或命令行选择模板
- ✅ **应用模板** - 使用模板创建新演示文稿

### 支持的设计元素

| 元素 | 支持 | 说明 |
|------|------|------|
| 背景色 | ✅ | 从 Master 幻灯片提取和应用 |
| 主题颜色 | ✅ | accent1-6 完整颜色方案 |
| 字体配置 | ✅ | 标题/正文字体自动匹配 |
| Layout 布局 | ✅ | 11 种标准布局支持 |
| Logo 图片 | ✅ | 自动检测并应用到幻灯片 |
| Master 背景 | ✅ | 完整复制 Master 样式 |

---

## 🚀 快速开始

### 1. 保存你的第一个模板

```bash
cd /root/.openclaw/skills/pptx/scripts

# 从现有 PPTX 创建模板
python3 template_manager.py save /path/to/your/company.pptx \
  --name "公司品牌" \
  --description "官方品牌模板，包含 Logo 和标准配色"
```

### 2. 查看可用模板

```bash
# 列出所有模板
python3 template_manager.py list

# 或
python3 create_pptx.py --list-templates
```

### 3. 使用模板创建演示文稿

```bash
# 从 Markdown 大纲
python3 create_pptx.py --outline outline.md \
  --template "公司品牌" \
  --output presentation.pptx

# 从主题自动生成
python3 create_pptx.py --topic "2026 产品发布" \
  --slides 10 \
  --template "公司品牌" \
  --output launch.pptx
```

---

## 📁 目录结构

```
pptx/
├── SKILL.md              # 技能文档
├── README.md             # 本文件
├── editing.md            # 编辑指南
├── pptxgenjs.md          # PptxGenJS 教程
├── templates/            # 模板存储目录
│   ├── corporate.json    # 模板元数据
│   ├── corporate.pptx    # 模板源文件
│   ├── corporate_logo.png # 提取的 Logo
│   └── assets/           # 其他资源
└── scripts/
    ├── create_pptx.py       # 创建演示文稿
    ├── template_manager.py  # 模板管理
    ├── analyze_template.py  # 模板分析
    ├── interactive_select.py # 交互式选择
    ├── thumbnail.py         # 缩略图生成
    ├── add_slide.py         # 添加幻灯片
    ├── clean.py             # 清理
    └── office/
        ├── unpack.py        # 解包 PPTX
        ├── pack.py          # 打包 PPTX
        ├── soffice.py       # LibreOffice 转换
        └── validate.py      # 验证
```

---

## 📖 详细用法

### 模板管理

```bash
# 保存模板
python3 template_manager.py save input.pptx -n "模板名" -d "描述"

# 列出模板
python3 template_manager.py list

# 查看模板详情
python3 template_manager.py get <template_id>

# 获取模板文件路径
python3 template_manager.py path <template_id>

# 删除模板
python3 template_manager.py delete <template_id>
```

### 创建演示文稿

```bash
# 从 Markdown 大纲
python3 create_pptx.py --outline outline.md -o output.pptx

# 使用模板
python3 create_pptx.py --outline outline.md -t "公司品牌" -o output.pptx

# 从主题生成
python3 create_pptx.py --topic "AI 发展趋势" --slides 8 -o ai.pptx

# 从 JSON 结构
python3 create_pptx.py --json slides.json -o output.pptx

# 列出可用模板
python3 create_pptx.py --list-templates
```

### 分析模板

```bash
# 分析 PPTX 提取模板信息
python3 analyze_template.py template.pptx -o info.json

# JSON 输出
python3 analyze_template.py template.pptx --json

# 人类可读格式
python3 analyze_template.py template.pptx
```

### 交互式选择

```bash
# 交互模式
python3 interactive_select.py

# 快速选择
python3 interactive_select.py --select "公司"

# 仅列出
python3 interactive_select.py --list

# JSON 输出
python3 interactive_select.py --list --json
```

### 编辑现有 PPT

```bash
# 1. 分析
python3 thumbnail.py template.pptx
python3 -m markitdown template.pptx

# 2. 解包
python3 office/unpack.py template.pptx unpacked/

# 3. 编辑 slides/slide{N}.xml

# 4. 清理并打包
python3 clean.py unpacked/
python3 office/pack.py unpacked/ output.pptx --original template.pptx
```

---

## 📝 Markdown 大纲格式

```markdown
# 演示文稿标题
subtitle: 2026 年度回顾
author: 你的名字

## 简介
- 欢迎和议程
- 今天的主要目标

## 市场分析
- 市场同比增长 15%
- 竞争地位强劲

## 财务摘要
- Q4 表现强劲
- 收入目标超额完成
```

---

## 🎨 模板 JSON 结构

```json
{
  "id": "corporate",
  "name": "公司品牌",
  "description": "官方品牌模板",
  "slide_count": 10,
  "layout_count": 8,
  "theme_colors": {
    "accent1": "003366",
    "accent2": "006699",
    "bg1": "FFFFFF"
  },
  "theme_fonts": {
    "heading": "Arial",
    "body": "Calibri"
  },
  "sample_colors": {
    "most_used": ["003366", "FFFFFF", "006699"]
  },
  "logo_file": "assets/corporate_logo.png",
  "masters": [...],
  "layouts": [...]
}
```

---

## 🔧 常见问题

### Q: 如何保存带 Logo 的模板？
A: 确保 Logo 在 Master 幻灯片上，保存时会自动提取。

### Q: 模板保存在哪里？
A: `~/.openclaw/skills/pptx/templates/`

### Q: 如何分享模板？
A: 复制 `templates/` 目录下的 `.json` 和 `.pptx` 文件。

### Q: 支持哪些布局？
A: 支持 11 种标准布局：Title、Title and Content、Section Header、Two Content、Comparison、Title Only、Blank、Content with Caption、Picture with Caption、Vertical Title、Vertical Text。

---

## 📦 依赖

- `python-pptx` - PowerPoint 操作
- `markitdown[pptx]` - 文本提取
- `Pillow` - 图像处理
- `defusedxml` - XML 解析

---

## 📄 许可

见 LICENSE.txt
