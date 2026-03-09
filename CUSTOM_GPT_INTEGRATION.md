# Custom GPT 集成指南

将 PPTX Expert 接入 ChatGPT Custom GPT，通过 **Actions** 调用 API，用户说「做 PPT/PPTX」时由 GPT 直接调用接口并返回下载链接。

---

## 加入现有 Custom GPT（你已部署 qingjingxin.org）

你已在 **http://qingjingxin.org/playground/ppt-expert-api/** 部署 API，只需在**现有** Custom GPT 里加一个 Action 并（可选）在 Instructions 里说明用该 Action 做 PPT。

### 步骤

1. 打开你的 Custom GPT → **Configure** → **Actions** → **Create new action**。
2. **Import from URL** 填：
   ```
   https://qingjingxin.org/playground/ppt-expert-api/openapi.json
   ```
3. **Authentication**：
   - Type: **API Key**
   - Auth Type: **Custom**
   - Header Name: `X-API-Key`
   - API Key 填下面「API Key（自用）」里的密钥。
4. 保存。
5. 在 **Instructions** 里加一句（或合并进你原有指令）：
   - 当用户要创建 PPT/PPTX 时，必须调用 **createPresentation** Action，创建成功后给出下载链接：`https://qingjingxin.org/playground/ppt-expert-api` + 返回的 `download_url`。
   - 需要完整 Instructions 可复制下方「二、Instructions」整段，或与你现有指令合并。

### API Key（自用）

下面密钥仅用于你在 qingjingxin.org 上的自用部署；请勿泄露或提交到公开仓库。

```
ppt-expert-qjx-8f3e2a1b9c4d5e6f
```

- **在 Custom GPT 里**：把上面整串填到 Action 的 API Key 框。
- **在服务器上（可选）**：在 API 所在目录的 `.env` 中加一行 `API_KEY=ppt-expert-qjx-8f3e2a1b9c4d5e6f`，重启服务后，未带该 Key 的请求会返回 401。若不设置 `API_KEY`，当前 API 不校验密钥（任何人可调）。

---

## 一、从零创建新 Custom GPT 的步骤

### 1. 创建 Custom GPT

1. 打开 https://chat.openai.com/gpts → **Create**。
2. 在 **Configure** 中填写：

| 字段 | 填写内容 |
|------|----------|
| **Name** | `PPTX Expert`（可自拟） |
| **Description** | `Create professional PowerPoint (PPT/PPTX) from topics, outlines, or templates. Uses API to generate and download files.` |
| **Instructions** | 见下方「二、Instructions」整段复制进去。 |

### 2. 配置 Actions（必做）

1. **Create new action** → **Import from URL** 填：`https://qingjingxin.org/playground/ppt-expert-api/openapi.json`（本地开发可用 `http://localhost:8000/openapi.json`）。
2. **Authentication**：Type **API Key**，Auth Type **Custom**，Header Name `X-API-Key`，API Key 使用上文「API Key（自用）」或与服务器 `API_KEY` 一致。
3. 保存 Action。

### 3. 知识库（可选）

可上传 `README.md`、`SKILL.md` 等，便于 GPT 理解能力边界。

### 4. 发布

选择 **Only me** 或 **Anyone with a link**，保存并发布。

---

## 二、Instructions（复制到 Custom GPT）

将下面整段复制到 Custom GPT 的 **Instructions** 框：

```
You are PPTX Expert, a professional PowerPoint assistant. Your job is to help users create presentations in PPT or PPTX format.

## When to use Actions (required)

Whenever the user wants to create, generate, or make a presentation, deck, or slides in PPT/PPTX format (in any language), you MUST call the PPTX Expert API Actions—do not only describe steps or write outline text without calling the API.

- "做一份PPT" / "生成PPT" / "帮我做演示文稿" → call createPresentation.
- "Create a PowerPoint about X" / "Make slides for X" / "I need a PPTX for X" → call createPresentation.
- "用模板做一个汇报" / "用公司模板" → first listTemplates if needed, then call createPresentation with template_id.

You have these Actions available; use them as follows:

1. **createPresentation** – Use this for every request to create a PPT/PPTX. Required parameters: title. Optional: subtitle, topic, slides (default 5), outline (markdown), template_id. Prefer topic when the user gives a theme; use outline when they provide structure.
2. **listTemplates** – Call when the user asks for templates, wants to pick a template, or says "用模板". Then use a chosen template_id in createPresentation.
3. **uploadTemplate** – Only when the user uploads a PPTX file to save as a template (file + optional name, description).
4. **qualityCheck** – When the user asks to check or improve slide content (title + bullets).
5. **recommendLayout** – When the user asks for layout suggestions for a slide (title + bullets).
6. **listDesignPresets** (GET /design/presets) – When the user asks for design or color presets.

After createPresentation succeeds, always give the user:
- The filename and slide count.
- The download link: https://qingjingxin.org/playground/ppt-expert-api + download_url from the response (e.g. https://qingjingxin.org/playground/ppt-expert-api/presentations/download/<filename>).
- A short note that the file is PPTX and can be opened in PowerPoint.

## Behavior

- If the request is vague (e.g. "做个PPT"), ask: number of slides, topic or outline, and template preference (or suggest listing templates).
- Prefer calling the API once with good parameters over multiple back-and-forth; only ask when essential (e.g. missing title or topic).
- Keep replies concise and actionable; after creating a presentation, offer optional next steps (e.g. quality check, different template, or more slides).
- Tone: professional and friendly.
```

---

## 三、生产环境与认证

| 项 | 值 |
|----|-----|
| **API 根地址** | `https://qingjingxin.org/playground/ppt-expert-api` |
| **OpenAPI Schema** | `https://qingjingxin.org/playground/ppt-expert-api/openapi.json` |
| **认证** | Header `X-API-Key`，值与服务器 PPTX Expert API 的 `API_KEY` 一致。 |
| **401** | 检查 Custom GPT Action 里填写的 API Key 是否正确。 |

---

## 四、快速自检

在 Custom GPT 中发送：

- 「帮我做一份关于人工智能的 PPT，8 页。」

预期：GPT 调用 `createPresentation`，返回文件名、页数和下载链接（`https://qingjingxin.org/playground/ppt-expert-api/presentations/download/...`）。

---

## 参考：架构与 API 摘要

```
ChatGPT UI → Custom GPT (Actions) → PPTX Expert API (FastAPI) → Python scripts
                                        ↑
                                 OpenAPI / openapi.json
```

| 端点 | 方法 | 用途 |
|------|------|------|
| `/presentations/create` | POST | 创建 PPTX（title 必填；topic, slides, outline, template_id 可选） |
| `/presentations/download/{filename}` | GET | 下载生成的文件 |
| `/templates/list` | GET | 列出模板 |
| `/templates/upload` | POST | 上传并保存模板 |
| `/content/quality-check` | POST | 内容质量检查（title, bullets） |
| `/content/recommend-layout` | POST | 布局推荐（title, bullets） |
| `/design/presets` | GET | 设计/配色预设 |
| `/health` | GET | 健康检查 |

---

## 常见问题

- **Custom GPT 不调用 Action？** 确认 Instructions 已粘贴、Schema 从上述 URL 导入且无报错。
- **401 Unauthorized？** 检查 Action 的 API Key 与服务器 `API_KEY` 一致。
- **API 超时？** 服务器端 Nginx/代理可适当提高 `proxy_read_timeout`。

---

## 资源

- [OpenAI Actions](https://platform.openai.com/docs/actions)
- [OpenAPI 规范](https://swagger.io/specification/)
- 项目 API 文档：https://qingjingxin.org/playground/ppt-expert-api/docs
