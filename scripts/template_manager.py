#!/usr/bin/env python3
"""
Template Manager - Save, list, load, and apply PowerPoint templates.
Templates are stored as JSON with all design settings.
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

TEMPLATE_DIR = Path.home() / '.openclaw' / 'skills' / 'pptx' / 'templates'

def ensure_template_dir():
    """Ensure template directory exists."""
    TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
    (TEMPLATE_DIR / 'assets').mkdir(exist_ok=True)
    return TEMPLATE_DIR

def save_template(pptx_path, name=None, description=None):
    """
    Save a PPTX file as a reusable template.
    Returns template info dict.
    """
    pptx_path = Path(pptx_path)
    
    if not pptx_path.exists():
        return {'error': f'File not found: {pptx_path}'}
    
    ensure_template_dir()
    
    # Generate template name from filename if not provided
    if not name:
        name = pptx_path.stem.replace('_', ' ').replace('-', ' ').title()
    
    template_id = name.lower().replace(' ', '_').replace('.', '')
    timestamp = datetime.now().isoformat()
    
    # Copy PPTX to templates folder
    template_pptx = TEMPLATE_DIR / f'{template_id}.pptx'
    shutil.copy2(pptx_path, template_pptx)
    
    # Analyze template
    from analyze_template import analyze_template
    analysis = analyze_template(str(pptx_path))
    
    # Create template metadata
    template_info = {
        'id': template_id,
        'name': name,
        'description': description or f'Template from {pptx_path.name}',
        'source_file': pptx_path.name,
        'created_at': timestamp,
        'pptx_file': f'{template_id}.pptx',
        'slide_count': analysis.get('slide_count', 0),
        'layout_count': analysis.get('layout_count', 0),
        'master_count': analysis.get('master_count', 0),
        'layouts': analysis.get('layouts', []),
        'masters': analysis.get('masters', []),
        'theme_colors': analysis.get('theme_colors', {}),
        'theme_fonts': analysis.get('theme_fonts', {}),
        'sample_colors': analysis.get('sample_colors', {}),
    }
    
    # Save template JSON
    template_json = TEMPLATE_DIR / f'{template_id}.json'
    with open(template_json, 'w', encoding='utf-8') as f:
        json.dump(template_info, f, indent=2, default=str)
    
    # Copy any logo images from the PPTX
    try:
        import zipfile
        with zipfile.ZipFile(pptx_path, 'r') as zf:
            for name in zf.namelist():
                if 'image' in name.lower() and ('logo' in name.lower() or 'master' in name.lower()):
                    ext = Path(name).suffix
                    if ext in ['.png', '.jpg', '.jpeg', '.svg']:
                        asset_name = f'{template_id}_logo{ext}'
                        asset_path = TEMPLATE_DIR / 'assets' / asset_name
                        with open(asset_path, 'wb') as img_f:
                            img_f.write(zf.read(name))
                        template_info['logo_file'] = f'assets/{asset_name}'
                        break
    except Exception:
        pass
    
    # Update JSON with logo info
    with open(template_json, 'w', encoding='utf-8') as f:
        json.dump(template_info, f, indent=2, default=str)
    
    return template_info

def list_templates():
    """List all available templates."""
    ensure_template_dir()
    
    templates = []
    for json_file in TEMPLATE_DIR.glob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                template = json.load(f)
                templates.append(template)
        except Exception:
            pass
    
    return sorted(templates, key=lambda x: x.get('created_at', ''), reverse=True)

def get_template(template_id_or_name):
    """Get a specific template by ID or name."""
    ensure_template_dir()
    
    # Try exact ID match
    template_json = TEMPLATE_DIR / f'{template_id_or_name}.json'
    if template_json.exists():
        with open(template_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    # Try fuzzy match
    for json_file in TEMPLATE_DIR.glob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                template = json.load(f)
                if template_id_or_name.lower() in template.get('id', '').lower() or \
                   template_id_or_name.lower() in template.get('name', '').lower():
                    return template
        except Exception:
            pass
    
    return None

def delete_template(template_id):
    """Delete a template."""
    ensure_template_dir()
    
    template_json = TEMPLATE_DIR / f'{template_id}.json'
    template_pptx = TEMPLATE_DIR / f'{template_id}.pptx'
    
    deleted = []
    
    if template_json.exists():
        template_json.unlink()
        deleted.append(str(template_json))
    
    if template_pptx.exists():
        template_pptx.unlink()
        deleted.append(str(template_pptx))
    
    # Delete associated assets
    for asset in TEMPLATE_DIR.glob(f'{template_id}_logo*'):
        asset.unlink()
        deleted.append(str(asset))
    
    return deleted

def get_template_pptx_path(template_id):
    """Get the full path to a template's PPTX file."""
    pptx_path = TEMPLATE_DIR / f'{template_id}.pptx'
    if pptx_path.exists():
        return str(pptx_path)
    return None

def main():
    parser = argparse.ArgumentParser(description='Manage PowerPoint templates')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Save command
    save_parser = subparsers.add_parser('save', help='Save a PPTX as template')
    save_parser.add_argument('input', help='Input PPTX file')
    save_parser.add_argument('--name', '-n', help='Template name')
    save_parser.add_argument('--description', '-d', help='Template description')
    
    # List command
    subparsers.add_parser('list', help='List all templates')
    
    # Get command
    get_parser = subparsers.add_parser('get', help='Get template details')
    get_parser.add_argument('template_id', help='Template ID or name')
    
    # Delete command
    del_parser = subparsers.add_parser('delete', help='Delete a template')
    del_parser.add_argument('template_id', help='Template ID')
    
    # Path command (get PPTX path)
    path_parser = subparsers.add_parser('path', help='Get template PPTX path')
    path_parser.add_argument('template_id', help='Template ID')
    
    args = parser.parse_args()
    
    if args.command == 'save':
        result = save_template(args.input, args.name, args.description)
        if 'error' in result:
            print(f"❌ Error: {result['error']}")
            return 1
        print(f"✅ Template saved: {result['name']}")
        print(f"   ID: {result['id']}")
        print(f"   Slides: {result['slide_count']}")
        print(f"   Layouts: {result['layout_count']}")
        if result.get('logo_file'):
            print(f"   Logo: {result['logo_file']}")
        return 0
    
    elif args.command == 'list':
        templates = list_templates()
        if not templates:
            print("📭 No templates found")
            return 0
        
        print(f"\n📁 Available Templates ({len(templates)}):\n")
        for t in templates:
            print(f"  📽️  {t['name']}")
            print(f"      ID: {t['id']}")
            print(f"      Slides: {t['slide_count']} | Layouts: {t['layout_count']}")
            if t.get('theme_fonts', {}).get('heading'):
                print(f"      Fonts: {t['theme_fonts']['heading']} / {t['theme_fonts'].get('body', 'N/A')}")
            print(f"      Created: {t.get('created_at', 'N/A')[:10]}")
            print()
        return 0
    
    elif args.command == 'get':
        template = get_template(args.template_id)
        if not template:
            print(f"❌ Template not found: {args.template_id}")
            return 1
        print(json.dumps(template, indent=2, default=str))
        return 0
    
    elif args.command == 'delete':
        deleted = delete_template(args.template_id)
        if not deleted:
            print(f"❌ Template not found: {args.template_id}")
            return 1
        print(f"✅ Deleted: {', '.join(deleted)}")
        return 0
    
    elif args.command == 'path':
        path = get_template_pptx_path(args.template_id)
        if not path:
            print(f"❌ Template not found: {args.template_id}")
            return 1
        print(path)
        return 0
    
    else:
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())
