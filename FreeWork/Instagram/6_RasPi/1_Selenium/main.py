from selenium import webdriver
from selenium.webdriver.chrome.options import *

BROWSER = "/usr/lib/chromium-browser/chromedriver" #To work in raspbian
SITE = 'https://business.facebook.com/creatorstudio/?tab=instagram_content_posts'

def browserOptions():
# Load chrome profile cfg when the chrome driver is loaded.
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    #options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36')    
    #options.add_argument("user-data-dir=ChromeCfg")
    return options

driver = webdriver.Chrome(BROWSER, options=browserOptions())
driver.get(SITE)
