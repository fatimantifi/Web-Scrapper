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

path = r"C:\Users\Sylgi\Desktop\Manga Scrapper"
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

trunk = "https://ww3.mangafox.online"


url = trunk + "/super-x-ray-eyes/episode-1-123017033562831"
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




"""

Manga Fox : Suivant .find(class="next_prev") puis enfant btn"

Boucle sur les scr de class="list_img"

"""

# A creuser
Div = soup.findAll('div')
for item in Div:
    if 'class' in item.attrs:
        if item['class'] == "next_prev_chapter":
            print(item)