import os

PROJECT_ROOT = '/Users/kayadelfgaauw/Documents/Napoli_Events_2'
ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif', '.ico')

# 1. Gather all code content
code_content = ""
for root, dirs, files in os.walk(PROJECT_ROOT):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.css', '.js')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    code_content += f.read()
            except Exception as e:
                print(f"Could not read {file}: {e}")

# 2. Walk assets and check usage
deleted_count = 0
for root, dirs, files in os.walk(ASSETS_DIR):
    for file in files:
        if file.lower().endswith(EXTENSIONS):
            file_path = os.path.join(root, file)
            
            # Simple check: is the filename in the code?
            # This handles 'image.webp' appearing in 'assets/images/WebP/image.webp' reference
            if file not in code_content:
                print(f"Deleting unused file: {file}")
                try:
                    os.remove(file_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {file}: {e}")
            else:
                # File is used
                pass

print(f"Cleanup complete. Deleted {deleted_count} files.")
