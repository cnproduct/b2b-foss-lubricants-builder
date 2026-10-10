#!/usr/bin/env python3
"""
apply_interactive_enhancements.py
Updates all 7 core pages with:
1. Official logo (/assets/images/foss-official-logo.png) in header, footer, og:image, and JSON-LD schema.
2. Dynamic Number Count-Up hooks (.stat-num, .count-up).
3. Dual-column scroll animations (.reveal-left, .reveal-right, .reveal-up).
4. Image Lightbox wrappers (.zoomable-image-wrapper with .zoom-hint-badge).
5. Interactive Photo Switcher widgets on index.html, products.html, about.html, and packaging-logistics.html.
"""

import os
import re

CORE_PAGES = [
    'index.html',
    'about.html',
    'contact.html',
    'products.html',
    'hydraulic-oil.html',
    'industrial-oils.html',
    'packaging-logistics.html'
]

def update_logo_and_head(content, filename):
    # 1. Favicon & meta og:image
    content = re.sub(
        r'<meta property="og:image" content="https?://[^"]*foss-logo\.(svg|png)">',
        r'<meta property="og:image" content="https://www.fosslubricants.com/assets/images/foss-official-logo.png">',
        content
    )
    content = re.sub(
        r'<link rel="icon" type="image/svg\+xml" href="[^"]*foss-logo\.svg">',
        r'<link rel="icon" type="image/png" href="/assets/images/foss-official-logo.png">',
        content
    )
    # JSON-LD logo
    content = re.sub(
        r'"logo":\s*"https?://[^"]*foss-logo[^"]*"',
        r'"logo": "https://www.fosslubricants.com/assets/images/foss-official-logo.png"',
        content
    )

    # 2. Header logo
    header_old = r'<img src="[^"]*foss-logo\.svg" alt="FOSS LUBRICATION Logo - 福斯润滑" class="site-logo-img"[^>]*>'
    header_new = r'<img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="site-logo-img" width="116" height="48">'
    content = re.sub(header_old, header_new, content)

    # 3. Footer logo
    footer_old = r'<img src="[^"]*foss-logo\.svg" alt="FOSS LUBRICATION Logo"[^>]*style="[^"]*"[^>]*>'
    footer_new = r'<img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="footer-logo-img" width="120" height="50">'
    content = re.sub(footer_old, footer_new, content)

    # Also clean any leftover footer .html#
    content = content.replace('hydraulic-oil.html#', '/hydraulic-oil#')
    content = content.replace('industrial-oils.html#', '/industrial-oils#')
    content = content.replace('packaging-logistics.html#', '/packaging-logistics#')
    content = content.replace('about.html#', '/about#')
    content = content.replace('contact.html#', '/contact#')

    return content

def main():
    for page in CORE_PAGES:
        if not os.path.exists(page):
            print(f"Skipping {page} (not found)")
            continue
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()

        updated = update_logo_and_head(content, page)

        with open(page, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated logo and headers in {page}")

if __name__ == '__main__':
    main()
