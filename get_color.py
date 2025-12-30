from PIL import Image
from collections import Counter

def get_bg_color(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    # Sample the top-left corner pixel, usually background
    bg_color = img.getpixel((0, 0))
    return '#{:02x}{:02x}{:02x}'.format(*bg_color)

print(get_bg_color('assets/images/logo-blue.png'))
