# PPTX Expert - Custom GPT 配置

完整设置步骤与可粘贴的 Instructions 见项目根目录：**CUSTOM_GPT_INTEGRATION.md**。

## 简要配置

- **Name**: PPTX Expert
- **Description**: Create professional PowerPoint (PPT/PPTX) from topics, outlines, or templates. Uses API to generate and download files.
- **Instructions**: 从 SETUP_AND_INSTRUCTIONS.md 第二节整段复制到 GPT 的 Instructions。
- **Actions**: Import schema from `https://qingjingxin.org/playground/ppt-expert-api/openapi.json`，认证方式 API Key，Header `X-API-Key`。

## 指令要点（与 SETUP_AND_INSTRUCTIONS 一致）

- 用户只要提出创建 PPT/PPTX（任意表述），必须调用 **createPresentation** Action，不要只回复文字步骤。
- 可选：先 **listTemplates** 再 createPresentation；上传模板用 **uploadTemplate**；内容检查用 **qualityCheck**；布局建议用 **recommendLayout**。
- 创建成功后必须提供下载链接：`https://qingjingxin.org/playground/ppt-expert-api` + 返回的 `download_url`。
