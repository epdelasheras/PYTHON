import shutil
from bs4 import BeautifulSoup
import re
import urllib.request
from PIL import Image
import math
import os
from os import path
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import *

TIME2WAIT = 20
FOLDER = './pics'
BROWSER = "chromedriver.exe" #To work in windows
#BROWSER = "/usr/lib/chromium-browser/chromedriver" #To work in raspbian
URL_MARCA = 'https://es.kiosko.net/es/np/marca.html'
KEY_MARCA = 'marca.750'
URL_AS = 'https://es.kiosko.net/es/np/as.html'
KEY_AS = 'as.750'
URL_MUNDO = 'https://es.kiosko.net/es/np/mundodeportivo.html'
KEY_MUNDO = 'mundodeportivo.750'
URL_SPORT = 'https://es.kiosko.net/es/np/sport.html'
KEY_SPORT = 'sport.750'
LOGIN_USERNAME = "prensatest"
LOGIN_PASSWORD = "kikazo"
URL_STUDIO_CREATOR = 'https://business.facebook.com/creatorstudio/?tab=instagram_content_posts'
TAG_LOCATION = "España"
TAG_POST = "Portadas de hoy " + str(time.strftime("%d/%m/%y"))
TAG_HASTAGS = "#portadas#portad_as_ymas#diarioas#diariomarca#diariosport#mundodeportivo#deporte#futbol#laligasantander#uefachampionsleague#championsleague#realmadridcf#zidane#sergioramos#benzema#modric#cristianoronaldo#fcbarcelona#koeman#messi#pedri#neymar#atleticodemadrid#simeone#marcosllorente#oblak#jaofelix#luissuarez#hazard"          

#----------------------- OTHER METHODs-------------------------------
def createFolderPics():
# Method used to create/delete pics folder
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



def browserOptions():
# Load chrome profile cfg when the chrome driver is loaded.
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    #options.add_argument("--headless") #This line is mandatory when the script/crontab is executed. Comment to see the explorer running.
    #options.add_argument('--disable-dev-shm-usage') #This line is mandatory when the script/crontab is executed. Comment to see the explorer running.
    #options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36')    
    #options.add_argument("user-data-dir=ChromeCfg")
    return options

def StudioCreatorAddPic(driver, picname):
# Method used to add pics into the studio creator website
    # adjust pic size    
    file_path = picResize(picname)    
    # load pic
    pathPics = os.path.normpath(os.getcwd() + '/' + file_path)
    driver.find_element_by_xpath("//input[@type='file']").clear()
    driver.find_element_by_xpath("//input[@type='file']").send_keys(pathPics)    

def picResize (picname):
# Method used to resize the pic to fit into the instagram standards
    img_pil = Image.open(str(FOLDER) + '/' + picname + ".jpg")
    img_resize = picAdjust(img_pil, 1080, (255, 255, 255))    
    img_resize = img_resize.save(str(FOLDER) + '/' + picname + "_resize.jpg")    
    return str(FOLDER) + '/' + picname + "_resize.jpg"

def picAdjust(im, min_size=1080, fill_color=(255, 255, 255)):
# Method called from picResize method. Adjust the size of the pic
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

#----------------------- DOWNLOAD PICs METHODs-----------------------

def downloadPic(driver, site, wordToFind, picname):
    driver.get(site)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]    
    directory = os.path.dirname(os.path.realpath(__file__)) + FOLDER
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

#----------------------- INSTAGRAM + STUDIO CREATOR METHODs-----------------------

def studioCreatorLogin(driver, site):
    try:    
        print("Loading Studio Creator Webpage, wait...")
        window_before = driver.window_handles[0] # Save the current window    
        driver.get(site)
        print("Waiting for cookies window, wait...")    
        #Press Cookies button    
        keyElement = "//button[contains(@id, 'u_0_') and @class='_42ft _4jy0 _9fix _4jy3 _517h _51sy']"    
        element = WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,keyElement)))    
        driver.execute_script("arguments[0].click();", element)
        keyElement = "//button[contains(@id, 'u_0_') and @class='_42ft _4jy0 _9gti _4jy3 _4jy1 selected _51sy']"    
        element = WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,keyElement)))    
        driver.execute_script("arguments[0].click();", element)
        keyElement = "//button[contains(@id, 'u_0_') and @class='_42ft _4jy0 _9fws _4jy3 _4jy1 selected _51sy']"    
        element = WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,keyElement)))    
        driver.execute_script("arguments[0].click();", element)
        print("Cookies button ok!")
        # Press Instagram button    
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.ID,'media_manager_chrome_bar_instagram_icon'))).click()        
        print("Instagram button ok!")
        # Press "Inicio de sesion" button    
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='l61y9joe j8otv06s a1itoznt qwtvmjv2 svz86pwt ippphs35 a53abz89 tds9wb2m']"))).click()        
        print("Session start button ok!")
        # Wait until the new windows is loaded    
        WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
        print("New window loaded ok!")
        # Save the new window
        window_after = driver.window_handles[1]
        # Switch to the new window
        driver.switch_to_window(window_after)
        #driver.implicitly_wait(2)
        #Press Cookies button            
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='aOOlW   HoLwm ']"))).click()
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='aOOlW  bIiDR  ']"))).click()
        print("Cookies Instagram button ok!")
        return window_before, driver    
    except TimeoutException:
        print("Timeout exception error :-(")
        driver.close()

