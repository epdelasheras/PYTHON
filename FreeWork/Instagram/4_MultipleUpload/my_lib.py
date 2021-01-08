
from PIL import Image
import math

def make_square(im, min_size=1080, fill_color=(255, 255, 255)):
    #here getting the width and the height of the picture and after that adjusting it's size for it to fit on a 1080px picture perfectly
    width, height = im.size
    ratio = 1080 / width
    width = width + 0.00
    height = height + 0.00
    width = width * ratio
    height = height * ratio
    height = math.floor(height)
    width = math.floor(width)
    im = im.resize((width, height)) #resizing the picture to width 1080
    #here is some code i got online to create a white picture then paste my picture on top of it to make the picture square
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    new_im = new_im.convert("RGB")
    return new_im # returning the new image so that I can save and upload

def image_resize (picname):
    img_pil = Image.open(picname + ".jpg")
    img_resize = make_square(img_pil, 1080, (255, 255, 255))
    img_resize = img_resize.save(picname + "_resize.jpg")
