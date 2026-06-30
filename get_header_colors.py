import numpy as np
from PIL import Image

target_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\img_practice8_2_1.png"
img = Image.open(target_path).convert("RGB")
img_np = np.array(img)
h, w, c = img_np.shape

# Crop header area: y=30 to 150, x=100 to 1100
header = img_np[30:150, 100:1100]

# Find unique colors
colors, counts = np.unique(header.reshape(-1, 3), axis=0, return_counts=True)
sorted_indices = np.argsort(-counts)

print("--- Header Colors ---")
for idx in sorted_indices[:15]:
    c = colors[idx]
    cnt = counts[idx]
    is_white_or_gray = (abs(int(c[0]) - int(c[1])) < 10) and (abs(int(c[1]) - int(c[2])) < 10) and (abs(int(c[0]) - int(c[2])) < 10)
    if not is_white_or_gray or cnt > 10000:
        print(f"Color {list(c)} count: {cnt}")
        
# Crop the button area: y=180 to 550
content = img_np[180:550, 100:1100]
colors2, counts2 = np.unique(content.reshape(-1, 3), axis=0, return_counts=True)
sorted_indices2 = np.argsort(-counts2)

print("--- Content Colors ---")
for idx in sorted_indices2[:15]:
    c = colors2[idx]
    cnt = counts2[idx]
    is_white_or_gray = (abs(int(c[0]) - int(c[1])) < 10) and (abs(int(c[1]) - int(c[2])) < 10) and (abs(int(c[0]) - int(c[2])) < 10)
    if not is_white_or_gray or cnt > 10000:
        print(f"Color {list(c)} count: {cnt}")