def instagramLogin(driver, username, passwd):
    # fill user / pass cells         
    user = driver.find_element_by_name('username')
    user.send_keys(username)        
    passw = driver.find_element_by_name('password')
    passw.send_keys(passwd)
    try:    
        # Press login button                         
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//form[@id='loginForm']/div[1]/div[6]/button/div"))).click()
        print("Login Instagram button ok!")
        # Press "Ahora no" button  
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='sqdOP yWX7d    y3zKF     ']"))).click()         
        print("Not now Instagram button ok!")
    except TimeoutException:
        print("Timeout exception error :-(")
        driver.close()    

def studioCreatorUpload(driver): 
    try:   
        # Press button "Crear publicacion"                
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='l61y9joe j8otv06s a1itoznt qwtvmjv2 kiex77na lgsfgr3h mcogi7i5 ih1xi9zn ippphs35 a53abz89 yukb02kx']"))).click()            
        print("Create post Studio Creator button ok!")
        # Press button "Seccion Noticias Instagram"            
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='l61y9joe j8otv06s a1itoznt te7ihjl9 svz86pwt q3s3exew d8d6zf0d p66o6c86 jrvjs1jy a53abz89']"))).click()            
        print("News section Studio Creator loaded ok!")
        time.sleep(3)    
        # Add 1st pic    
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='l61y9joe j8otv06s a1itoznt fvlrrmdj svz86pwt jrvjs1jy a53abz89 jvnjaidj']"))).click()                    
        print("Add pic button ok!")
        StudioCreatorAddPic(driver, 'PortadaAs')
        WebDriverWait(driver, TIME2WAIT).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='_6eqx _6a']"), "100%"))                
        WebDriverWait(driver, TIME2WAIT).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='_6eqx _6a']"), "100%"))       
        print("Pic1 added ok")
        # Add 2nd pic       
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='l61y9joe j8otv06s a1itoznt fvlrrmdj svz86pwt jrvjs1jy a53abz89 jvnjaidj']"))).click()    
        StudioCreatorAddPic(driver, 'PortadaMarca')
        WebDriverWait(driver, TIME2WAIT).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='_6eqx _6a']"), "100%"))    
        print("Pic2 added ok")    
        # Add 3rd pic    
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='l61y9joe j8otv06s a1itoznt fvlrrmdj svz86pwt jrvjs1jy a53abz89 jvnjaidj']"))).click()    
        StudioCreatorAddPic(driver, 'PortadaMundo')
        WebDriverWait(driver, TIME2WAIT).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='_6eqx _6a']"), "100%"))    
        print("Pic3 added ok")    
        # Add 4th pic    
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='l61y9joe j8otv06s a1itoznt fvlrrmdj svz86pwt jrvjs1jy a53abz89 jvnjaidj']"))).click()    
        StudioCreatorAddPic(driver, 'PortadaSport')    
        WebDriverWait(driver, TIME2WAIT).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='_6eqx _6a']"), "100%"))    
        print("Pic4 added ok")
        # Add post & hastag to the pics     
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_5yk2']"))).click()
        textbox_post = WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_5yk2']")))
        textbox_post.send_keys(TAG_POST + "\n" + "\n" + TAG_HASTAGS)
        # Fill location
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//input[@class='_58al']"))).click()
        textbox_location = WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//input[@class='_58al']")))
        textbox_location.send_keys(TAG_LOCATION)
        time.sleep(3)        
        textbox_location.send_keys(Keys.RETURN)
        print("Location added ok")
        # Press "Publicar" Button            
        WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_271k _271m _1qjd']"))).click()    
        print("Publish Studio Creator button ok!")    
        # Wait until all the pics are fully load:
        keyElement = "//span[@class='l61y9joe j8otv06s a1itoznt rnz22s23 svz86pwt q3s3exew d8d6zf0d p66o6c86 jrvjs1jy a53abz89 tnlcj30g o27k9hdg kkzhtrjg okqr6zti' and contains(.,'Tu contenido se ha publicado en Instagram.')]"
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH,keyElement)))            
    except TimeoutException:
        print("Timeout exception error :-(")
        driver.close()    

def instagramLogout(driver, username):
    # Load Instagram website    
    site = 'https://www.instagram.com/' + username
    print(site)
    driver.get(site)
    time.sleep(3)
    # Click the Gear
    WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav[1]/div/header/div/div[1]/button'))).click()
    time.sleep(2)
    # Click over close session
    WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav[1]/div/section/div[3]/div/div[4]/div/div/a/div[1]'))).click()
    time.sleep(2)
    # Click "Salir" option
    WebDriverWait(driver, TIME2WAIT).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/button[1]'))).click()
    time.sleep(2)
    # Close the window website
    driver.close()        

