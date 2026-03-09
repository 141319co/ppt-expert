#!/usr/bin/env python3
"""
PPTX Expert API - FastAPI service for Custom GPT Actions
"""

import os
import sys
import uuid
import logging
from pathlib import Path
from typing import Optional, List
from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks, Request
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
import uvicorn

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from template_manager import save_template, list_templates, get_template, delete_template
from analyze_template import analyze_template
from content_enhancer import ContentEnhancer

# Configuration
UPLOAD_DIR = Path('/tmp/pptx-uploads')
OUTPUT_DIR = Path('/tmp/pptx-outputs')
TEMPLATE_DIR = Path.home() / '.openclaw' / 'skills' / 'pptx' / 'templates'

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    logger.info("PPTX Expert API starting...")
    yield
    logger.info("PPTX Expert API shutting down...")

app = FastAPI(
    title="PPTX Expert API",
    description="Enterprise PowerPoint generation API for Custom GPT",
    version="1.0.0",
    lifespan=lifespan
)

# Optional API Key auth: if API_KEY env is set, require X-API-Key header to match
API_KEY = os.environ.get("API_KEY")

# Paths that do not require API key (public)
PUBLIC_PATHS = ("/", "/health", "/privacy-policy.html")

@app.middleware("http")
async def optional_api_key_auth(request: Request, call_next):
    if API_KEY and request.url.path not in PUBLIC_PATHS:
        key = request.headers.get("X-API-Key")
        if key != API_KEY:
            return JSONResponse(status_code=401, content={"detail": "Invalid or missing API key"})
    return await call_next(request)

# ============== Models ==============

class CreatePresentationRequest(BaseModel):
    """Request model for creating presentations."""
    title: str = Field(..., description="Presentation title")
    subtitle: Optional[str] = Field(None, description="Subtitle")
    topic: Optional[str] = Field(None, description="Topic for auto-generation")
    slides: Optional[int] = Field(5, description="Number of slides")
    outline: Optional[str] = Field(None, description="Markdown outline")
    template_id: Optional[str] = Field(None, description="Template ID to use")
    output_name: Optional[str] = Field(None, description="Output filename")

class TemplateSaveRequest(BaseModel):
    """Request model for saving templates."""
    name: str = Field(..., description="Template name")
    description: Optional[str] = Field(None, description="Template description")

class ContentQualityRequest(BaseModel):
    """Request model for content quality check."""
    title: str
    bullets: List[str] = []

class LayoutRecommendationRequest(BaseModel):
    """Request model for layout recommendation."""
    title: str
    bullets: List[str] = []

# ============== Endpoints ==============

@app.get("/")
async def root():
    """API health check."""
    return {
        "service": "PPTX Expert API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

# Privacy policy (static page for Custom GPT requirement)
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

@app.get("/privacy-policy.html")
async def privacy_policy():
    """Serve privacy policy page."""
    path = STATIC_DIR / "privacy-policy.html"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Privacy policy not found")
    return FileResponse(path, media_type="text/html")

@app.post("/presentations/create")
async def create_presentation(request: CreatePresentationRequest):
    """
    Create a PowerPoint presentation.
    
    - **title**: Presentation title
    - **subtitle**: Optional subtitle
    - **topic**: Topic for auto-generation
    - **slides**: Number of slides (default: 5)
    - **outline**: Markdown outline
    - **template_id**: Template to use
    """
    try:
        from create_pptx import PresentationCreator, parse_markdown_outline, generate_topic_slides
        
        # Build presentation data
        prs_data = {
            "title": request.title,
            "subtitle": request.subtitle or "",
            "slides": []
        }
        
        if request.outline:
            prs_data = parse_markdown_outline(request.outline)
        elif request.topic:
            prs_data["slides"] = generate_topic_slides(request.topic, request.slides)
        
        # Create presentation
        creator = PresentationCreator()
        output_name = request.output_name or f"presentation_{uuid.uuid4().hex[:8]}.pptx"
        output_path = OUTPUT_DIR / output_name
        
        if request.template_id:
            slide_count = creator.create_with_template(prs_data, request.template_id, str(output_path))
        else:
            slide_count = creator.create_default(prs_data, str(output_path))
        
        return {
            "success": True,
            "file": output_name,
            "path": str(output_path),
            "slides": slide_count,
            "download_url": f"/presentations/download/{output_name}"
        }
    
    except Exception as e:
        logger.error(f"Creation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/presentations/download/{filename}")
async def download_presentation(filename: str):
    """Download a generated presentation."""
    file_path = OUTPUT_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        str(file_path),
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename=filename
    )

