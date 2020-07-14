# https://ecsimsw.tistory.com/entry/Google-image-crawler-Crawling-Scraping-python
import requests
import webbrowser
import urllib.request
from bs4 import BeautifulSoup

url = "https://jongwoojeff.github.io/"

def make_soup(url):
    html = urllib.request.urlopen(url)
    return BeautifulSoup(html, 'html.parser')

def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")

get_images(url)