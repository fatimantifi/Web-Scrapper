import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

def dossier():
    os.chdir("Google Drive//Python//Web-Scrapper")

CompteurParcours = 0


"""

Navigation dans la page Web

"""

trunk = "https://www.mangareader.net"


url = trunk + "/tate-no-yuusha-no-nariagari/1/2"
response = requests.get(url)





"""

Recherche de l'image dans la page web

"""

def Navigate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    Im = soup.findAll('img')[0]
    link = Im['src']
    download_url = link
    return [soup, download_url]


"""

Télécharger l'image

"""

def Download(download_url,name):
    #On fait une requête et on cache le fait que l'on est un robot
    req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

    #on prend le content de la page en bytes
    web_byte = urllib.request.urlopen(req).read()

    #on écrit le content dans un fichier test et on lui file le bon format
    open(name + '.jpg','wb').write(web_byte)




"""

Recherche du imgholder (qui permet d'aller à la page suivante)

"""

def Next(soup):
    L = soup.find(id = "imgholder")
    M = L.findChildren()
    CompteurParcours = 0
    NewAdd = ParcoursSoup(M)
    #NouvelleUrl = trunk + NewAdd
    return NouvelleUrl


def ParcoursSoup(M,CompteurParcours):
    try :
        NewAdd = M[CompteurParcours]['href']
    except:
        CompteurParcours +=1
        NewAdd = ParcoursSoup(M,CompteurParcours)
    return [NewAdd,CompteurParcours]


