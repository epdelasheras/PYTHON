from instabot import Bot 
from PIL import Image
import os
from my_lib import make_square

img_pil = Image.open("PortadaMarca.jpg")

img_resize = make_square(img_pil, 1080, (255, 255, 255))

#img_pil.show()
#img_resize.show()

img_resize = img_resize.save("PortadaMarca_resize.jpg")

bot = Bot() 

bot.login(username = "portatest", 
		password = "kikazo") 

# Recommended to put the photo 
# you want to upload in the same 
# directory where this Python code 
# is located else you will have 
# to provide full path for the photo 
bot.upload_photo("PortadaMarca_resize.jpg", 
				caption ="Portada Marca")

os.remove("PortadaMarca_resize.jpg.REMOVE_ME")

print("fin") 
