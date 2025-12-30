import os
import re

files_to_update = [
    "index.html",
    "style.css",
    "catering.html",
    "exclusief.html",
    "originale.html",
    "workshops.html",
    "over-ons.html"
]

# Regex to match assets/images/filename.extension
# Captured group 1: filename (excluding path and extension)
# Captured group 2: extension (jpg or png)
# Lookahead/behind or just match the whole string?
# Matching "assets/images/filename.ext".
# Exclude if it already has "WebP/" in it?
# My regex `assets/images/([^/"]+)\.(jpg|png)` does that by excluding slash.

pattern = re.compile(r'assets/images/([^/"]+)\.(jpg|png)', re.IGNORECASE)

replacement = r'assets/images/WebP/\1.webp'

base_dir = "/Users/kayadelfgaauw/Documents/Napoli_Events_2"

for filename in files_to_update:
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        print(f"Skipping {filename} (not found)")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, count = pattern.subn(replacement, content)
        
        if count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {count} references in {filename}")
        else:
            print(f"No matches found in {filename}")
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")
