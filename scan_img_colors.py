import numpy as np
from PIL import Image
import os

target_dir = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f"

def scan_colors(img_name):
    img_path = os.path.join(target_dir, img_name)
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return
    img = Image.open(img_path).convert("RGB")
    img_np = np.array(img)
    colors, counts = np.unique(img_np.reshape(-1, 3), axis=0, return_counts=True)
    sorted_indices = np.argsort(-counts)
    print(f"\n--- Colors in {img_name} ---")
    for idx in sorted_indices[:20]:
        c = colors[idx]
        cnt = counts[idx]
        is_gray = (abs(int(c[0]) - int(c[1])) < 10) and (abs(int(c[1]) - int(c[2])) < 10) and (abs(int(c[0]) - int(c[2])) < 10)
        if not is_gray or cnt > 10000:
            print(f"Color {list(c)} count: {cnt}")

scan_colors("img_practice8_2_2.png")
scan_colors("img_practice8_2_3.png")
