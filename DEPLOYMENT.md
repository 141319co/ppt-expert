# 🚀 PPTX Expert 部署指南

## 📋 部署选项

| 方式 | 难度 | 适用场景 |
|------|------|---------|
| Docker | ⭐⭐ | 快速部署 |
| Nginx | ⭐⭐⭐ | 生产环境 |
| systemd | ⭐⭐ | Linux 服务器 |
| Vercel/Railway | ⭐⭐ | 云平台 |

## 🐳 Docker 部署

### 构建镜像

```bash
cd api
docker build -t pptx-expert:1.0.0 .
```

### 运行容器

```bash
docker run -d \
  --name pptx-expert \
  -p 8000:8000 \
  -v /tmp/pptx-outputs:/tmp/pptx-outputs \
  pptx-expert:1.0.0
```

### Docker Compose

```yaml
version: '3.8'

services:
  pptx-expert:
    build: ./api
    ports:
      - "8000:8000"
    volumes:
      - ./outputs:/tmp/pptx-outputs
    restart: unless-stopped
    environment:
      - API_KEY=your-secret-key
```

## 🌐 Nginx 反向代理

### 配置步骤

1. **复制配置文件**

```bash
sudo cp nginx/ppt-expert-api.conf /etc/nginx/conf.d/
```

2. **测试配置**

```bash
sudo nginx -t
```

3. **重载 Nginx**

```bash
sudo systemctl reload nginx
```

4. **验证**

```bash
curl http://your-domain.com/playground/ppt-expert-api/health
```

### 配置说明

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /playground/ppt-expert-api/ {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        client_max_body_size 50M;
    }
}
```

## 🔧 systemd 服务

### 创建服务文件

```bash
sudo cat > /etc/systemd/system/ppt-expert-api.service << 'EOF'
[Unit]
Description=PPTX Expert API Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/path/to/ppt-expert/api
Environment="PATH=/path/to/ppt-expert/api/venv/bin"
ExecStart=/path/to/ppt-expert/api/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
