import requests
import webbrowser
import urllib.request
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.google.com/search?q=dog&rlz=1C1SQJL_enKR858KR858&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvyIThp8_qAhUcwosBHb2ZDwAQ_AUoAXoECBgQAw&biw=1920&bih=937'

img_dir = "./image_folder/"
dir_path = img_dir + "test"

# test opening browser
# test clicking on images and getting urls
print("opening URL")
# print("How many images?")
# image_cnt = int(input())
# print("Getting " + str(image_cnt) + " images...")
# path for mac
# driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Chrome("/Users/jeff/Desktop/chromedriver")
driver.get(url)

element = driver.find_element_by_tag_name("body")
image_urls=[]
imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(1)))
imgurl.click()
images = driver.find_elements_by_class_name("n3VNCb")

for image in images:
    # print(image.get_attribute("src"))
    image_urls.append(image.get_attribute("src"))
image = image_urls[0]

def test_single(url):
    try:
        file_path = dir_path + "/" + "newTest" + ".jpg"
        urllib.request.urlretrieve(url, file_path)
    except Exception as e:
        print ("failed")
test_single(image)
# print(image_urls[0])