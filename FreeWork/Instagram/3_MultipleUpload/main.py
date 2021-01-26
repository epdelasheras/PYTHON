import time
from my_lib import *

# load studio creator webpage
window_before, driver = studioCreatorLogin()

# login instagram account
username = 'portatest'
passwd = 'kikazo'
instagramLogin(driver, username, passwd)

# Wait 3sec until the old windows is loaded
time.sleep(3)

# Switch to the old window
driver.switch_to_window(window_before)

# upload pics to sutio creator
studioCreatorUpload(driver)

# logaout instagram
instagramLogout(driver)

print("Fin")