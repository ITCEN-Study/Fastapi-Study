import numpy as np
from PIL import Image
import os

target_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\img_practice8_2_1.png"
img = Image.open(target_path).convert("RGB")
img_np = np.array(img)

# Let's find unique colors in the image, ignoring background white (255, 255, 255) and gray borders
colors, counts = np.unique(img_np.reshape(-1, 3), axis=0, return_counts=True)

# Sort by count descending
sorted_indices = np.argsort(-counts)
for idx in sorted_indices[:30]:
    c = colors[idx]
    cnt = counts[idx]
    # Check if not close to white or gray
    is_white_or_gray = (abs(int(c[0]) - int(c[1])) < 10) and (abs(int(c[1]) - int(c[2])) < 10) and (abs(int(c[0]) - int(c[2])) < 10)
    if not is_white_or_gray or cnt > 10000:
        print(f"Color {list(c)} count: {cnt}")
