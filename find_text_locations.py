import numpy as np
from PIL import Image
import os

target_dir = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f"

def scan_coords(img_name, color, name_str):
    img_path = os.path.join(target_dir, img_name)
    if not os.path.exists(img_path):
        return
    img = Image.open(img_path).convert("RGB")
    img_np = np.array(img)
    mask = (img_np[:, :, 0] == color[0]) & (img_np[:, :, 1] == color[1]) & (img_np[:, :, 2] == color[2])
    y_idx, x_idx = np.where(mask)
    if len(y_idx) > 0:
        print(f"[{img_name}] {name_str} {color}: count={len(y_idx)}, bounding box: x={np.min(x_idx)}~{np.max(x_idx)}, y={np.min(y_idx)}~{np.max(y_idx)}")
    else:
        print(f"[{img_name}] {name_str} {color} not found.")

# img_practice8_2_2.png (Dooly)
scan_coords("img_practice8_2_2.png", [255, 0, 0], "Red")
scan_coords("img_practice8_2_2.png", [0, 128, 1], "Green")

# img_practice8_2_3.png (Douner)
scan_coords("img_practice8_2_3.png", [0, 0, 255], "Blue")
scan_coords("img_practice8_2_3.png", [128, 0, 0], "Maroon")
