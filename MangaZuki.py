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


path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"
CompteurParcours = 0
Titre = "Gangnam Romance"
url = "https://www.mangazuki.online/manga/gangnam-romance/chapter-1/"




Initialisation(Titre,url)

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
    ListeTag = []
    for item in L:
        ListeTag.append(item.find('img'))
    ListeLiens = []
    for item in ListeTag:
        t = item['src']
        n = t.find('https')
        ListeLiens.append(item['src'][n:])
    return ListeLiens



def Next(soup,urlsvg):
    NextUrl = "Fin du Manga"
    if urlsvg != "Fin du Manga":
        A = soup.findAll('a')
        L = []
        for a in A:
            if 'class' in a.attrs and a['class'] == ['btn','next_page']:
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
    bool = 'class' in item.attrs and (item['class'] == ['page-break'])
    return bool

def ClasseNextDiv(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['navi-change-chapter-btn'] or item['class'] == ['btn-navigation-chap'])
    return bool

def ClasseNextListe(tag):
    bool = False
    bool = 'class' in tag.attrs  and (tag['class'] ==['navi-change-chapter-btn-next','a-h'] or tag['class'] == ['next'])
    return bool


#https://whatstatus.co/manga/manga/world/chapter-0

def Liste():
    ListeTitre = ['Lust Awakening','QueenBe','Daily Life','Rental Girl','TakeaPeek','What she Fell','Holic']
    ListeUrl = ['https://www.mangazuki.online/manga/lust-awakening/lust-awakening-chapter-1/','https://www.mangazuki.online/manga/queen-bee/queen-bee-chapter-1/','https://www.mangazuki.online/manga/read-a-perverts-daily-life-manhwa/chapter-1/','https://www.mangazuki.online/manga/read-rental-girls/rental-girls-chapter-1/','https://www.mangazuki.online/manga/take-a-peek/take-a-peek-chapter-1/','https://www.mangazuki.site/manga/my-dick/chapter-1-22','https://www.mangazuki.site/manga/holic/chapter-1']
    for i in range(0,len(ListeTitre)-1):
        Titre = ListeTitre[i]
        Initialisation(Titre)
        url = ListeUrl[i]
        ParcourSoup(url)
