import requests
import urllib.request
import time
from bs4 import BeautifulSoup

"""

Navigation dans la page Web

"""



url = "https://www.mangareader.net/tate-no-yuusha-no-nariagari/1/2"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

Im = soup.findAll('img')[0]

link = Im['src']

download_url = link



"""

Arriver à télécharger l'image

"""



req = Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})


web = urlretrieve(req)
web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')








class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(link)



#urllib.request.urlretrieve(link, 'text.jpg') 