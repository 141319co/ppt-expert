#!/usr/bin/env python3
"""
Interactive template selector for PowerPoint creation.
Presents available templates and lets user choose one.
"""

import sys
import json
from pathlib import Path
from template_manager import list_templates, get_template

def display_templates():
    """Display available templates in a user-friendly format."""
    templates = list_templates()
    
    if not templates:
        print("\n📭 暂无保存的模板")
        print("\n💡 提示：使用以下命令保存模板:")
        print("   python3 template_manager.py save your_template.pptx --name \"模板名称\"")
        return None
    
    print("\n" + "=" * 60)
    print("📁 可用的 PowerPoint 模板")
    print("=" * 60 + "\n")
    
    for i, t in enumerate(templates, 1):
        print(f"{i}. 📽️  {t['name']}")
        print(f"   ID: {t['id']}")
        print(f"   描述：{t.get('description', '无描述')}")
        print(f"   幻灯片：{t.get('slide_count', 0)} | 布局：{t.get('layout_count', 0)}")
        
        # 字体信息
        fonts = t.get('theme_fonts', {})
        if fonts:
            print(f"   字体：{fonts.get('heading', 'N/A')} / {fonts.get('body', 'N/A')}")
        
        # 颜色信息
        colors = t.get('sample_colors', {}).get('most_used', [])
        if colors:
            color_preview = ' | '.join([f'#{c}' if not c.startswith('#') else c for c in colors[:3]])
            print(f"   主色：{color_preview}")
        
        # Logo 信息
        if t.get('logo_file'):
            print(f"   ✅ 包含 Logo")
        
        print()
    
    return templates

def select_template(templates, auto_select_first=False):
    """Let user select a template."""
    if auto_select_first and len(templates) == 1:
        print(f"\n✅ 自动选择唯一模板：{templates[0]['name']}")
        return templates[0]['id']
    
    if not templates:
        return None
    
    print("请选择模板 (输入编号或 ID，或按 Enter 使用默认模板):")
    choice = input("> ").strip()
    
    if not choice:
        print("使用默认模板 (无模板)")
        return None
    
    # Try number
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(templates):
            selected = templates[idx]
            print(f"\n✅ 已选择：{selected['name']}")
            return selected['id']
    except ValueError:
        pass
    
    # Try ID or name match
    for t in templates:
        if choice.lower() in t['id'].lower() or choice.lower() in t['name'].lower():
            print(f"\n✅ 已选择：{t['name']}")
            return t['id']
    
    print(f"⚠️  未找到匹配的模板：{choice}")
    return None

def quick_select(template_query=None):
    """Quick select template by query or return first match."""
    templates = list_templates()
    
    if not templates:
        return None
    
    if not template_query:
        # Return most recent template
        return templates[0]['id']
    
    # Search by query
    for t in templates:
        if template_query.lower() in t['id'].lower() or \
           template_query.lower() in t['name'].lower() or \
           template_query.lower() in t.get('description', '').lower():
            return t['id']
    
    return None

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Interactive template selector')
    parser.add_argument('--select', '-s', help='Quick select by query')
    parser.add_argument('--auto', action='store_true', help='Auto-select if only one template')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--list', '-l', action='store_true', help='List templates only')
    
    args = parser.parse_args()
    
    if args.list:
        templates = list_templates()
        if args.json:
            print(json.dumps(templates, indent=2, default=str))
        else:
            display_templates()
        return 0
    
    if args.select:
        template_id = quick_select(args.select)
        if template_id:
            if args.json:
                print(json.dumps({'selected': template_id}))
            else:
                print(f"✅ Selected: {template_id}")
            return 0
        else:
            if args.json:
                print(json.dumps({'error': 'No matching template'}))
            else:
                print("❌ No matching template found")
            return 1
    
    # Interactive mode
    templates = display_templates()
    if not templates:
        return 1
    
    selected_id = select_template(templates, args.auto)
    
    if selected_id:
        print(f"\nTemplate ID: {selected_id}")
        return 0
    else:
        print("\nNo template selected")
        return 1

if __name__ == '__main__':
    sys.exit(main())
