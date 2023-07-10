import sys
from PIL import Image

orig = Image.open(sys.argv[1])
im = orig.convert("L").resize((256, 256), Image.BICUBIC)
im2 = im.copy()
(width, height) = im.size

for x in range(width):
    for y in range(height):
        im2.putpixel((x, y), 0)

for x in range(width):
    for y in range(height):
        brightness = im.getpixel((x, y))
        im2.putpixel((brightness, y), x)

im2.convert("RGB").resize(orig.size, Image.HAMMING).save("out.png", "PNG")
