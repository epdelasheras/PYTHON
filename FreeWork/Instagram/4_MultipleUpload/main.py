import autoit # pip install -U pyautoit
import os
import time
from my_lib import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

site = 'https://business.facebook.com/creatorstudio/?tab=instagram_content_posts'
driver = webdriver.Chrome("chromedriver.exe", options=get_options())
driver.implicitly_wait(2)
driver.get(site)
window_before = driver.window_handles[0] # Save the current window


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

user = driver.find_element_by_name('username')
user.send_keys('portatest')

passw = driver.find_element_by_name('password')
passw.send_keys('kikazo')

# Press login button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div[1]/div/div/div/form/div[1]/div[6]/button'))).click()

# Press "Ahora no" button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/div/div/button'))).click()

# Wait 3sec until the old windows is loaded
time.sleep(3)

# Switch to the old window
driver.switch_to_window(window_before)

# Press button "Crear publicacion"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/span/div/div/div[2]'))).click()

# Press button "Seccion Noticias Instagram"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div'))).click()

# Press link "Añadir contenido"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[5]/div/div/div/span'))).click()

# Press link "Subir archivos"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div/div[1]/a'))).click()
#driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/a/div[2]').click()

# Add 1st pic
time.sleep(3)
autoit.win_active("Open")
file_path = 'PortadaMarca.jpg'
autoit.control_send("Abrir", "Edit1", os.path.normpath(os.getcwd() + '/' + file_path))
autoit.control_send("Abrir", "Edit1", "{ENTER}")

# Press linkg "añadir contenidos" & "subir archivos"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/span'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div/div/div/div[1]/a'))).click()

# Add 2nd pic
time.sleep(3)
autoit.win_active("Open")
file_path = 'PortadaAs.jpg'
autoit.control_send("Abrir", "Edit1", os.path.normpath(os.getcwd() + '/' + file_path))
autoit.control_send("Abrir", "Edit1", "{ENTER}")

# Press linkg "añadir contenidos" & "subir archivos"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/span'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div/div/div/div[1]/a'))).click()

# Add 3rd pic
time.sleep(3)
autoit.win_active("Open")
file_path = 'PortadaMundo.jpg'
autoit.control_send("Abrir", "Edit1", os.path.normpath(os.getcwd() + '/' + file_path))
autoit.control_send("Abrir", "Edit1", "{ENTER}")

# Press linkg "añadir contenidos" & "subir archivos"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/span'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div/div/div/div[1]/a'))).click()

# Add 4th pic
time.sleep(3)
autoit.win_active("Open")
file_path = 'PortadaSport.jpg'
autoit.control_send("Abrir", "Edit1", os.path.normpath(os.getcwd() + '/' + file_path))
autoit.control_send("Abrir", "Edit1", "{ENTER}")

# Press "Publicar" Button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div[2]/button'))).click()

# Load instagram website
new_site = 'https://www.instagram.com/portatest'
driver.get(new_site)

time.sleep(5)

# Click the Gear
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav[1]/div/header/div/div[1]/button'))).click()

# Click over close session
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav[1]/div/section/div[3]/div/div[4]/div/div/a/div[1]'))).click()

# Click "Salir" option
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/button[1]'))).click()


# Close the window website
driver.close()

print("Fin")