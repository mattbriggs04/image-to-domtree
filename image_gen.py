from PIL import Image

# Create a new 5x5 image in mode '1' (1-bit pixels, black and white)
img = Image.new('1', (5, 5))

pixels = img.load()
for y in range(5):
    for x in range(5):
        pixels[x, y] = (x + y) % 2  # 0 = black, 1 = white

# Save as BMP
img.save('checkerboard.bmp')