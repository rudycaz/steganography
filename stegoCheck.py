from PIL import Image
import numpy as np

original_img_pil = Image.open("ORIGINAL IMAGE PATH")
encoded_img_pil = Image.open("ENCODED IMAGE PATH")

original_img = np.array(original_img_pil)
encoded_img = np.array(encoded_img_pil)

original_img_flat = original_img.flatten()
encoded_img_flat = encoded_img.flatten()

for idx in range(len(original_img_flat)):
    original_pixel_bin = format(original_img_flat[idx], '08b')  
    encoded_pixel_bin = format(encoded_img_flat[idx], '08b')    
    
    if original_pixel_bin[-1] != encoded_pixel_bin[-1]:
        print(f"Pixel {idx}: Original LSB = {original_pixel_bin[-1]}, Encoded LSB = {encoded_pixel_bin[-1]}")

print("LSB comparison done.")
