import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
from Download import *

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


"""

Télécharger l'image

"""



"""

Recherche du imgholder (qui permet d'aller à la page suivante)

"""

def Next(soup):
    if download_url != "Fin du Manga":
        L = soup.find(id = "imgholder")
        M = L.findChildren()
        CompteurParcours = 0
        NewAdd = ListeToString(ParcoursSoup(M,CompteurParcours))
        NouvelleUrl = trunk + NewAdd
    else:
        NouvelleUrl = "Fin du Manga"
    print(NouvelleUrl)
    return NouvelleUrl


def ParcoursSoup(M,CompteurParcours):
    try :
        NewAdd = M[CompteurParcours]['href']
    except:
        CompteurParcours +=1
        NewAdd = ParcoursSoup(M,CompteurParcours)
    return [NewAdd,CompteurParcours]

def ListeToString(L):
    M = L
    if type(M) == type([]):
        M = M[0]
        M = ListeToString(M)
    return M


"""

Implémentation d'une boucle

"""

#L'url doit être la première page

def DownloadManga(url):
    NouvelleUrl = url
    i = 0
    while NouvelleUrl != "Fin du Manga":
        [soup,download_url] = Navigate(NouvelleUrl)
        Download(download_url,Titre + str(i))
        i += 1
        NouvelleUrl = Next(soup)








"""

Manga Fox : Suivant .find(class="next_prev") puis enfant btn"

Boucle sur les scr de class="list_img"

"""