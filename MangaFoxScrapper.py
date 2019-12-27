import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
#from Download import *

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

url = trunk + "/favorite-part/chapter-1-324246019529673"
response = requests.get(url)



"""

Recherche de l'image dans la page web

"""

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Div = soup.findAll('div')
    for item in Div:
        if 'class' in item.attrs and item['class'] == ['list_img']:
            L = item.findChildren()
    ListeLiens = []
    for item in L:
        ListeLiens.append(item['src'])
    return ListeLiens






"""

Manga Fox : Suivant .find(class="next_prev") puis enfant btn"

Boucle sur les scr de class="list_img"

"""


def Next(soup,urlsvg):
    NextUrl = "Fin du Manga"
    if urlsvg != "Fin du Manga":
        Div = soup.findAll('div')
        L = []
        for item in Div:
            if 'class' in item.attrs and item['class'] == ['next_prev_chapter']:
                if item['class'] == ['next_prev_chapter']: #A supprimer
                    L.append(item)

        M = L[0]
        NextUrl ="Fin du Manga"
        for item in M.findChildren():
            if 'title' in item.attrs and item['title'] == 'Next Chapter':
                NextUrl = item['href']
        if NextUrl == "":
            NextUrl = "Fin du Manga"
        print(NextUrl)
    return NextUrl

def ParcourSoup(urldebut):
    url = urldebut
    u = 0
    while url != "Fin du Manga":
        [soup,ListeLiens] = Navigate(url)
        i = 0
        for url in ListeLiens:
            Download(url,str(u) + str(i))
            i += 1
        url = Next(soup,url)
        u+=1
