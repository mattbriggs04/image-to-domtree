from PIL import Image
import random
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[1]} <output file>")

# generate a random black and white bmp image
width=20
height=10
img = Image.new('1', (width, height))

pixels = img.load()
for y in range(height):
    for x in range(width):
        pixels[x, y] = random.randint(0, 1)

img.save(str(sys.argv[1]), format='BMP')