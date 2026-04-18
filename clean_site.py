import os
import re

def clean_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove sourceMappingURL in CSS and JS
    content = re.sub(r'/\*# sourceMappingURL=.*?\*/', '', content)
    content = re.sub(r'//# sourceMappingURL=.*', '', content)

    # Fix filename logic for carousel
    content = re.sub(
        r'var [a-z]=location\.pathname\.split\("/"\)\.pop\(\);.*?index\.html"===[a-z]&&',
        'var filename=location.pathname.split("/").pop(); if(filename === "index.html" || filename === "") ',
        content
    )

    # In index.html, deduplicate some scripts if needed
    if 'index.html' in filepath:
        # This is complex to do via regex on a 5MB file, but we can target the transparency scripts specifically
        # Let's just remove the data-source ones and put a clean one at the end
        pass

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    print(f"Cleaning {f}...")
    clean_html(f)
