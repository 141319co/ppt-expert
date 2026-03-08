# Custom GPT 部署指南

## 📋 部署方式

### 方式 1: Vercel (推荐)

```bash
# 安装 Vercel CLI
npm install -g vercel

# 部署 API
cd /root/.openclaw/skills/pptx/api
vercel --prod
```

### 方式 2: Railway

1. 创建 Railway 项目
2. 连接 GitHub 仓库
3. 设置环境变量
4. 自动部署

### 方式 3: Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn python-multipart

COPY scripts/ ./scripts/
COPY api/ ./api/

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t pptx-expert .
docker run -p 8000:8000 pptx-expert
```

## 🔧 Custom GPT 配置步骤

### 1. 创建 Custom GPT

1. 访问 https://chat.openai.com/gpts
2. 点击 "Create a GPT"
3. 配置基本信息：
   - **Name**: PPTX Expert
   - **Description**: Professional PowerPoint creator
   - **Instructions**: 复制 PPTX_Expert_GPT_Instructions.md 内容

### 2. 配置 Actions

1. 点击 "Create new action"
2. 选择 "Import from URL"
3. 输入你的 API URL: `https://your-domain.com/openapi.json`
4. 配置认证：
   - **Type**: API Key
   - **Header**: `X-API-Key`

### 3. 上传知识库

上传以下文件到 GPT 的知识库：
- README.md
- SKILL.md
- 使用示例

### 4. 测试

在对话中测试：
```
帮我创建一个关于 AI 的 PPT
显示可用模板
检查这页幻灯片的质量
```

## 🔐 安全配置

### API 认证

```python
# 在 API 中添加认证中间件
@app.middleware("http")
async def authenticate(request: Request, call_next):
    api_key = request.headers.get("X-API-Key")
    if api_key != os.getenv("API_KEY"):
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})
    return await call_next(request)
```

### 环境变量

```bash
# .env
API_KEY=your-secret-key
UPLOAD_DIR=/tmp/uploads
MAX_FILE_SIZE=52428800  # 50MB
```

## 📊 监控

### 日志

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### 指标

- API 响应时间
- 错误率
- 请求量

## 🚀 生产环境建议

1. **使用 HTTPS** - 必须
2. **设置速率限制** - 防止滥用
3. **文件清理** - 定期清理临时文件
4. **备份模板** - 定期备份用户模板
5. **错误追踪** - 使用 Sentry 等工具
