import requests
import webbrowser
import urllib.request
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_input():
    print("Enter a keyword")
    keyword = input()
    print("Enter a number of " + keyword + " images to get")
    img_count = input()
    valid_input = False
    while (valid_input == False):
        try:
            img_count = int(img_count)
            if (img_count > 1):
                valid_input = True
            else:
                print("Number must be greater than 1")
                img_count = input()
        except ValueError:
            print("That's not an integer!") 
            img_count = input()      
    
    return keyword, img_count

def url_builder(keyword):
    url = "https://www.google.com/search?q=" + keyword + "&rlz=1C1SQJL_enKR858KR858&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvyIThp8_qAhUcwosBHb2ZDwAQ_AUoAXoECBgQAw&biw=1920&bih=937"
    return url

def get_image_urls(url, img_count):
    driver = webdriver.Chrome("./chromedriver")
    # driver = webdriver.Chrome("/Users/jeff/Desktop/chromedriver")
    driver.get(url)

    # element = driver.find_element_by_tag_name("body")
    image_urls=[]
    # imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(7)))
    # imgurl.click()
    # images = driver.find_elements_by_class_name("n3VNCb")
    try:
        for i in range(1,img_count+1):
            # todo
            # avoid clicking related search
            imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(i)))
            imgurl.click()

            # select image from the popup
            # 2 sceonds is more accurate than 1 
            time.sleep(2)
            images = driver.find_elements_by_class_name("n3VNCb")
            for image in images:
                # print(image.get_attribute("src"))
                # if (image.get_attribute("src")[-3:].lower() in ["jpg","png","jpeg"]):
                if (image.get_attribute("src")[0:5] == "https"):
                    if (image.get_attribute("src")[8:17] == "encrypted"):
                        continue
                    image_urls.append(image.get_attribute("src"))
        driver.execute_script("window.scrollTo(0, "+str(i*150)+");")
    except Exception: 
        # more than 40 keeps failing dont know why
        print("Error: System Crashed. Returning saved image urls.")
        # driver.close()
        return image_urls
    # for image in images:
    #     # print(image.get_attribute("src"))
    #     image_urls.append(image.get_attribute("src"))
    
    # image_urls = list(dict.fromkeys(image_urls))
    print("Found " + str(len(image_urls)) + " valid image urls")
    return image_urls


def make_dir(keyword):
    dir_path = "./image_folder/" + keyword
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

# add method to multi thread downloading process
def download_images(urls, dir_path, keyword):
    print("Downloading...")
    # save urls to image
    success_count = 0
    fail_count = 0
    for i in range(len(urls)):
        try:
            file_path = dir_path + "/" + keyword + str(success_count + 1) + ".jpg"
            # urllib.request.urlretrieve(urls[i], file_path)
            # second method
            response = urllib.request.urlopen(urls[i])
            image = response.read()
            with open(file_path, "wb") as file:
                file.write(image)

            success_count += 1
        except Exception as e:
            fail_count += 1
    print("Failed to download " + str(fail_count) + " images")
    print("Downloaded " + str(success_count) + " images")
# path for mac
# driver = webdriver.Chrome("./chromedriver")
# driver = webdriver.Chrome("/Users/jeff/Desktop/chromedriver")
# driver.get(url_builder("dog"))

# element = driver.find_element_by_tag_name("body")
# image_urls=[]
# imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(7)))
# imgurl.click()
# images = driver.find_elements_by_class_name("n3VNCb")

# for i in range(1,100):
#     imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div[%s]//a[1]//div[1]//img[1]'%(str(i)))
#     imgurl.click()

#     #select image from the popup
#     # 2 sceonds is more accurate than 1 
#     time.sleep(2)
#     images = driver.find_elements_by_class_name("n3VNCb")
#     for image in images:
#     # print(image.get_attribute("src"))
#         # if (image.get_attribute("src")[-3:].lower() in ["jpg","png","jpeg"]):
#         if (image.get_attribute("src")[0:5] == "https"):
#             # print(image.get_attribute("src")[0:5])
#             if (image.get_attribute("src")[8:17] == "encrypted"):
#                 continue
#             image_urls.append(image.get_attribute("src"))
    
#     driver.execute_script("window.scrollTo(0, "+str(i*150)+");")
# for image in images:
#     # print(image.get_attribute("src"))
#     image_urls.append(image.get_attribute("src"))
# image = image_urls[0]

# def test_multiple(urls):
#     for i in range(len(urls)):
#         try:
#             file_path = dir_path + "/" + "test" + str(i) + ".jpg"
#             # print ("success at: " +str(i) + " "+ urls[i])
#             urllib.request.urlretrieve(urls[i], file_path)
#         except Exception as e:
#             print ("failed at: " + str(i))

# test_single(image)
# print(image_urls[0])

# image_urls = list(dict.fromkeys(image_urls))
# test_multiple(image_urls)