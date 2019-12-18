import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "https://www.mangareader.net/tate-no-yuusha-no-nariagari/1/2"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

Im = soup.findAll('img')[0]

link = Im['src']

download_url = link

urllib.request.urlretrieve(link, 'text.jpg') 