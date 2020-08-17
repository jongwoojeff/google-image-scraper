import requests
import threading
from bs4 import BeautifulSoup
import os # not mandatory

URLS = [
  'https://pastpapers.papacambridge.com/?dir=Cambridge%20International%20Examinations%20%28CIE%29/AS%20and%20A%20Level/Business%20%28for%20first%20examination%20in%202016%29%20-%209609/2019-May-June',
  'https://pastpapers.papacambridge.com/?dir=Cambridge%20International%20Examinations%20%28CIE%29/AS%20and%20A%20Level/Business%20%28for%20first%20examination%20in%202016%29%20-%209609/2018-Oct-Nov',
  'https://pastpapers.papacambridge.com/?dir=Cambridge%20International%20Examinations%20%28CIE%29/AS%20and%20A%20Level/Business%20%28for%20first%20examination%20in%202016%29%20-%209609/2018-May-June',
  'https://pastpapers.papacambridge.com/?dir=Cambridge%20International%20Examinations%20%28CIE%29/AS%20and%20A%20Level/Business%20%28for%20first%20examination%20in%202016%29%20-%209609/2018-March'
]

def downloadPage(URL, folder):
  os.mkdir(folder) # create folder
  BASEURL = 'https://pastpapers.papacambridge.com/'
  download_urls = []

  page = requests.get(URL).text # get the raw HTML of the page
  soup = BeautifulSoup(page) # make our page easy to navigate

  for a in soup.find_all('a'): # iterate through every <a> tag on the page
    href = a['href'] # get the href attribute of the tag
    if a.text == 'Download': # if the link ends in .pdf
      downloadLink = BASEURL + href # create the download url
      download_urls.append(downloadLink) # add the link to our array

  for file in download_urls: # for each index and file in download_urls
    fileName = file.split('/')[-1] # the text after the last / is the file name we want
    fileRequest = requests.get(file) # download the file
    with open(os.path.join(folder, fileName), 'wb') as examFile: # open a new file in write and binary mode
      examFile.write(fileRequest.content) # write the content of the downloaded file

for url in URLS:
  folderName = url.split('/')[-1] # the name of the folder
  processThread = threading.Thread(
    target=downloadPage, args=(url, folderName)) # parameters and functions have to be passed separately
  processThread.start() # start the thread