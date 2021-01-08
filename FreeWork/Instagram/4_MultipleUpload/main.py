from instabot import Bot 
import os
from my_lib import *

bot = Bot() 
bot.login(username = "portatest", password = "kikazo") 


picname1 = "PortadaMarca"
image_resize(picname1)

picname2 = "PortadaAs"
image_resize(picname2)

# Recommended to put the photo 
# you want to upload in the same 
# directory where this Python code 
# is located else you will have 
# to provide full path for the photo 
bot.upload_photo(picname1 + "_resize.jpg", 
				caption = picname1)


#os.remove(picname + "_resize.jpg.REMOVE_ME")

print("fin") 
