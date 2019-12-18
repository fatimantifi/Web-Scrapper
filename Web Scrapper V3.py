import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

def dossier():
    os.chdir("Google Drive//Python//Web-Scrapper")


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

Télécharger l'image

"""


#On fait une requête et on cache le fait que l'on est un robot
req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

#on prend le content de la page en bytes
web_byte = urllib.request.urlopen(req).read()

#on écrit le content dans un fichier test et on lui file le bon format
open('test.jpg','wb').write(web_byte)

