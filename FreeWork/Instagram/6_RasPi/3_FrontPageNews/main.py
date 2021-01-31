from my_lib import *

print("##########Downloading pics...##########")
deletePicFiles()
# launch chrome
driver = webdriver.Chrome(BROWSER, options=browserOptions())
driver.implicitly_wait(2)
# download pics
downloadPic(driver, URL_ELPAIS, KEY_ELPAIS, "PortadaElPais")
downloadPic(driver, URL_ELMUNDO, KEY_ELMUNDO, "PortadaElMundo")
downloadPic(driver, URL_ABC, KEY_ABC, "PortadaABC")
downloadPic(driver, URL_LAVANGUARDIA, KEY_LAVANGUARDIA, "PortadaLaVanguardia")
downloadPic(driver, URL_LARAZON, KEY_LARAZON, "PortadaLaRazon")
# Close the window website
driver.close()  
print("##########Pics downloaded successfully##########")

print("##########Login Instagram wait...##########")
# load studio creator webpage
driver = webdriver.Chrome(BROWSER, options=browserOptions())
driver.implicitly_wait(2)
window_before, driver = studioCreatorLogin(driver, URL_STUDIO_CREATOR)                      
# Get user/pass from the GUI cells.
instagramLogin(driver, LOGIN_USERNAME, LOGIN_PASSWORD)
print("##########Login successfully!##########")
# Wait 3sec until the old windows is loaded
time.sleep(3)
# Switch to the old window
driver.switch_to.window(window_before)        
time.sleep(3)
# Upload all pics
print("##########Uploading pics wait...##########")
studioCreatorUpload(driver)        
driver.close()
print("##########Pics upload successfully!##########")