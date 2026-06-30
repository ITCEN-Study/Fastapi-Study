from PIL import Image
import os

target_dir = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f"
output_dir = r"C:\Users\user\.gemini\antigravity-cli\brain\7adc94b8-4acd-4fef-a08c-6394f6478f5f\scratch"

def convert_to_ascii(img_name, out_name, width=120):
    img_path = os.path.join(target_dir, img_name)
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return
    img = Image.open(img_path).convert("L")
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.5)
    img_resized = img.resize((width, height))
    
    pixels = list(img_resized.getdata())
    chars = " .:-=+*#%@"
    num_chars = len(chars)
    
    lines = []
    for idx, pixel in enumerate(pixels):
        if idx > 0 and idx % width == 0:
            lines.append("\n")
        val = int((pixel / 255) * (num_chars - 1))
        lines.append(chars[val])
        
    out_path = os.path.join(output_dir, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print(f"Saved {img_name} as ASCII to {out_name}")

convert_to_ascii("img_practice8_2_1.png", "img2_1_ascii.txt")
convert_to_ascii("img_practice8_2_2.png", "img2_2_ascii.txt")
convert_to_ascii("img_practice8_2_3.png", "img2_3_ascii.txt")
