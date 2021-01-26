from my_lib import *

# create/remove pic folder
createFolderPics()
print("##########Folder pics created successfully##########")
# launch chrome
driver = webdriver.Chrome(BROWSER, options=browserOptions())
driver.implicitly_wait(2)       
# download pics
downloadPic(driver, URL_AS, KEY_AS, "PortadaAS")
downloadPic(driver, URL_MARCA, KEY_MARCA, "PortadaMarca")
downloadPic(driver, URL_MUNDO, KEY_MUNDO, "PortadaMundo")
downloadPic(driver, URL_SPORT, KEY_SPORT, "PortadaSport")
# Close the window website
driver.close()  
print("##########Pics downloaded successfully##########")

# load studio creator webpage
driver = webdriver.Chrome(BROWSER, options=browserOptions())
driver.implicitly_wait(2)
print("##########Login Instagram wait...##########")
window_before, driver = studioCreatorLogin(driver, URL_STUDIO_CREATOR)                      
# Get user/pass from the GUI cells.
instagramLogin(driver, LOGIN_USERNAME, LOGIN_PASSWORD)
print("##########Login successfully!##########")
# Wait 3sec until the old windows is loaded
time.sleep(3)
# Switch to the old window
driver.switch_to_window(window_before)        
time.sleep(3)
# Upload all pics
print("##########Uploading pics wait...##########")
studioCreatorUpload(driver)        
driver.close()
print("##########Pics upload successfully!##########")