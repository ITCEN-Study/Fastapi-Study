import numpy as np
from PIL import Image

target_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\img_practice8_2_1.png"
img = Image.open(target_path).convert("RGB")
img_np = np.array(img)
h, w, c = img_np.shape

# Let's find where the buttons are by scanning for the background color #ab015f (RGB: 171, 1, 95)
# Let's find pixels close to [171, 1, 95]
mask = (np.abs(img_np[:, :, 0] - 171) < 15) & (np.abs(img_np[:, :, 1] - 1) < 15) & (np.abs(img_np[:, :, 2] - 95) < 15)
y_indices, x_indices = np.where(mask)

if len(y_indices) > 0:
    min_y, max_y = np.min(y_indices), np.max(y_indices)
    min_x, max_x = np.min(x_indices), np.max(x_indices)
    print(f"Buttons area: y={min_y} to {max_y}, x={min_x} to {max_x}")
    
    # Let's analyze the text colors inside each button.
    # The buttons are spread horizontally. Let's find the centers of the three buttons.
    # We can divide the x range into three parts:
    x_width = (max_x - min_x) // 3
    for i in range(3):
        bx_start = min_x + i * x_width
        bx_end = bx_start + x_width
        # Crop this button's text area (center of the button)
        button_crop = img_np[min_y + 20 : max_y - 20, bx_start + 20 : bx_end - 20]
        # Look for text pixels (which should be different from button background [171, 1, 95] and white/gray)
        # Text in the button will have a different color. Let's find the unique non-background colors in this cropped area.
        colors, counts = np.unique(button_crop.reshape(-1, 3), axis=0, return_counts=True)
        sorted_indices = np.argsort(-counts)
        print(f"Button {i+1} (approx x={bx_start}-{bx_end}):")
        for idx in sorted_indices:
            color = colors[idx]
            cnt = counts[idx]
            # Ignore background color #ab015f
            is_bg = (np.abs(color[0] - 171) < 20) and (color[1] < 20) and (np.abs(color[2] - 95) < 20)
            if not is_bg and cnt > 5:
                print(f"  Color {list(color)} count: {cnt}")
else:
    print("Could not find button background color #ab015f in image.")
