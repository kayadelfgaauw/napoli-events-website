import os
from PIL import Image

SOURCE_DIR = "/Users/kayadelfgaauw/Documents/Napoli_Events_2/assets/images"
TARGET_DIR = os.path.join(SOURCE_DIR, "WebP")

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

valid_extensions = ('.jpg', '.jpeg', '.png')

print(f"Scanning {SOURCE_DIR}...")

for filename in os.listdir(SOURCE_DIR):
    if filename.lower().endswith(valid_extensions):
        source_path = os.path.join(SOURCE_DIR, filename)
        
        # Construct target filename
        name_root, _ = os.path.splitext(filename)
        target_filename = f"{name_root}.webp"
        target_path = os.path.join(TARGET_DIR, target_filename)
        
        try:
            with Image.open(source_path) as img:
                print(f"Converting {filename} to WebP...")
                img.save(target_path, "WEBP", quality=85)
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

# Special check for workshops-process.jpg which might already be in WebP folder but as a jpg or needs move
# Actually, the user uploaded it and I copied it to WebP folder as jpg in previous step. 
# Let's check the WebP folder itself for any non-webp files that need conversion?
# The prompt implies converting "all photos currently on the site". 
# The ls command showed 'workshops-process.jpg' inside `assets/images/WebP/`.
# My script above scans `assets/images`. 
# I should also scan `assets/images/WebP` for non-webp files to be thorough, 
# or just ensure `workshops-process.jpg` gets converted.

WEBP_SUBDIR = os.path.join(SOURCE_DIR, "WebP")
print(f"Scanning {WEBP_SUBDIR} for any remaining non-webp files...")
for filename in os.listdir(WEBP_SUBDIR):
    if filename.lower().endswith(valid_extensions):
        source_path = os.path.join(WEBP_SUBDIR, filename)
        name_root, _ = os.path.splitext(filename)
        target_filename = f"{name_root}.webp"
        target_path = os.path.join(WEBP_SUBDIR, target_filename)
        
        # Avoid re-converting if it already exists? Or overwrite? Overwrite is safer for updates.
        try:
            with Image.open(source_path) as img:
                print(f"Converting {filename} (in WebP folder) to WebP...")
                img.save(target_path, "WEBP", quality=85)
                # Optional: remove original jpg from WebP folder to keep it clean? 
                # User asked to "change to WebP", implies replacement or usage of WebP. 
                # I'll keep the original for safety unless I'm sure.
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print("Conversion complete.")
