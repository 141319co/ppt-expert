#!/usr/bin/env python3
"""
AI-powered content enhancement for presentations.
Provides intelligent content expansion, layout recommendations, and quality checks.
"""

import re
from typing import List, Dict, Any, Optional, Tuple

class ContentEnhancer:
    """Enhance presentation content with AI and rules-based intelligence."""
    
    # Content type to layout mapping
    LAYOUT_RECOMMENDATIONS = {
        'introduction': 'title_and_content',
        'overview': 'two_column',
        'key_points': 'content_standard',
        'statistics': 'stat_callout',
        'comparison': 'comparison',
        'timeline': 'timeline',
        'team': 'image_grid',
        'quote': 'quote',
        'data': 'chart',
        'conclusion': 'section_divider',
    }
    
    # Keywords for content type detection
    CONTENT_KEYWORDS = {
        'introduction': ['intro', 'welcome', 'overview', 'agenda', 'outline'],
        'statistics': ['statistic', 'data', 'number', 'percentage', '%', 'growth'],
        'comparison': ['vs', 'versus', 'compare', 'comparison', 'difference'],
        'timeline': ['timeline', 'roadmap', 'schedule', 'phase', 'milestone'],
        'team': ['team', 'member', 'staff', 'employee', 'person'],
        'quote': ['quote', 'testimonial', 'feedback', 'review'],
        'conclusion': ['conclusion', 'summary', 'next steps', 'thank', 'qa'],
    }
    
    def __init__(self, language: str = 'zh'):
        self.language = language
    
    def detect_content_type(self, title: str, bullets: List[str] = None) -> str:
        """Detect content type from title and bullets."""
        text = f"{title} {' '.join(bullets or [])}".lower()
        
        for content_type, keywords in self.CONTENT_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                return content_type
        
        return 'general'
    
    def recommend_layout(self, title: str, bullets: List[str] = None) -> str:
        """Recommend best layout for content."""
        content_type = self.detect_content_type(title, bullets)
        return self.LAYOUT_RECOMMENDATIONS.get(content_type, 'content_standard')
    
    def expand_content(self, bullets: List[str], target_count: int = 4) -> List[str]:
        """Expand bullet points to target count with intelligent suggestions."""
        if len(bullets) >= target_count:
            return bullets[:target_count]
        
        expanded = bullets.copy()
        
        # Generate placeholder suggestions
        suggestions = [
            "Key insight or finding",
            "Supporting data point",
            "Practical implication",
            "Next action item",
        ]
        
        while len(expanded) < target_count and suggestions:
            expanded.append(suggestions.pop(0))
        
        return expanded
    
    def optimize_bullet_text(self, text: str, max_words: int = 14) -> str:
        """Optimize bullet text for readability."""
        words = text.split()
        
        if len(words) <= max_words:
            return text
        
        # Truncate gracefully
        truncated = ' '.join(words[:max_words])
        if truncated[-1] not in '.,;:!?':
            truncated += '...'
        
        return truncated
    
    def generate_slide_notes(self, title: str, bullets: List[str]) -> str:
        """Generate speaker notes from slide content."""
        notes = [f"Slide: {title}\n"]
        
        for i, bullet in enumerate(bullets, 1):
            notes.append(f"• Point {i}: {bullet}")
        
        notes.append("\nKey message: Emphasize the main takeaway from this slide.")
        
        return '\n'.join(notes)
    
    def check_content_quality(self, title: str, bullets: List[str]) -> Dict[str, Any]:
        """Check content quality and return issues."""
        issues = []
        suggestions = []
        
        # Check title length
        if len(title) > 50:
            issues.append(f"Title too long ({len(title)} chars)")
            suggestions.append("Consider shortening title to <50 characters")
        
        # Check bullet count
        if len(bullets) > 6:
            issues.append(f"Too many bullets ({len(bullets)})")
            suggestions.append("Limit to 4-6 bullets per slide")
        
        # Check bullet length
        for i, bullet in enumerate(bullets):
            if len(bullet) > 100:
                issues.append(f"Bullet {i+1} too long")
                suggestions.append("Keep bullets concise (<100 characters)")
        
        # Check for empty content
        if not bullets:
            issues.append("No bullet points")
            suggestions.append("Add 3-5 key points")
        
        # Check for single bullet
        if len(bullets) == 1:
            suggestions.append("Consider adding more supporting points")
        
        return {
            'issues': issues,
            'suggestions': suggestions,
            'score': max(0, 100 - len(issues) * 15),
        }
    
    def suggest_improvements(self, title: str, bullets: List[str]) -> List[str]:
        """Suggest specific improvements for slide content."""
        suggestions = []
        
        # Content suggestions
        if len(bullets) < 3:
            suggestions.append("Add more supporting details")
        
        if all(len(b) < 20 for b in bullets):
            suggestions.append("Consider adding data or examples")
        
        # Structure suggestions
        if not any(b.endswith('.') for b in bullets):
            suggestions.append("Use consistent punctuation (all with or without periods)")
        
        if any(b[0].islower() for b in bullets if b):
            suggestions.append("Start all bullets with capital letters")
        
        # Visual suggestions
        layout = self.recommend_layout(title, bullets)
        if layout == 'content_standard' and len(bullets) > 4:
            suggestions.append("Consider splitting into two slides")
        
        return suggestions
    
    def format_for_presentation(self, content: str) -> Dict[str, Any]:
        """Parse and format raw content for presentation."""
        lines = content.strip().split('\n')
        
        result = {
            'title': '',
            'subtitle': '',
            'bullets': [],
            'notes': '',
        }
        
        for line in lines:
            line = line.strip()
            
            if not line:
                continue
            
            if line.startswith('# '):
                result['title'] = line[2:].strip()
            elif line.startswith('## '):
                if result['title']:
                    # New slide
                    pass
                result['title'] = line[3:].strip()
            elif line.startswith('- '):
                result['bullets'].append(self.optimize_bullet_text(line[2:]))
            elif not result['title']:
                result['title'] = line
            else:
                result['bullets'].append(self.optimize_bullet_text(line))
        
        # Generate notes
        if result['title'] and result['bullets']:
            result['notes'] = self.generate_slide_notes(result['title'], result['bullets'])
        
        return result

