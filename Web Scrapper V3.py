import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')

one = soup.findAll('a')[36]
link = one['href']

download_url = 'http://web.mta.info/developers/'+ link

urllib.request.urlretrieve(download_url,"./'"+link[link.find('/turnstile_')+1:]) 