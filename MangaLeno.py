import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
def dossier():
    os.chdir("Google Drive//Python//Web-Scrapper")

dossier()

from Download import *


"""

Initialisation

"""


path = r"C:\Users\Sylgi\Desktop\Manga Scrapper"
CompteurParcours = 0
Titre = "BrawlingGo"
url = "https://manganelo.com/chapter/brawling_go/chapter_0"

def Initialisation():
    os.chdir(path)
    if Titre not in os.listdir():
        os.mkdir(Titre)
    os.chdir(Titre)

Initialisation()

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Div = soup.findAll('div')
    L = []
    for item in Div:
        if ClasseDownload(item):
            L.append(item)
    M = L[0]
    ListeTag = M.findAll('img')
    ListeLiens = []
    for item in ListeTag:
        ListeLiens.append(item['src'])
    return ListeLiens



def Next(soup,urlsvg):
    NextUrl = "Fin du Manga"
    if urlsvg != "Fin du Manga":
        #Div = soup.findAll('div')
        A = soup.findAll('a')
        L = []
        """
        for item in Div:
            if ClasseNextDiv(item):
                L.append(item)
        for item in L: #Mettre L[0]
            if item.a.text == "NEXT CHAPTER":
                NextUrl = item.a['href']
            else:
                for tag in item.findChildren():
                    print(tag)
                    if ClasseNextListe(item):
                        NextUrl = tag['href']
        for item in L[0].findChildren():
            if item.a.text == "NEXT CHAPTER":
                NextUrl = item.a['href']
        """
        for a in A:
            if a.text == "NEXT CHAPTER":
                NextUrl = a['href']


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
        for urldown in ListeLiens:
            Download(urldown,str(u) + str(i))
            i += 1
        url = Next(soup,url)
        u+=1000


def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['container-chapter-reader'] or item['class'] == ['vung-doc'])
    return bool

def ClasseNextDiv(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['navi-change-chapter-btn'] or item['class'] == ['btn-navigation-chap'])
    return bool

def ClasseNextListe(tag):
    bool = False
    bool = 'class' in tag.attrs  and (tag['class'] ==['navi-change-chapter-btn-next','a-h'] or tag['class'] == ['next'])
    return bool




def Liste():
    ListeTitre = ["SuperbCaptain","Iron Ladies","DomesticNoKanojo"]
    ListeUrl = ["https://ww3.mangafox.online/the-superb-captain-in-the-city","https://ww3.mangafox.online/iron-ladies","https://ww3.mangafox.online/domestic-na-kanojo/chapter-1-i-want-to-become-an-adult-quickly-703387354022149"]
    for i in range(0,len(ListeTitre)-1):
        Titre = ListeTitre[i]
        url = ListeUrl[i]
        ParcourSoup(url)
