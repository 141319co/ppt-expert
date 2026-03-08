#!/usr/bin/env python3
"""
Professional design presets for enterprise-grade presentations.
Includes color palettes, typography, and layout configurations.
"""

from pptx.dml.color import RGBColor
from typing import Dict, List, Any

# Professional Color Palettes
COLOR_PALETTES = {
    'corporate_blue': {
        'name': 'Corporate Blue',
        'description': 'Professional blue palette for business presentations',
        'primary': RGBColor(0, 51, 102),      # Deep Navy
        'secondary': RGBColor(0, 102, 153),   # Ocean Blue
        'accent': RGBColor(255, 102, 0),      # Vibrant Orange
        'background': RGBColor(255, 255, 255),
        'text': RGBColor(33, 33, 33),
        'text_light': RGBColor(102, 102, 102),
        'success': RGBColor(0, 128, 0),
        'warning': RGBColor(255, 165, 0),
        'error': RGBColor(204, 0, 0),
    },
    'modern_tech': {
        'name': 'Modern Tech',
        'description': 'Contemporary palette for technology companies',
        'primary': RGBColor(26, 26, 46),      # Dark Purple
        'secondary': RGBColor(91, 33, 121),   # Purple
        'accent': RGBColor(0, 212, 255),      # Cyan
        'background': RGBColor(250, 250, 252),
        'text': RGBColor(26, 26, 46),
        'text_light': RGBColor(100, 100, 120),
        'success': RGBColor(0, 200, 100),
        'warning': RGBColor(255, 180, 0),
        'error': RGBColor(255, 80, 80),
    },
    'executive_gold': {
        'name': 'Executive Gold',
        'description': 'Elegant gold palette for executive presentations',
        'primary': RGBColor(30, 30, 30),      # Charcoal
        'secondary': RGBColor(184, 134, 11),  # Gold
        'accent': RGBColor(218, 165, 32),     # Goldenrod
        'background': RGBColor(255, 255, 255),
        'text': RGBColor(30, 30, 30),
        'text_light': RGBColor(100, 100, 100),
        'success': RGBColor(0, 128, 0),
        'warning': RGBColor(200, 150, 0),
        'error': RGBColor(180, 0, 0),
    },
    'healthcare_green': {
        'name': 'Healthcare Green',
        'description': 'Calming green palette for healthcare/wellness',
        'primary': RGBColor(0, 102, 51),      # Forest Green
        'secondary': RGBColor(0, 153, 76),    # Medium Green
        'accent': RGBColor(102, 204, 153),    # Mint
        'background': RGBColor(245, 250, 245),
        'text': RGBColor(30, 50, 40),
        'text_light': RGBColor(100, 120, 110),
        'success': RGBColor(0, 150, 50),
        'warning': RGBColor(255, 180, 50),
        'error': RGBColor(200, 50, 50),
    },
    'startup_purple': {
        'name': 'Startup Purple',
        'description': 'Vibrant purple for startups and creative agencies',
        'primary': RGBColor(102, 0, 153),     # Deep Purple
        'secondary': RGBColor(153, 51, 204),  # Purple
        'accent': RGBColor(255, 0, 153),      # Magenta
        'background': RGBColor(255, 255, 255),
        'text': RGBColor(40, 20, 50),
        'text_light': RGBColor(100, 80, 110),
        'success': RGBColor(0, 200, 100),
        'warning': RGBColor(255, 150, 0),
        'error': RGBColor(255, 50, 80),
    },
    'minimal_dark': {
        'name': 'Minimal Dark',
        'description': 'Dark theme for modern presentations',
        'primary': RGBColor(255, 255, 255),   # White
        'secondary': RGBColor(200, 200, 200), # Light Gray
        'accent': RGBColor(0, 180, 255),      # Bright Blue
        'background': RGBColor(30, 30, 30),
        'text': RGBColor(255, 255, 255),
        'text_light': RGBColor(180, 180, 180),
        'success': RGBColor(0, 200, 100),
        'warning': RGBColor(255, 180, 50),
        'error': RGBColor(255, 80, 80),
    },
}

# Typography Presets
TYPOGRAPHY = {
    'corporate': {
        'heading': 'Arial',
        'heading_bold': 'Arial Bold',
        'body': 'Arial',
        'body_light': 'Arial',
        'monospace': 'Consolas',
    },
    'modern': {
        'heading': 'Segoe UI',
        'heading_bold': 'Segoe UI Semibold',
        'body': 'Segoe UI',
        'body_light': 'Segoe UI Light',
        'monospace': 'Consolas',
    },
    'elegant': {
        'heading': 'Georgia',
        'heading_bold': 'Georgia Bold',
        'body': 'Calibri',
        'body_light': 'Calibri Light',
        'monospace': 'Consolas',
    },
    'tech': {
        'heading': 'Roboto',
        'heading_bold': 'Roboto Bold',
        'body': 'Roboto',
        'body_light': 'Roboto Light',
        'monospace': 'Roboto Mono',
    },
}

