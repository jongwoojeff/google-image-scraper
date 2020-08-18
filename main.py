# https://github.com/YoongiKim/AutoCrawler/blob/master/collect_links.py
# try box grid method for gathering image urls
import image_scraper as ims
import urllib.request
import threading

keyword, img_count = ims.get_input()
url = ims.url_builder(keyword)
image_urls = ims.get_image_urls(url, img_count)
path = ims.make_dir(keyword)
ims.download_images(image_urls, path, keyword, img_count)

# add a function to continue downloading for more