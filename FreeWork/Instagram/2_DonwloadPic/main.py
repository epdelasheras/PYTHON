import re
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import urllib.request

site = 'https://es.kiosko.net/es/np/marca.html'

driver = webdriver.Chrome("d:/Trabajo/GitHub/PYTHON/Instagram/2_DonwloadPic/chromedriver.exe")
driver.get(site)
#response = requests.get(site)

#soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup)

img_tags = soup.find_all('img')
#print (img_tags)

urls = [img['src'] for img in img_tags]
#print (urls)

directory = os.path.dirname(os.path.realpath(__file__)) + "/marca/"
if not os.path.exists(directory):
    os.makedirs(directory)

for url in urls:
    
    filename = re.findall(r"marca.750", str(url))        
    #filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if filename != []:
        print (filename) 
        print(url)        
        imagename = os.path.join(directory, "PortadaMarca"+".jpg")
        with open(imagename, 'wb') as f:
            urllib.request.urlretrieve("http:"+url, imagename)
    else:
        pass
