import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
def dossier():
    os.chdir("Google Drive//Python//Web-Scrapper")


#Ne marche que sur MangaReader


"""

Initialisation

"""

path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"
CompteurParcours = 0
Titre = "Manga"

def Initialisation():
    os.chdir(path)
    if Titre not in os.listdir():
        os.mkdir(Titre)
    os.chdir(Titre)

Initialisation()


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
    if soup.text.find("is not released") <0:
        Im = soup.findAll('img')[0]
        link = Im['src']
        download_url = link
    else:
        print("Fin du manga")
        download_url = "Fin du Manga"
    return [soup, download_url]



def Next(soup):
    NextUrl = ""
    Div = soup.findAll("div")
    for item in Div:
        if 'id' in item.attrs and item['id'] == 'imgholder':
            NextUrl = trunk + item.a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl







