import numpy as np
from PIL import Image

target_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\img_practice8_2_1.png"
img = Image.open(target_path).convert("RGB")
img_np = np.array(img)
h, w, c = img_np.shape

print(f"Image dimensions: {w}x{h}")

# Let's find all unique colors (excluding white and grays)
colors, counts = np.unique(img_np.reshape(-1, 3), axis=0, return_counts=True)
sorted_indices = np.argsort(-counts)

print("Non-white, non-gray colors:")
for idx in sorted_indices:
    color = colors[idx]
    cnt = counts[idx]
    
    # Check if not gray/white
    is_gray = (abs(int(color[0]) - int(color[1])) < 10) and (abs(int(color[1]) - int(color[2])) < 10) and (abs(int(color[0]) - int(color[2])) < 10)
    if not is_gray and cnt > 50:
        # Find one coordinate of this color
        y_idx, x_idx = np.where((img_np[:, :, 0] == color[0]) & (img_np[:, :, 1] == color[1]) & (img_np[:, :, 2] == color[2]))
        print(f"Color: {list(color)}, Count: {cnt}, Sample Coordinate: (x={x_idx[0]}, y={y_idx[0]})")
