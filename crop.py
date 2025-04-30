from PIL import Image

img = Image.open('images/frame.bmp')

crop_pixels = 32
width, height = img.size

cropped_img = img.crop( (crop_pixels, crop_pixels, width-crop_pixels, height-crop_pixels) )
cropped_img.save('images/cropped_qrcode.bmp')