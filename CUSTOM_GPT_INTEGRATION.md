# 🤖 Custom GPT 完整集成指南

## 📋 概述

将 PPTX Expert 集成到 ChatGPT Custom GPT，通过 **Actions (API)** 实现完整功能。

## 🏗️ 架构

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   ChatGPT UI    │────▶│  Custom GPT      │────▶│  PPTX API       │
│   (用户对话)     │     │  (Actions 调用)   │     │  (FastAPI 服务)  │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                │                        │
                                │                        ▼
                                │              ┌─────────────────┐
                                │              │  Python Scripts │
                                │              │  (核心逻辑)      │
                                │              └─────────────────┘
                                ▼
                       ┌─────────────────┐
                       │  OpenAPI Spec   │
                       │  (API 定义)      │
                       └─────────────────┘
```

## 🚀 快速开始

### 1. 部署 API 服务

```bash
# 本地开发
cd /root/.openclaw/skills/pptx/api
pip install -r requirements.txt
uvicorn main:app --reload

# 访问 http://localhost:8000/docs 查看 API 文档
```

### 2. 创建 Custom GPT

1. 访问 https://chat.openai.com/gpts
2. 点击 "Create a GPT"
3. 配置：

**基本信息**
- Name: `PPTX Expert`
- Description: `Professional PowerPoint presentation creator`
- Instructions: 复制 `custom_gpt/PPTX_Expert_GPT_Instructions.md`

**Actions 配置**
- 点击 "Create new action"
- Schema: 导入 `api/openapi.json`
- Authentication: API Key (Header: `X-API-Key`)

**知识库**
- 上传 `README.md`, `SKILL.md`

### 3. 测试

```
用户：帮我创建一个关于 AI 发展趋势的 PPT

GPT: 我来帮你创建 AI 发展趋势的演示文稿。

请问：
1. 需要多少页幻灯片？（默认 5 页）
2. 有偏好的模板吗？
3. 有特定的大纲或要点要包含吗？

[调用 POST /presentations/create]

✅ 已创建演示文稿：ai_trends.pptx
📊 共 5 页幻灯片
📥 下载：[download_url]
```

## 📡 API 端点

### 创建演示文稿
```
POST /presentations/create
```

**请求**
```json
{
  "title": "AI 发展趋势",
  "subtitle": "2026 年展望",
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
  "download_url": "/presentations/download/ai_trends.pptx"
}
```

### 上传模板
```
POST /templates/upload
Content-Type: multipart/form-data

file: [PPTX 文件]
name: "公司品牌"
description: "官方模板"
```

### 列出模板
```
GET /templates/list
```

### 质量检查
```
POST /content/quality-check
```

**请求**
```json
{
  "title": "市场分析",
  "bullets": ["增长 25%", "竞争激烈", "机遇与挑战并存"]
}
```

**响应**
```json
{
  "score": 85,
  "issues": [],
  "suggestions": ["可以添加具体数据支持"]
}
```

### 推荐布局
```
POST /content/recommend-layout
```

## 🎯 使用场景

### 场景 1: 快速创建 PPT

```
用户：帮我做一个产品发布会的 PPT

GPT: 好的，我来帮你创建产品发布会演示文稿。

[调用 create API]

✅ 已创建 8 页幻灯片：
1. 封面
2. 产品概述
3. 核心功能
4. 技术优势
5. 市场定位
6. 发布计划
7. 团队介绍
8. Q&A

需要我调整任何内容吗？
```

### 场景 2: 使用模板

```
用户：用公司模板做个季度汇报

GPT: 我来查看可用模板...

[调用 list templates API]

找到 3 个模板：
1. 公司品牌 - 官方模板
2. 季度汇报 - 财务风格
3. 简约深色 - 现代风格

建议使用"季度汇报"模板，合适吗？
```

### 场景 3: 内容优化

```
用户：这页内容怎么样？
标题：业绩增长
要点：["增长 20%", "超预期"]

GPT: 我来检查质量...

[调用 quality-check API]

评分：65/100

建议：
⚠️ 要点太少（2 个），建议 4-6 个
⚠️ 可以添加具体数据
💡 建议使用图表布局

需要我帮你优化吗？
```

## 🔐 认证配置

### 在 Custom GPT 中设置

1. Actions → Authentication
2. Type: `API Key`
3. Header Name: `X-API-Key`
4. API Key: `your-secret-key`

### 在 API 中验证

```python
@app.middleware("http")
async def authenticate(request, call_next):
    api_key = request.headers.get("X-API-Key")
    if api_key != os.getenv("API_KEY"):
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})
    return await call_next(request)
```

## 📦 部署选项

| 平台 | 难度 | 成本 | 推荐 |
|------|------|------|------|
| Vercel | ⭐⭐ | 免费 | ✅ |
| Railway | ⭐⭐ | $5/月 | ✅ |
| Docker | ⭐⭐⭐ | 自托管 | ✅ |
| AWS | ⭐⭐⭐⭐ | 按量 | 高级 |

## 🧪 测试清单

- [ ] API 健康检查
- [ ] 创建演示文稿
- [ ] 上传模板
- [ ] 列出模板
- [ ] 质量检查
- [ ] 布局推荐
- [ ] 文件下载
- [ ] 错误处理
- [ ] 认证验证

## 📊 监控指标

```python
# 添加监控中间件
@app.middleware("http")
async def track_metrics(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    
    logger.info(f"{request.method} {request.url.path} - {duration:.2f}s")
    return response
```

## 🐛 常见问题

**Q: API 超时怎么办？**
A: 增加超时设置，优化大文件处理

**Q: 文件上传失败？**
A: 检查文件大小限制，确保 multipart 配置正确

**Q: Custom GPT 不识别 Actions？**
A: 确保 OpenAPI schema 正确，重新导入

## 📚 资源

- [OpenAI Actions 文档](https://platform.openai.com/docs/actions)
- [OpenAPI 规范](https://swagger.io/specification/)
- [FastAPI 文档](https://fastapi.tiangolo.com/)

---

**Made with ❤️ for better presentations**
