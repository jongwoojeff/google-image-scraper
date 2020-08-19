# try box grid method for gathering image urls
import image_scraper as ims
# import time

thread = ims.download_whole()
if (thread == True):
    print("Enter a keyword")
    keyword = input()
else:
    keyword, img_count = ims.get_input()

start_time = ims.time.time()

url = ims.url_builder(keyword)
image_urls = ims.get_image_urls(url)
path = ims.make_dir(keyword)

if (thread == True):
    ims.set_multithread(image_urls, path, keyword)
else:
    ims.download_images(image_urls, path, keyword, img_count)

print("---Took %s seconds ---" % (ims.time.time() - start_time))
