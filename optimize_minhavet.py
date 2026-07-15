from PIL import Image
import os

assets = '/home/ubuntu/oftalmo-vet-site/minhavet-site/assets'

tasks = [
    ('hero_dog_desktop.png', 'hero_dog_desktop.webp', 1440, 810, 55),
    ('hero_dog_mobile.png', 'hero_dog_mobile.webp', 720, 1280, 55),
    ('logo.png', 'logo.webp', 200, 200, 90),
    ('mascote.png', 'mascote.webp', 600, 600, 85),
]

for src, dst, max_w, max_h, quality in tasks:
    src_path = os.path.join(assets, src)
    dst_path = os.path.join(assets, dst)
    if not os.path.exists(src_path):
        print(f'SKIP: {src}')
        continue
    img = Image.open(src_path)
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    img.save(dst_path, 'WEBP', quality=quality, method=6)
    print(f'Optimized: {dst}')

print('Optimization complete!')
