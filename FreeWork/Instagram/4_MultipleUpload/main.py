import autoit # pip install -U pyautoit
import os
import time
from my_lib import *
from selenium import webdriver

site = "https://www.instagram.com/accounts/login/"

driver = webdriver.Chrome("chromedriver.exe", options=get_options())
driver.get(site)

# wait some time until load page
time.sleep(3)

# Press button to accept cookies
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()

# wait some time until load page
time.sleep(1)

user = driver.find_element_by_name('username')
user.send_keys('portatest')

passw = driver.find_element_by_name('password')
passw.send_keys('kikazo')

# Press login button
driver.find_element_by_xpath('/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[6]/button').click()

time.sleep(3)

# Press "Ahora no" button for not saving info
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/button').click()

time.sleep(2)

# Press "Cancelar" button for not adding info to the starting screen
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

time.sleep(2)

picname = "PortadaMarca"
image_resize(picname)

# 1. Click upload image button
print('Clicking `upload` button...')
driver.find_element_by_xpath("//div[@role='menuitem']").click()
time.sleep(2)

# 2. Get the windows file explorer window that opened
# Add the image path and click enter
print('Uploading image to file explorer...')
autoit.win_active("Open")
file_path = 'PortadaMarca_resize.jpg'
autoit.control_send("Abrir", "Edit1", os.path.normpath(os.getcwd() + '/' + file_path))
autoit.control_send("Abrir", "Edit1", "{ENTER}")
time.sleep(2)

# 3. Image should import and click Next button
print('Image importing and processed to description...')
driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
time.sleep(2)

# 5. CLick Share
print('Clicking `Share`!')
driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
time.sleep(4)
print('Upload completed.')