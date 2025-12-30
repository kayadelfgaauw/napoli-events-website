from PIL import Image

def generate_maximized_favicon(source_path, size):
    img = Image.open(source_path).convert("RGBA")
    
    # Autocrop: Trim transparent borders to maximize content
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        print(f"Cropped transparent borders. New dimensions: {img.size}")
    
    # Calculate new size preserving aspect ratio
    # We want the longest dimension to fill the size completely
    img.thumbnail((size, size), Image.Resampling.LANCZOS)
    
    # Create transparent square background
    background = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    
    # Calculate centering position
    pos = ((size - img.size[0]) // 2, (size - img.size[1]) // 2)
    
    # Paste image onto background
    background.paste(img, pos)
    return background

source = '/Users/kayadelfgaauw/.gemini/antigravity/brain/ea1dbd3d-f62f-425d-bc07-81f43a18f12b/uploaded_image_1767128505587.png'

# Generate WebP (High res)
high_res = generate_maximized_favicon(source, 192)
high_res.save('favicon.webp', 'WEBP')

# Generate ICO (Standard 32x32)
ico_img = generate_maximized_favicon(source, 32)
ico_img.save('favicon.ico', 'ICO')

print("Favicons maximized and regenerated.")
