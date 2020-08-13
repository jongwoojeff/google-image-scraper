# https://github.com/YoongiKim/AutoCrawler/blob/master/collect_links.py
# https://markhneedham.com/blog/2018/07/15/python-parallel-download-files-requests/
# try box grid method for gathering image urls
import image_scraper as ims
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool

keyword, img_count = ims.get_input()
url = ims.url_builder(keyword)
image_urls = ims.get_image_urls(url, img_count)
path = ims.make_dir(keyword)
# ims.download_images(image_urls, path, keyword, img_count)

# multiprocessing
print("There are {} CPUs on this machine ".format(cpu_count()))

# pool = Pool(cpu_count())
# download_func = partial(ims.download_images, image_urls = image_urls, path = path, img_count = img_count)
# results = pool.map(download_func, image_urls)
# pool.close()
# pool.join()
results = ThreadPool(8).imap_unordered(ims.download_images, image_urls = image_urls, path = path, img_count = img_count)
for path in results:
    print(path)

# add a function to continue downloading for more