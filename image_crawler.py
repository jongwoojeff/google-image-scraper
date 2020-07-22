# https://ecsimsw.tistory.com/entry/Google-image-crawler-Crawling-Scraping-python
import requests
import webbrowser
import urllib.request
import os
from bs4 import BeautifulSoup

# check if url is valid

url = "https://www.google.com/search?q=dog&rlz=1C1SQJL_enKR858KR858&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvyIThp8_qAhUcwosBHb2ZDwAQ_AUoAXoECBgQAw&biw=1920&bih=937"
img_dir = "./image_folder/"
dir_path = img_dir + "test"
# make dir
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

def make_soup(url):
    # Using headers to avoid getting detected as a bot
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    # html = urllib.request.urlopen(url)
    return BeautifulSoup(html, 'html.parser')

def get_images(url):
    soup = make_soup(url)
    urls = []
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
    test_multiple(urls)

def test_single(url):
    try:
        file_path = dir_path + "/" + "test" + ".jpg"
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
    

get_images(url)
# change plan
# cannot fully download images without opening webbrowser. 
# No netlify, just build normal crawler
# for netlify late people's face for attractiveness based on celebrity trained data.