# Custom GPT Integration Guide

Connect PPTX Expert to ChatGPT Custom GPT via **Actions**. When users ask to create a PPT/PPTX, the GPT calls the API and returns a download link.

---

## Add to Your Existing Custom GPT (qingjingxin.org deployment)

You have the API deployed at **https://qingjingxin.org/playground/ppt-expert-api/**. Add one Action to your **existing** Custom GPT and optionally update Instructions so the GPT uses it for PPT creation.

### Steps

1. Open your Custom GPT → **Configure** → **Actions** → **Create new action**.
2. **Import from URL**: paste
   ```
   https://qingjingxin.org/playground/ppt-expert-api/openapi.json
   ```
3. **Authentication**:
   - Type: **API Key**
   - Auth Type: **Custom**
   - Header Name: `X-API-Key`
   - API Key: use the key in the “API Key (self-use)” section below.
4. Save.
5. In **Instructions**, add (or merge with your existing instructions):
   - When the user wants to create a PPT/PPTX, you must call the **createPresentation** Action and, on success, give the download link: `https://qingjingxin.org/playground/ppt-expert-api` + the response `download_url`.
   - For full Instructions, copy the entire “Section 2: Instructions” block below, or merge it with your current instructions.

### API Key (self-use)

The key below is for your own deployment on qingjingxin.org. Do not share it or commit it to a public repo.

```
ppt-expert-qjx-8f3e2a1b9c4d5e6f
```

- **In Custom GPT**: Paste the full string above into the Action’s API Key field.
- **On the server**: Add `API_KEY=ppt-expert-qjx-8f3e2a1b9c4d5e6f` to the `.env` in the API directory (e.g. `/opt/ppt-expert-api` or its `api/` subdir), then run `sudo systemctl restart ppt-expert-api`. Only requests with this key will be accepted; if `API_KEY` is not set, the API does not enforce auth.

### Schema input box is empty?

- **When using “Import from URL”**: ChatGPT fetches the schema and uses it to build the Action, but the JSON often **does not appear in the schema text box**. That is normal. If, after saving, a test like “Help me make a PPT” causes the GPT to call createPresentation, the schema is working.
- **If import fails (e.g. 404)**: Use **manual paste**. Do not use Import from URL; instead paste the full contents of this repo’s `api/openapi.json` into the Schema input box (from GitHub or your local copy).

---

## Section 1: Create a New Custom GPT from Scratch

### 1. Create the Custom GPT

1. Go to https://chat.openai.com/gpts → **Create**.
2. Under **Configure**, fill in:

| Field | Value |
|-------|--------|
| **Name** | `PPTX Expert` (or your choice) |
| **Description** | `Create professional PowerPoint (PPT/PPTX) from topics, outlines, or templates. Uses API to generate and download files.` |
| **Instructions** | Paste the full “Section 2: Instructions” block below. |

### 2. Configure Actions (required)

1. **Create new action** → **Import from URL**: `https://qingjingxin.org/playground/ppt-expert-api/openapi.json` (for local dev you can use `http://localhost:8000/openapi.json`).
2. **Authentication**: Type **API Key**, Auth Type **Custom**, Header Name `X-API-Key`, API Key from the “API Key (self-use)” section above or matching the server’s `API_KEY`.
3. Save the Action.

### 3. Knowledge base (optional)

You can upload `README.md`, `SKILL.md`, etc., so the GPT understands capabilities and limits.

### 4. Privacy policy (required for publishing)

Custom GPT requires a privacy policy URL. Use:

**https://qingjingxin.org/playground/ppt-expert-api/privacy-policy.html**

The page is served by the PPTX Expert API and covers use of the API and Custom GPT.

### 5. Publish

Choose **Only me** or **Anyone with a link**, then save and publish.

---

## Section 2: Instructions (paste into Custom GPT)

Copy the entire block below into the Custom GPT **Instructions** field:

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

## Section 3: Production environment and auth

| Item | Value |
|------|--------|
| **API base URL** | `https://qingjingxin.org/playground/ppt-expert-api` |
| **OpenAPI Schema** | `https://qingjingxin.org/playground/ppt-expert-api/openapi.json` |
| **Auth** | Header `X-API-Key`; value must match the server’s PPTX Expert API `API_KEY`. |
| **401** | Check that the API Key in the Custom GPT Action matches the server. |

---

## Section 4: Quick check

In the Custom GPT, send:

- “Help me make an 8‑slide PPT about artificial intelligence.”

Expected: the GPT calls `createPresentation`, then returns the filename, slide count, and download link (`https://qingjingxin.org/playground/ppt-expert-api/presentations/download/...`).

---

## Reference: Architecture and API summary

```
ChatGPT UI → Custom GPT (Actions) → PPTX Expert API (FastAPI) → Python scripts
                                        ↑
                                 OpenAPI / openapi.json
```

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/presentations/create` | POST | Create PPTX (title required; topic, slides, outline, template_id optional) |
| `/presentations/download/{filename}` | GET | Download generated file |
| `/templates/list` | GET | List templates |
| `/templates/upload` | POST | Upload and save template |
| `/content/quality-check` | POST | Content quality check (title, bullets) |
| `/content/recommend-layout` | POST | Layout recommendation (title, bullets) |
| `/design/presets` | GET | Design/color presets |
| `/health` | GET | Health check |

---

## FAQ

- **Custom GPT doesn’t call the Action?** Confirm Instructions are pasted and the schema was imported from the URL without errors.
- **401 Unauthorized?** Ensure the Action’s API Key matches the server’s `API_KEY`.
- **API timeout?** Increase `proxy_read_timeout` (and related timeouts) in Nginx or your proxy.

---

## Resources

- [OpenAI Actions](https://platform.openai.com/docs/actions)
- [OpenAPI Specification](https://swagger.io/specification/)
- API docs: https://qingjingxin.org/playground/ppt-expert-api/docs
