#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path

POSTS_DIR = Path("/home/frn/.openclaw/shared/VitalWell/posts")
GUIDES_DIR = Path("/home/frn/.openclaw/shared/VitalWell/guides")

def extract_title(html_content):
    match = re.search(r'<title>([^|]+)', html_content)
    if match:
        return match.group(1).strip()
    return "Untitled"

def extract_description(html_content):
    # Try meta description first
    match = re.search(r'<meta name="description" content="([^"]+)"', html_content)
    if match:
        return match.group(1)
    # Fall back to first paragraph
    match = re.search(r'<p>([^<]+)</p>', html_content)
    if match:
        return match.group(1)[:200]
    return "Boldly Balanced article"

def extract_image(html_content):
    # Try og:image first
    match = re.search(r'<meta property="og:image" content="([^"]+)"', html_content)
    if match:
        return match.group(1)
    # Fall back to first img src
    match = re.search(r'src="(https://images[^"]+)"', html_content)
    if match:
        return match.group(1)
    return "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=1200&q=80"

def extract_date(html_content):
    # Look for date pattern
    match = re.search(r'\d{4}-\d{2}-\d{2}', html_content)
    if match:
        return match.group(1)
    # Look for written date
    match = re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})', html_content)
    if match:
        from datetime import datetime
        try:
            dt = datetime.strptime(match.group(1), '%B %d, %Y')
            return dt.strftime('%Y-%m-%d')
        except:
            pass
    return "2026-02-22"

def add_schema_to_file(filepath, url_path):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already has schema
    if 'application/ld+json' in content:
        print(f"Schema already exists in {filepath.name}, skipping")
        return
    
    title = extract_title(content)
    description = extract_description(content)
    image = extract_image(content)
    date = extract_date(content)
    
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description[:200],
        "image": image,
        "author": {
            "@type": "Organization",
            "name": "Boldly Balanced"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Boldly Balanced",
            "logo": {
                "@type": "ImageObject",
                "url": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=200&q=80"
            }
        },
        "datePublished": date,
        "dateModified": date,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://vitalwell.vercel.app/{url_path}"
        }
    }
    
    # Build JSON manually to avoid escaping issues  
    schema_lines = [
        '    <!-- Schema.org Article JSON-LD -->',
        '    <script type="application/ld+json">',
        '    {',
        '      "@context": "https://schema.org",',
        '      "@type": "Article",',
        f'      "headline": "{title}",',
        f'      "description": "{description[:200]}",',
        f'      "image": "{image}",',
        '      "author": {',
        '        "@type": "Organization",',
        '        "name": "Boldly Balanced"',
        '      },',
        '      "publisher": {',
        '        "@type": "Organization",',
        '        "name": "Boldly Balanced",',
        '        "logo": {',
        '          "@type": "ImageObject",',
        '          "url": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=200&q=80"',
        '        }',
        '      },',
        f'      "datePublished": "{date}",',
        f'      "dateModified": "{date}",',
        '      "mainEntityOfPage": {',
        '        "@type": "WebPage",',
        f'        "@id": "https://vitalwell.vercel.app/{url_path}"',
        '      }',
        '    }',
        '    </script>'
    ]
    schema_tag = '\n'.join(schema_lines)
    
    # Insert after <head> tag
    new_content = content.replace('<head>', '<head>\n' + schema_tag, 1)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Added schema to {filepath.name}")

# Process posts
for f in POSTS_DIR.glob("*.html"):
    add_schema_to_file(f, f"posts/{f.name}")

# Process guides
for f in GUIDES_DIR.glob("*.html"):
    add_schema_to_file(f, f"guides/{f.name}")

print("Done!")
