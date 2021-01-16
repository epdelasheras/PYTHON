
import math
import autoit # pip install -U pyautoit
import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import *

def StudioCreatorAddPic(picname):
    # adjust pic size    
    file_path = image_resize(picname)
    # load pic       
    autoit.win_active("Open")    
    autoit.control_send("Abrir", "Edit1", os.path.normpath(os.getcwd() + '/' + file_path))
    autoit.control_send("Abrir", "Edit1", "{ENTER}")


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
    return picname + "_resize.jpg"

def chormeOptions():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    #options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36')    
    options.add_argument("user-data-dir=ChromeCfg")
    return options

def studioCreatorLogin():
    site = 'https://business.facebook.com/creatorstudio/?tab=instagram_content_posts'
    driver = webdriver.Chrome("chromedriver.exe", options=chormeOptions())
    driver.implicitly_wait(2)
    window_before = driver.window_handles[0] # Save the current window    
    driver.get(site)

    # Press Instagram button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[1]/div/div[1]/div[2]/div'))).click()

    # Press "Inicio de sesion" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div'))).click()

    # Wait 3sec until the new windows is loaded
    time.sleep(3)

    # Save the new window
    window_after = driver.window_handles[1]

    # Switch to the new window
    driver.switch_to_window(window_after)
    driver.implicitly_wait(2)
    return window_before, driver

def instagramLogin(driver, username, passwd):
    # fill user / pass cells
    user = driver.find_element_by_name('username')
    user.send_keys(username)
    passw = driver.find_element_by_name('password')
    passw.send_keys(passwd)

    # Press login button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[6]/button'))).click()

    # Press "Ahora no" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/div/div/button'))).click()


def studioCreatorUpload(driver):
    # Press button "Crear publicacion"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/span/div/div/div[2]'))).click()

    # Press button "Seccion Noticias Instagram"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div'))).click()

    # Press link "Añadir contenido"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[5]/div/div/div/span'))).click()

    # Press link "Subir archivos"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div/div[1]/a'))).click()
    time.sleep(3)

    # Add 1st pic
    file_path = 'PortadaMarca'
    StudioCreatorAddPic(file_path)

    # Add 2nd pic
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/span'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div/div/div/div[1]/a'))).click()
    time.sleep(3)
    file_path = 'PortadaAs'
    StudioCreatorAddPic(file_path)

    # Add 3rd pic
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/span'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div/div/div/div[1]/a'))).click()
    time.sleep(3)
    file_path = 'PortadaMundo'
    StudioCreatorAddPic(file_path)

    # Add 4th pic
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/span'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div/div/div/div[1]/a'))).click()
    time.sleep(3)
    file_path = 'PortadaSport'
    StudioCreatorAddPic(file_path)

    # Press "Publicar" Button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div[2]/button'))).click()

def instagramLogout(driver):
    # Load Instagram website
    site = 'https://www.instagram.com/portatest'
    driver.get(site)

    time.sleep(5)

    # Click the Gear
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav[1]/div/header/div/div[1]/button'))).click()

    # Click over close session
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav[1]/div/section/div[3]/div/div[4]/div/div/a/div[1]'))).click()

    # Click "Salir" option
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/button[1]'))).click()

    # Close the window website
    driver.close()    