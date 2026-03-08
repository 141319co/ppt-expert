---
name: pptx
description: Complete PowerPoint skill with template system. Create, edit, and manage PPTX files with reusable templates including colors, fonts, layouts, and logos.
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill - 完整模板系统

## 📁 模板系统

### 保存模板

从现有 PPTX 创建可复用模板：

```bash
# 保存模板
python3 scripts/template_manager.py save your_template.pptx --name "公司模板" --description "官方品牌模板"

# 模板存储在 ~/.openclaw/skills/pptx/templates/
```

### 查看模板

```bash
# 列出所有模板
python3 scripts/template_manager.py list

# 查看模板详情
python3 scripts/template_manager.py get <template_id>

# 获取模板文件路径
python3 scripts/template_manager.py path <template_id>
```

### 删除模板

```bash
python3 scripts/template_manager.py delete <template_id>
```

---

## 🚀 创建演示文稿

### 使用模板创建

```bash
# 从大纲创建（使用模板）
python3 scripts/create_pptx.py --outline outline.md --template "公司模板" --output deck.pptx

# 从主题生成（使用模板）
python3 scripts/create_pptx.py --topic "Q4 销售回顾" --slides 8 --template corporate --output review.pptx

# 列出可用模板
python3 scripts/create_pptx.py --list-templates
```

### 不使用模板

```bash
# 从 Markdown 大纲
python3 scripts/create_pptx.py --outline outline.md --output deck.pptx

# 从 JSON 结构
python3 scripts/create_pptx.py --json slides.json --output deck.pptx
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

## 🔍 分析模板

```bash
# 分析 PPTX 提取模板信息
python3 scripts/analyze_template.py template.pptx --output template_info.json

# JSON 输出
python3 scripts/analyze_template.py template.pptx --json
```

分析内容包括：
- 📊 幻灯片数量、布局数量
- 🎨 主题颜色方案
- 📝 字体配置（标题/正文）
- 🖼️ Master 幻灯片和背景
- 📐 占位符布局
- 🏢 Logo 和图片位置

---

## ✏️ 编辑现有 PPT

### 工作流

1. **分析模板**
```bash
python3 scripts/thumbnail.py template.pptx
python3 -m markitdown template.pptx
```

2. **解包**
```bash
python3 scripts/office/unpack.py template.pptx unpacked/
```

3. **编辑 slides/slide{N}.xml**

4. **清理并打包**
```bash
python3 scripts/clean.py unpacked/
python3 scripts/office/pack.py unpacked/ output.pptx --original template.pptx
```

---

## 🎨 模板功能支持

### ✅ 完整支持

| 功能 | 说明 |
|------|------|
| 背景色 | 从模板 Master 幻灯片提取和应用 |
| 主题颜色 | 提取 accent1-6 颜色方案 |
| 字体 | 标题和正文字体配置 |
| Layout | 使用模板的占位符布局 |
| Logo | 自动检测并应用到幻灯片 |
| Master 背景 | 复制 Master 幻灯片背景样式 |

### 📁 模板存储结构

```
~/.openclaw/skills/pptx/templates/
├── corporate.json          # 模板元数据
├── corporate.pptx          # 模板源文件
├── corporate_logo.png      # 提取的 Logo
├── startup.json
├── startup.pptx
└── assets/
    └── ...
```

### 🔧 模板 JSON 结构

```json
{
  "id": "corporate",
  "name": "公司模板",
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

## 📋 快速参考

| 任务 | 命令 |
|------|------|
| 保存模板 | `template_manager.py save file.pptx -n "Name"` |
| 列出模板 | `template_manager.py list` 或 `create_pptx.py --list-templates` |
| 创建 PPT | `create_pptx.py --outline file.md -t template -o out.pptx` |
| 分析模板 | `analyze_template.py file.pptx -o info.json` |
| 解包 PPT | `office/unpack.py file.pptx unpacked/` |
| 打包 PPT | `office/pack.py unpacked/ out.pptx --original template.pptx` |
| 缩略图 | `thumbnail.py file.pptx` |
| 提取文本 | `python -m markitdown file.pptx` |

---

## 🎯 使用示例

### 首次设置模板

```bash
# 1. 上传你的公司 PPTX 模板
# 2. 保存为模板
python3 scripts/template_manager.py save company_brand.pptx \
  --name "公司品牌" \
  --description "官方品牌模板，包含 Logo 和标准配色"

# 3. 查看模板
python3 scripts/template_manager.py list
```

### 使用模板创建演示文稿

```bash
# 创建新演示文稿
python3 scripts/create_pptx.py \
  --topic "2026 产品发布" \
  --slides 10 \
  --template "公司品牌" \
  --output product_launch.pptx
```

### 分析现有模板

```bash
# 分析模板详情
python3 scripts/analyze_template.py existing.pptx \
  --output template_analysis.json

# 查看提取的颜色和字体
cat template_analysis.json | jq '.theme_colors, .theme_fonts'
```

---

## ⚠️ 注意事项

1. **模板必须先保存** - 使用 `template_manager.py save` 创建模板
2. **Logo 自动检测** - 保存模板时自动提取 Master 幻灯片中的 Logo
3. **颜色提取** - 从模板中最常使用的颜色自动推断主色/辅色
4. **布局匹配** - 优先使用模板的 Title/Content 布局

---

## 📦 依赖

- `python-pptx` - PowerPoint 操作
- `markitdown[pptx]` - 文本提取
- `Pillow` - 图像处理
- `defusedxml` - XML 解析
