import os
import time
#from my_lib import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

site = "https://www.instagram.com/accounts/login/"

driver = webdriver.Chrome("chromedriver.exe")
driver.get(site)

# wait some time until load page
time.sleep(1)

# Press button to accept cookies
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()

# wait some time until load page
time.sleep(1)

user = driver.find_element_by_name('username')
user.send_keys('portatest')

passw = driver.find_element_by_name('password')
passw.send_keys('kikazo')

# Press login button
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div').click()

time.sleep(5)

# Press "Ahora no" button for not saving session info
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()

time.sleep(1)

# Press "Ahora no" for not enabling notifications
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

'''
user.send_keys('portatest')

passw = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
passw.send_keys('kikazo')

driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()

#picname = "PortadaMarca"
#image_resize(picname)
'''
print("fin")