# Font Size Scale (in points)
FONT_SIZES = {
    'title': 44,
    'heading_1': 36,
    'heading_2': 28,
    'heading_3': 24,
    'body_large': 20,
    'body': 18,
    'body_small': 16,
    'caption': 12,
    'footnote': 10,
}

# Layout Templates
LAYOUT_PRESETS = {
    'title_slide': {
        'title_y': 2.0,
        'title_size': 'title',
        'subtitle_y': 3.5,
        'subtitle_size': 'body_large',
        'show_logo': True,
    },
    'section_divider': {
        'full_background': True,
        'title_size': 'heading_1',
        'title_color': 'background',  # Inverted
        'centered': True,
    },
    'content_standard': {
        'title_y': 0.3,
        'content_y': 1.3,
        'content_width': 9.0,
        'content_height': 4.5,
        'bullet_level_indent': 0.3,
    },
    'two_column': {
        'left_x': 0.5,
        'left_width': 4.25,
        'right_x': 5.0,
        'right_width': 4.25,
        'gutter': 0.5,
    },
    'image_left': {
        'image_x': 0.5,
        'image_width': 4.5,
        'content_x': 5.25,
        'content_width': 4.0,
    },
    'image_right': {
        'content_x': 0.5,
        'content_width': 4.0,
        'image_x': 4.75,
        'image_width': 4.5,
    },
    'stat_callout': {
        'stat_size': 72,
        'stat_color': 'primary',
        'label_size': 'body',
        'label_color': 'text_light',
    },
}

# Chart Style Presets
CHART_STYLES = {
    'corporate': {
        'colors': ['003366', '006699', '0099CC', '33B5E5', '66CCEE'],
        'background': 'FFFFFF',
        'grid_color': 'E0E0E0',
        'text_color': '333333',
        'show_legend': True,
        'legend_position': 'bottom',
        'rounded_corners': True,
    },
    'modern': {
        'colors': ['1A1A2E', '5B2179', '9D4EDD', 'C77DFF', 'E0AAFF'],
        'background': 'FAFAFC',
        'grid_color': 'F0F0F5',
        'text_color': '1A1A2E',
        'show_legend': True,
        'legend_position': 'right',
        'rounded_corners': True,
    },
    'minimal': {
        'colors': ['2D2D2D', '5C5C5C', '8C8C8C', 'BCBCBC', 'ECECEC'],
        'background': 'FFFFFF',
        'grid_color': 'F5F5F5',
        'text_color': '2D2D2D',
        'show_legend': False,
        'legend_position': None,
        'rounded_corners': False,
    },
}

# Design Rules
DESIGN_RULES = {
    'min_contrast_ratio': 4.5,  # WCAG AA
    'max_lines_per_slide': 6,
    'max_words_per_bullet': 14,
    'min_font_size': 12,
    'title_min_size': 36,
    'margin_min': 0.5,  # inches
    'spacing_consistent': True,
    'alignment_consistent': True,
}

def get_palette(palette_name: str) -> Dict[str, Any]:
    """Get color palette by name."""
    return COLOR_PALETTES.get(palette_name, COLOR_PALETTES['corporate_blue'])

def get_typography(style_name: str) -> Dict[str, str]:
    """Get typography preset by name."""
    return TYPOGRAPHY.get(style_name, TYPOGRAPHY['corporate'])

def get_chart_style(style_name: str) -> Dict[str, Any]:
    """Get chart style by name."""
    return CHART_STYLES.get(style_name, CHART_STYLES['corporate'])

def validate_contrast(color1: RGBColor, color2: RGBColor) -> float:
    """Calculate contrast ratio between two colors."""
    def luminance(c: RGBColor) -> float:
        def adjust(v: int) -> float:
            v = v / 255.0
            return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
        
        r, g, b = adjust(c.r), adjust(c.g), adjust(c.b)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    l1 = luminance(color1)
    l2 = luminance(color2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    
    return (lighter + 0.05) / (darker + 0.05)

if __name__ == '__main__':
    import json
    
    print("Available Color Palettes:")
    for name, palette in COLOR_PALETTES.items():
        print(f"  - {name}: {palette['description']}")
    
    print("\nAvailable Typography:")
    for name, fonts in TYPOGRAPHY.items():
        print(f"  - {name}: {fonts['heading']} / {fonts['body']}")
    
    print("\nDesign Rules:")
    for rule, value in DESIGN_RULES.items():
        print(f"  - {rule}: {value}")
