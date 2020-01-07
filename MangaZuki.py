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
Titre = "Gangnam Romance"
url = "https://www.mangazuki.online/manga/gangnam-romance/chapter-1/"

def Initialisation(Titre):
    os.chdir(path)
    if Titre not in os.listdir():
        os.mkdir(Titre)
    os.chdir(Titre)

Initialisation(Titre)

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
        #Div = soup.findAll('div')
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




def Liste():
    ListeTitre = ["Fall In Love Because Of You","Vicious Luck","Yami no Chikara","Special Eyes","SatsurikuKuindeddoOnnaShikeishuu","Chichi no Jukan","The World of Moral Reversal","Tamorawa"]
    ListeUrl = ["https://manganelo.com/chapter/mt921341/chapter_1","https://manganelo.com/chapter/ki921326/chapter_1","https://mangakakalot.com/chapter/yn918383/chapter_1","https://manganelo.com/chapter/ad921328/chapter_1","https://mangakakalot.com/chapter/es921638/chapter_1","https://mangakakalot.com/chapter/kc921212/chapter_1","https://mangakakalot.com/chapter/the_world_of_moral_reversal/chapter_1","https://mangakakalot.com/chapter/oj920167/chapter_1"]
    for i in range(0,len(ListeTitre)-1):
        Titre = ListeTitre[i]
        Initialisation(Titre)
        url = ListeUrl[i]
        ParcourSoup(url)
