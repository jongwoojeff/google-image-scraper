import requests
import threading
import urllib.request
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.google.com/search?q=dog&source=lnms&tbm=isch&sa=X&ved=2ahUKEwis942FiKTrAhXbMHAKHZT7BwMQ_AUoAXoECBoQAw&biw=1440&bih=789"

dir_path = "./image_folder/" + "test"
if not os.path.exists(dir_path):
  os.makedirs(dir_path)

def get_image_urls(url):
    # driver = webdriver.Chrome("./chromedriver")
    driver = webdriver.Chrome("/Users/jeff/Desktop/chromedriver")
    driver.get(url)
    
    elem = driver.find_element_by_tag_name("body")

    for i in range(10):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    print("Reached end of the search result")

    photo_grid_boxes = driver.find_elements_by_xpath('//div[@class="bRMDJf islir"]')

    image_urls = []

    for box in photo_grid_boxes:
        try:
            imgs = box.find_elements_by_tag_name("img")
            for img in imgs:
                src = img.get_attribute("src")
                # Google preloads 20 images as base64
                if str(src).startswith('data:'):
                    src = img.get_attribute("data-iurl")
                image_urls.append(src)

        except Exception:
            print("Error: System Crashed. Returning saved image urls.")
            return image_urls

    print("Found " + str(len(image_urls)) + " image urls")
    return image_urls

# get_image_urls(url)

def fetch_url(url, i):
      try:
        file_path = dir_path + "/" + "test" + str(i) + ".jpg"
        # urllib.request.urlretrieve(urls[i], file_path)
        # second method
        response = urllib.request.urlopen(url)
        image = response.read()
        with open(file_path, "wb") as file:
            file.write(image)
        
      except Exception:
        print("shit")

urls = get_image_urls(url)

for i in range(len(urls)):
  # processThread = threading.Thread(target=fetch_url, args=(urls[i], i))
  # processThread.start()
  fetch_url(urls[i], i)