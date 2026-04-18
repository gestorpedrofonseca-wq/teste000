import base64
import os

images = [
    "assets/img/favicon.405cd09d.ico",
    "assets/img/white-logo.a195d627.png",
    "assets/img/sopa-solidaria1.90eb9325.jpg",
    "assets/img/zumba1.735b7a1b.jpg",
    "assets/img/sede-os-fenix.69d530f4.jpg",
    "assets/img/46yYWfa.jpg",
    "assets/img/BuN7Gym.jpg",
    "assets/img/ODN13IE.jpg",
    "assets/img/qtshKGQ.jpg",
    "assets/img/pix-qr.png",
    "assets/img/Charity.ec4e9031.jpg"
]

base_path = r"c:\Users\User\OneDrive\Área de Trabalho\SITE CLIENTE 01"
output_file = os.path.join(base_path, "image_map.py")

image_map = {}

for img in images:
    full_path = os.path.join(base_path, img)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode('utf-8')
            ext = os.path.splitext(img)[1].lower().strip('.')
            if ext == 'ico':
                mime = 'image/x-icon'
            elif ext in ['jpg', 'jpeg']:
                mime = 'image/jpeg'
            elif ext == 'png':
                mime = 'image/png'
            elif ext == 'svg':
                mime = 'image/svg+xml'
            else:
                mime = f'image/{ext}'
            image_map[img] = f"data:{mime};base64,{encoded}"

with open(output_file, "w") as f:
    f.write("image_map = " + repr(image_map))

print(f"Generated map for {len(image_map)} images.")