def enhance_outline(outline: str) -> str:
    """Enhance a markdown outline with AI suggestions."""
    enhancer = ContentEnhancer()
    
    # Parse slides
    slides = []
    current_slide = {'title': '', 'bullets': []}
    
    for line in outline.split('\n'):
        line = line.strip()
        
        if line.startswith('## '):
            if current_slide['title']:
                slides.append(current_slide)
            current_slide = {'title': line[3:].strip(), 'bullets': []}
        elif line.startswith('- '):
            current_slide['bullets'].append(line[2:].strip())
    
    if current_slide['title']:
        slides.append(current_slide)
    
    # Enhance each slide
    enhanced = []
    for slide in slides:
        layout = enhancer.recommend_layout(slide['title'], slide['bullets'])
        quality = enhancer.check_content_quality(slide['title'], slide['bullets'])
        
        enhanced.append({
            'title': slide['title'],
            'bullets': slide['bullets'],
            'layout': layout,
            'quality_score': quality['score'],
            'suggestions': quality['suggestions'],
        })
    
    return enhanced

if __name__ == '__main__':
    enhancer = ContentEnhancer()
    
    # Test content detection
    test_cases = [
        ("Introduction", ["Welcome", "Agenda"]),
        ("Q4 Statistics", ["Growth: 25%", "Revenue: $10M"]),
        ("Product Comparison", ["Product A vs Product B"]),
        ("Next Steps", ["Conclusion", "Q&A"]),
    ]
    
    print("Content Type Detection:")
    for title, bullets in test_cases:
        content_type = enhancer.detect_content_type(title, bullets)
        layout = enhancer.recommend_layout(title, bullets)
        print(f"  {title}: {content_type} → {layout}")
    
    print("\nQuality Check Example:")
    quality = enhancer.check_content_quality(
        "Very Long Title That Exceeds Recommended Length",
        ["Short", "Also short", "This is a very long bullet point that exceeds the recommended maximum word count and should be truncated"]
    )
    print(f"  Score: {quality['score']}/100")
    print(f"  Issues: {quality['issues']}")
    print(f"  Suggestions: {quality['suggestions']}")
