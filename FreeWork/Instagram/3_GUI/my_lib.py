
from PIL import Image
import math
import os
from os import path
import shutil
import re
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import urllib.request

FOLDER = './pics'
URL_MARCA = 'https://es.kiosko.net/es/np/marca.html'
KEY_MARCA = 'marca.750'
URL_AS = 'https://es.kiosko.net/es/np/as.html'
KEY_AS = 'as.750'
URL_MUNDO = 'https://es.kiosko.net/es/np/mundodeportivo.html'
KEY_MUNDO = 'mundodeportivo.750'
URL_SPORT = 'https://es.kiosko.net/es/np/sport.html'
KEY_SPORT = 'sport.750'

def pic_download(driver, site, pathToStore, wordToFind, picname):
    driver.get(site)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]    
    directory = os.path.dirname(os.path.realpath(__file__)) + pathToStore
    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urls:    
        filename = re.findall(wordToFind, str(url))                
        if filename != []:
            print (filename) 
            print(url)        
            imagename = os.path.join(directory, picname + ".jpg")
            with open(imagename, 'wb') as f:
                urllib.request.urlretrieve("http:"+url, imagename)
        else:
            pass

def init_app():

    # creating the pics directory    
    if path.exists("pics") == True:
        shutil.rmtree(FOLDER, ignore_errors=True)
        print ("Successfully removed the directory %s " % FOLDER)                               
        try:                            
            os.mkdir(FOLDER)      
        except OSError:
            print ("Creation of the directory %s failed" % FOLDER)
        else:
            print ("Successfully created the directory %s " % FOLDER)                       
    else:        
        try:                            
            os.mkdir(FOLDER)      
        except OSError:
            print ("Creation of the directory %s failed" % FOLDER)
        else:
            print ("Successfully created the directory %s " % FOLDER)                                   


def InstaPicResize(im, min_size=1080, fill_color=(255, 255, 255)):
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