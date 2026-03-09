# 📽️ PPTX Expert - Enterprise PowerPoint Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Version: 1.0.0](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/141319co/ppt-expert/releases/tag/v1.0.0)

专业的 PowerPoint 自动化技能，支持完整的模板系统、智能布局推荐和企业级设计预设。

🌐 **API 服务**: 可作为 Custom GPT Actions 使用  
📖 **文档**: [Custom GPT 集成指南](CUSTOM_GPT_INTEGRATION.md)  
🚀 **演示**: http://qingjingxin.org/playground/ppt-expert-api/docs

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

### 🌐 API 服务 (Custom GPT)
- **RESTful API** - FastAPI 构建
- **OpenAPI 规范** - 完整的 API 文档
- **Custom GPT Actions** - 可直接集成到 ChatGPT
- **Nginx 反向代理** - 生产就绪部署

## 🚀 快速开始

### 方式 1: 命令行使用

```bash
# 安装依赖
pip install -r requirements.txt

# 保存模板
python scripts/template_manager.py save company.pptx -n "公司品牌"

# 创建演示文稿
python scripts/create_pptx.py --outline outline.md -t "公司品牌" -o output.pptx

# 从主题生成
python scripts/create_pptx.py --topic "AI 发展趋势" --slides 8 -o ai.pptx
```

### 方式 2: API 服务

```bash
# 启动 API 服务
cd api
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

# 访问 API 文档
# http://localhost:8000/docs
```

### 方式 3: 生产部署 (Nginx)

```bash
# 配置 Nginx 反向代理
sudo cp nginx/ppt-expert-api.conf /etc/nginx/conf.d/
sudo nginx -t
sudo systemctl reload nginx

# 访问 API
# http://your-domain.com/playground/ppt-expert-api/
```

### 方式 4: Custom GPT

1. 创建 Custom GPT
2. 导入 OpenAPI Schema: `http://your-domain.com/playground/ppt-expert-api/openapi.json`
3. 配置 API 认证
4. 上传文档到知识库

详见 [Custom GPT 集成指南](CUSTOM_GPT_INTEGRATION.md)

## 📖 详细文档

| 文档 | 描述 |
|------|------|
| [README.md](README.md) | 使用文档 |
| [CUSTOM_GPT_INTEGRATION.md](CUSTOM_GPT_INTEGRATION.md) | Custom GPT 集成指南 |
| [DEPLOYMENT.md](DEPLOYMENT.md) | 部署指南 |
| [GITHUB_README.md](GITHUB_README.md) | GitHub 项目说明 |
| [GITHUB_RELEASE.md](GITHUB_RELEASE.md) | Release 说明 |
| [SKILL.md](SKILL.md) | OpenClaw 技能文档 |

## 📡 API 端点

### 创建演示文稿
```bash
POST /playground/ppt-expert-api/presentations/create
```

**请求示例**
```json
{
  "title": "AI 发展趋势",
  "topic": "AI 发展趋势",
  "slides": 8,
  "template_id": "corporate"
}
```

**响应**
```json
{
  "success": true,
  "file": "ai_trends.pptx",
  "slides": 8,
  "download_url": "/playground/ppt-expert-api/presentations/download/ai_trends.pptx"
}
```

### 其他端点

| 端点 | 方法 | 功能 |
|------|------|------|
| `/playground/ppt-expert-api/presentations/create` | POST | 创建 PPT |
| `/playground/ppt-expert-api/templates/list` | GET | 列出模板 |
| `/playground/ppt-expert-api/content/quality-check` | POST | 质量检查 |
| `/playground/ppt-expert-api/content/recommend-layout` | POST | 布局推荐 |
| `/playground/ppt-expert-api/design/presets` | GET | 设计预设 |
| `/playground/ppt-expert-api/docs` | GET | API 文档 (Swagger UI) |
| `/playground/ppt-expert-api/openapi.json` | GET | OpenAPI Schema |
| `/playground/ppt-expert-api/health` | GET | 健康检查 |

## 🎨 设计预设

内置 6 种专业配色方案：

| 预设 | 描述 | 适用场景 |
|------|------|---------|
| `corporate_blue` | 专业蓝色 | 企业汇报 |
| `modern_tech` | 现代科技 | 科技公司 |
| `executive_gold` | 优雅金色 | 高管会议 |
| `healthcare_green` | 医疗绿色 | 医疗健康 |
| `startup_purple` | 活力紫色 | 初创公司 |
| `minimal_dark` | 极简深色 | 技术分享 |

## 📁 项目结构

```
ppt-expert/
├── api/                        # API 服务 (Custom GPT)
│   ├── main.py                # FastAPI 主服务
│   ├── openapi.json           # OpenAPI 规范
│   ├── requirements.txt       # API 依赖
│   └── Dockerfile             # Docker 部署
├── custom_gpt/                 # Custom GPT 配置
│   ├── PPTX_Expert_GPT_Instructions.md
│   └── DEPLOYMENT.md
├── nginx/                      # Nginx 配置
│   └── ppt-expert-api.conf    # 反向代理配置
├── scripts/                    # 核心脚本
│   ├── create_pptx.py         # 创建演示文稿
│   ├── template_manager.py    # 模板管理
│   ├── analyze_template.py    # 模板分析
│   ├── config.py              # 配置管理
│   ├── design_presets.py      # 设计预设
│   └── content_enhancer.py    # 内容增强
├── requirements.txt            # Python 依赖
├── pyproject.toml             # 项目配置
└── CUSTOM_GPT_INTEGRATION.md  # Custom GPT 集成指南
```

## 🔧 配置

创建 `~/.pptx-skill/config.json`:

```json
{
  "default_template": "公司品牌",
  "logo_position": "top_right",
  "logo_size": 0.8,
  "log_level": "INFO"
}
```

## 🚀 部署

### Docker 部署

```bash
cd api
docker build -t pptx-expert .
docker run -p 8000:8000 pptx-expert
```

### Nginx 反向代理

```bash
# 复制配置
sudo cp nginx/ppt-expert-api.conf /etc/nginx/conf.d/

# 测试配置
sudo nginx -t

# 重载 Nginx
sudo systemctl reload nginx
```

### systemd 部署

```bash
# 创建服务文件
sudo systemctl enable ppt-expert-api
sudo systemctl start ppt-expert-api
```

### Vercel/Railway

详见 [custom_gpt/DEPLOYMENT.md](custom_gpt/DEPLOYMENT.md)

## 🧪 测试

```bash
# 健康检查
curl http://localhost:8000/health

# 创建演示文稿
curl -X POST http://localhost:8000/presentations/create \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","topic":"AI","slides":5}'

# 质量检查
curl -X POST http://localhost:8000/content/quality-check \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","bullets":["point1","point2"]}'
```

## 📊 版本

当前版本：**v1.0.0**

详见 [RELEASE_NOTES.md](RELEASE_NOTES.md) 和 [Releases](https://github.com/141319co/ppt-expert/releases/tag/v1.0.0)

## 🤝 贡献

欢迎贡献！请：

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 📄 许可

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [python-pptx](https://github.com/scanny/python-pptx)
- [OpenClaw](https://openclaw.ai)
- [FastAPI](https://fastapi.tiangolo.com/)

## 📬 联系方式

- GitHub: [@141319co](https://github.com/141319co)
- Issues: [GitHub Issues](https://github.com/141319co/ppt-expert/issues)
- API 文档：`/playground/ppt-expert-api/docs` 端点

---

<div align="center">

**Made with ❤️ for better presentations**

[⭐ Star this repo](https://github.com/141319co/ppt-expert) if you find it useful!

</div>
