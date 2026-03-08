#!/usr/bin/env python3
"""
Configuration management for PPTX Skill.
Supports environment variables, config files, and defaults.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

# Default configuration
DEFAULTS = {
    # Paths
    'template_dir': str(Path.home() / '.openclaw' / 'skills' / 'pptx' / 'templates'),
    'output_dir': str(Path.cwd()),
    'cache_dir': str(Path.home() / '.cache' / 'pptx-skill'),
    
    # Template settings
    'default_template': None,
    'auto_detect_logo': True,
    'preserve_master_background': True,
    
    # Design settings
    'default_font_heading': 'Arial',
    'default_font_body': 'Calibri',
    'default_font_size_title': 44,
    'default_font_size_heading': 32,
    'default_font_size_body': 18,
    'default_font_size_caption': 12,
    
    # Layout settings
    'default_margin': 0.5,  # inches
    'default_line_spacing': 1.2,
    'logo_position': 'top_right',  # top_left, top_right, bottom_left, bottom_right
    'logo_size': 0.8,  # inches
    
    # Quality settings
    'min_contrast_ratio': 4.5,  # WCAG AA standard
    'enable_design_check': True,
    'auto_fix_overflow': True,
    
    # AI settings
    'enable_ai_enhancement': False,
    'ai_model': None,
    'ai_api_key': None,
    
    # Output settings
    'output_format': 'pptx',  # pptx, pdf
    'compression_level': 'normal',  # low, normal, high
    'include_notes': False,
    
    # Logging
    'log_level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    'log_file': None,
}

class Config:
    """Configuration manager with layered settings."""
    
    def __init__(self, config_file: Optional[str] = None):
        self._config: Dict[str, Any] = DEFAULTS.copy()
        self._config_file = config_file or self._find_config_file()
        self._load_config_file()
        self._load_env_vars()
    
    def _find_config_file(self) -> Optional[str]:
        """Find config file in standard locations."""
        locations = [
            Path.home() / '.pptx-skill' / 'config.json',
            Path.cwd() / '.pptx-skill.json',
            Path.home() / '.openclaw' / 'skills' / 'pptx' / 'config.json',
        ]
        for loc in locations:
            if loc.exists():
                return str(loc)
        return None
    
    def _load_config_file(self):
        """Load configuration from file."""
        if self._config_file:
            try:
                with open(self._config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    self._config.update(file_config)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
    
    def _load_env_vars(self):
        """Override with environment variables."""
        env_mapping = {
            'PPTX_SKILL_TEMPLATE_DIR': 'template_dir',
            'PPTX_SKILL_OUTPUT_DIR': 'output_dir',
            'PPTX_SKILL_DEFAULT_TEMPLATE': 'default_template',
            'PPTX_SKILL_LOG_LEVEL': 'log_level',
            'PPTX_SKILL_AI_MODEL': 'ai_model',
            'PPTX_SKILL_AI_API_KEY': 'ai_api_key',
        }
        for env_var, config_key in env_mapping.items():
            value = os.environ.get(env_var)
            if value:
                self._config[config_key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value."""
        self._config[key] = value
    
    def save(self, path: Optional[str] = None):
        """Save current configuration to file."""
        save_path = path or self._config_file or str(Path.home() / '.pptx-skill' / 'config.json')
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(self._config, f, indent=2)
    
    def __getitem__(self, key: str) -> Any:
        return self._config[key]
    
    def __contains__(self, key: str) -> bool:
        return key in self._config

# Global config instance
config = Config()

def get_config() -> Config:
    """Get global configuration instance."""
    return config

if __name__ == '__main__':
    # Print current configuration
    import json
    print(json.dumps(config._config, indent=2))