@app.post("/templates/upload")
async def upload_template(
    file: UploadFile = File(..., description="PPTX template file"),
    name: Optional[str] = None,
    description: Optional[str] = None
):
    """
    Upload and save a PPTX template.
    
    - **file**: PPTX file to save as template
    - **name**: Template name (optional, defaults to filename)
    - **description**: Template description
    """
    try:
        # Save uploaded file
        temp_path = UPLOAD_DIR / f"temp_{uuid.uuid4().hex}.pptx"
        with open(temp_path, 'wb') as f:
            f.write(await file.read())
        
        # Save as template
        result = save_template(str(temp_path), name, description)
        
        if 'error' in result:
            raise HTTPException(status_code=400, detail=result['error'])
        
        # Cleanup temp file
        temp_path.unlink()
        
        return {
            "success": True,
            "template_id": result['id'],
            "name": result['name'],
            "slides": result['slide_count'],
            "layouts": result['layout_count']
        }
    
    except Exception as e:
        logger.error(f"Template upload failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/templates/list")
async def list_templates_endpoint():
    """List all available templates."""
    templates = list_templates()
    return {
        "count": len(templates),
        "templates": [
            {
                "id": t['id'],
                "name": t['name'],
                "description": t.get('description', ''),
                "slides": t.get('slide_count', 0),
                "layouts": t.get('layout_count', 0)
            }
            for t in templates
        ]
    }

@app.get("/templates/{template_id}")
async def get_template_endpoint(template_id: str):
    """Get template details."""
    template = get_template(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    
    return template

@app.delete("/templates/{template_id}")
async def delete_template_endpoint(template_id: str):
    """Delete a template."""
    deleted = delete_template(template_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Template not found")
    
    return {"success": True, "deleted": deleted}

@app.post("/content/quality-check")
async def quality_check(request: ContentQualityRequest):
    """
    Check content quality and get suggestions.
    
    - **title**: Slide title
    - **bullets**: Bullet points
    """
    enhancer = ContentEnhancer()
    result = enhancer.check_content_quality(request.title, request.bullets)
    return result

@app.post("/content/recommend-layout")
async def recommend_layout(request: LayoutRecommendationRequest):
    """
    Recommend best layout for content.
    
    - **title**: Slide title
    - **bullets**: Bullet points
    """
    enhancer = ContentEnhancer()
    layout = enhancer.recommend_layout(request.title, request.bullets)
    content_type = enhancer.detect_content_type(request.title, request.bullets)
    
    return {
        "content_type": content_type,
        "recommended_layout": layout,
        "suggestions": enhancer.suggest_improvements(request.title, request.bullets)
    }

@app.post("/content/enhance")
async def enhance_content(request: ContentQualityRequest):
    """
    Enhance content with AI suggestions.
    
    - **title**: Slide title
    - **bullets**: Bullet points
    """
    enhancer = ContentEnhancer()
    
    return {
        "optimized_bullets": [
            enhancer.optimize_bullet_text(b) for b in request.bullets
        ],
        "expanded": enhancer.expand_content(request.bullets),
        "notes": enhancer.generate_slide_notes(request.title, request.bullets),
        "suggestions": enhancer.suggest_improvements(request.title, request.bullets)
    }

@app.get("/design/presets")
async def list_design_presets():
    """List available design presets."""
    from design_presets import COLOR_PALETTES, TYPOGRAPHY, CHART_STYLES
    
    return {
        "color_palettes": [
            {"id": k, "name": v['name'], "description": v['description']}
            for k, v in COLOR_PALETTES.items()
        ],
        "typography": list(TYPOGRAPHY.keys()),
        "chart_styles": list(CHART_STYLES.keys())
    }

# ============== Error Handlers ==============

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unexpected error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )

# ============== Main ==============

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
