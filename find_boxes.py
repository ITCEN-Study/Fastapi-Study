import numpy as np
from PIL import Image

target_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\img_practice8_2_1.png"
img = Image.open(target_path).convert("RGB")
img_np = np.array(img)
h, w, c = img_np.shape

# Let's print the colors at y=300, for x sampled every 10 pixels
print("Colors at y=300 across x:")
row_y = 300
for x in range(0, w, 20):
    color = list(img_np[row_y, x])
    # check if not white [255, 255, 255]
    if color != [255, 255, 255]:
        print(f"x={x}: {color}")
