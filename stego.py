from PIL import Image
from math import gcd
import numpy as np 
import matplotlib.pyplot as plt 


img_pil=(Image.open("IMAGE TO UPLOAD"))

Width ,Height = img_pil.size
print(f"Width: {Width}, Height: {Height}")

img=np.array(img_pil)

plt.imshow(img_pil)
plt.show()

message=input("What is the message you wish to encode? \n")
message += "[END]"
message = message.encode("ascii")
message_bits = ''.join([format(byte, '08b') for byte in message])

img_flat = img.flatten()

for idx, bit in enumerate(message_bits):
    pixel_value = img_flat[idx] 
    pixel_value_bin=format(pixel_value, '08b')
    new_pixel_value_bin=pixel_value_bin[:-1]+bit
    img_flat[idx]=int(new_pixel_value_bin, 2)

img_encoded=img_flat.reshape((Height, Width, -1))


print(message)
print(message[1])
plt.imshow(img_encoded)
plt.show()

img_flat=img_encoded.flatten()

find_message=""

idx=0


while find_message[-5:] != "[END]":
    bits=[format(img_flat[i], '08b')[-1] for i in range (idx, idx+8)]
    bits=''.join(bits)
    find_message+=chr(int(bits,2))
    idx+=8

    if idx > len(img_flat):
        print("No hidden message found")
        break

print("Decoded Message", find_message)
