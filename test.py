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
driver = webdriver.Chrome("./chromedriver")
# driver = webdriver.Chrome("/Users/jeff/Desktop/chromedriver")
driver.get(url)

element = driver.find_element_by_tag_name("body")
image_urls=[]
# imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(7)))
# imgurl.click()
# images = driver.find_elements_by_class_name("n3VNCb")

for i in range(1,10):
    imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(i)))
    imgurl.click()

    #select image from the popup
    time.sleep(3)
    images = driver.find_elements_by_class_name("n3VNCb")
    for image in images:
    # print(image.get_attribute("src"))
        # if (image.get_attribute("src")[-3:].lower() in ["jpg","png","jpeg"]):
        if (image.get_attribute("src")[0:5] == "https"):
            # print(image.get_attribute("src")[0:5])
            image_urls.append(image.get_attribute("src"))
    
    driver.execute_script("window.scrollTo(0, "+str(i*150)+");")

# for image in images:
#     # print(image.get_attribute("src"))
#     image_urls.append(image.get_attribute("src"))
# image = image_urls[0]
print(len(image_urls))
def test_single(url):
    try:
        file_path = dir_path + "/" + "newTest" + ".jpg"
        urllib.request.urlretrieve(url, file_path)
    except Exception as e:
        print ("failed")

def test_multiple(urls):
    for i in range(len(urls)):
        try:
            file_path = dir_path + "/" + "test" + str(i) + ".jpg"
            urllib.request.urlretrieve(urls[i], file_path)
        except Exception as e:
            print ("failed at: " + str(i))
# test_single(image)
# print(image_urls[0])
image_urls = list(dict.fromkeys(image_urls))
test_multiple(image_urls)