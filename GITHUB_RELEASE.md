# 🎉 PPTX Expert v1.0.0 - Initial Release

## Release Information

- **Version**: 1.0.0
- **Release Date**: 2026-03-08
- **License**: MIT
- **Python**: 3.11+

## 🚀 What's New

### Core Features

#### 📽️ Template System
- Save any PPTX as a reusable template
- Auto-extract colors, fonts, layouts, and logos
- Full template management (list, view, delete)
- One-click template application

#### 🎨 Design Presets
- 6 professional color palettes:
  - `corporate_blue` - Business presentations
  - `modern_tech` - Technology companies
  - `executive_gold` - Executive meetings
  - `healthcare_green` - Healthcare/wellness
  - `startup_purple` - Creative agencies
  - `minimal_dark` - Modern presentations
- Typography presets (corporate, modern, elegant, tech)
- Chart style configurations
- Layout templates

#### 🤖 AI Enhancement
- Content quality scoring
- Intelligent layout recommendations
- Content optimization suggestions
- Multi-language support (Chinese/English)

#### ⚙️ Engineering
- Configuration management (file + environment variables)
- Structured logging
- Comprehensive error handling
- Dependency management

### 📦 Installation

```bash
# Clone repository
git clone https://github.com/141319co/ppt-expert.git
cd ppt-expert

# Install dependencies
pip install -r requirements.txt

# Or install from PyPI (future)
# pip install pptx-expert
```

### 📖 Quick Start

```bash
# Save a template
python scripts/template_manager.py save company.pptx -n "Company Brand" -d "Official template"

# List templates
python scripts/template_manager.py list

# Create presentation with template
python scripts/create_pptx.py --outline outline.md -t "Company Brand" -o output.pptx

# Generate from topic
python scripts/create_pptx.py --topic "AI Trends" --slides 8 -o ai.pptx

# Quality check
python scripts/create_pptx.py --outline outline.md -o output.pptx -q
```

### 📝 Markdown Outline Format

```markdown
# Presentation Title
subtitle: Your Subtitle
author: Your Name

## Introduction
- Welcome and agenda
- Key objectives

## Market Analysis
- Market growth 25%
- Competitive landscape

## Conclusion
- Summary
- Next steps
```

### 🔧 Configuration

Create `~/.pptx-skill/config.json`:

```json
{
  "default_template": "Company Brand",
  "logo_position": "top_right",
  "logo_size": 0.8,
  "log_level": "INFO"
}
```

### 📊 Quality Checks

Built-in quality validation:
- ✅ Title length (<50 chars)
- ✅ Bullet count (4-6 per slide)
- ✅ Bullet length (<100 chars)
- ✅ Contrast ratio (WCAG AA)
- ✅ Layout consistency

### 📁 Project Structure

```
ppt-expert/
├── scripts/                    # Core scripts (12 files)
│   ├── create_pptx.py         # Main creation script
│   ├── template_manager.py    # Template management
│   ├── analyze_template.py    # Template analysis
│   ├── config.py              # Configuration
│   ├── design_presets.py      # Design presets
│   ├── content_enhancer.py    # AI enhancement
│   └── office/                # Office tools
├── SKILL.md                    # OpenClaw skill doc
├── README.md                   # Documentation
├── requirements.txt            # Dependencies
├── pyproject.toml             # Python project config
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore
```

### 🐛 Known Limitations

1. Logo extraction only works for images on Master slides
2. Complex animations and transitions not preserved
3. Embedded videos require manual addition

### 📅 Roadmap

- [ ] v1.1.0 - AI content generation
- [ ] v1.2.0 - PDF export support
- [ ] v1.3.0 - More design presets
- [ ] v2.0.0 - Web interface, batch processing

### 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- [python-pptx](https://github.com/scanny/python-pptx) - PowerPoint library
- [OpenClaw](https://openclaw.ai) - AI assistant framework
- [Anthropics Skills](https://github.com/anthropics/skills) - Inspiration

### 📬 Contact

- GitHub: [@141319co](https://github.com/141319co)
- Issues: [GitHub Issues](https://github.com/141319co/ppt-expert/issues)

---

<div align="center">

**Made with ❤️ for better presentations**

[Documentation](README.md) • [Report Bug](issues) • [Request Feature](issues)

</div>
