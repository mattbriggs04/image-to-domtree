from PIL import Image

# this file was used in order to crop the qr code image because it was very large (>1.5MB)
if __name__ == "__main__":
    imgfile = "images/frame.bmp"
    img = Image.open(imgfile)

    # the amount of pixels to crop of each side
    crop_pixels = 32
    width, height = img.size
    cropped_img = img.crop( (crop_pixels, crop_pixels, width-crop_pixels, height-crop_pixels) )

    cropped_img.save('images/cropped_qrcode.bmp')