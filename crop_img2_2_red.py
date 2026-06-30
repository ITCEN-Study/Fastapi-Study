from PIL import Image
import numpy as np

img_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\img_practice8_2_2.png"
img = Image.open(img_path).convert("L")
w, h = img.size

# Bounding box: x=351~506, y=169~223. Let's crop x=330 to 520, y=150 to 240
crop_area = img.crop((330, 150, 520, 240))
cw, ch = crop_area.size

pixels = list(crop_area.getdata())
chars = " .:-=+*#%@"
num_chars = len(chars)

ascii_str = []
for i, pixel in enumerate(pixels):
    if i > 0 and i % cw == 0:
        ascii_str.append("\n")
    idx = int((pixel / 255) * (num_chars - 1))
    ascii_str.append(chars[idx])

output_path = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\scratch\crop_img2_2_red.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("".join(ascii_str))

print("Saved crop ASCII to", output_path)
