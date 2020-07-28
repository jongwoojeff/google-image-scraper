import requests
import webbrowser
import urllib.request
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.google.com/search?q=dog&rlz=1C1SQJL_enKR858KR858&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvyIThp8_qAhUcwosBHb2ZDwAQ_AUoAXoECBgQAw&biw=1920&bih=937'

# test opening browser
print("opening URL")
print("How many images?")
image_cnt = int(input())
print("Getting " + str(image_cnt) + " images...")
driver = webdriver.Chrome("./chromedriver")
driver.get(url)

element = driver.find_element_by_tag_name("body")

# check if url is valid

img_dir = "./image_folder/"
dir_path = img_dir + "test"
# make dir
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

urls = []

# test getting new HTML
def get_images(url):
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    # urls = []
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    
    valid_count = 0
    # get rid of stuff with no src attribute
    for line in images:
        img_url = line.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        img_url = urllib.parse.urljoin(url, img_url)
        valid_count += 1
        # get rid of HTTP GET key value pairs
        # try:
        #     pos = img_url.index("?")
        #     img_url = img_url[:pos]
        # except ValueError:
        #     pass
        # add method to check if url valid before appending?
        urls.append(img_url)

    print((str)(valid_count) + " valid images")

def test_multiple(urls):
    for i in range(len(urls)):
        try:
            file_path = dir_path + "/" + "test" + str(i) + ".jpg"
            urllib.request.urlretrieve(urls[i], file_path)
        except Exception as e:
            print ("failed at: " + str(i))

# getting duplicated images
# how to get full HTML?
while(len(urls) < image_cnt):
    get_images(url)
    element.send_keys(Keys.PAGE_DOWN)
test_multiple(urls)