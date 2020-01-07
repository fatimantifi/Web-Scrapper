import requests
import urllib.request
import os
from PIL import Image
import shutil
def dossier():
    os.chdir("Google Drive//Python//Web-Scrapper")

dossier()
import MangaFoxScrapper as MF
import MangaLeno as ML
import MangaReaderScrapper as MR
import MangaZuki as MZ




def Download(download_url,name):
    if download_url != "Fin du Manga":
        if download_url != "https://s3.mangareader.net/images/erogesopt.jpg":
            #On fait une requête et on cache le fait que l'on est un robot
            req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

            #on prend le content de la page en bytes
            web_byte = urllib.request.urlopen(req).read()

            #on écrit le content dans un fichier test et on lui file le bon format
            open(name + '.jpg','wb').write(web_byte)


def Compression():
    os.mkdir("Compr")
    ListeNon = []
    for elt in os.listdir():
        try:
            print(elt)
            im = Image.open(elt)
            im.save("Compr/" + elt,quality = 50, optimize = True)
        except:
            try:
                shutil.copy(elt,"Compr/" + elt)
            except:
                print("Erreur pour elt")
                ListeNon.append(elt)
    return ListeNon


def Initialisation(Titre):
    os.chdir(path)
    if Titre not in os.listdir():
        os.mkdir(Titre)
    os.chdir(Titre)


class Site:
    def __init__(self,url,Titre):
        self.url = url
        self.soup = ""
        self.ListeLiens = []
        self.Titre = Titre

    def Navigate(self):
        if 'mangafox' in self.url:
            [self.soup,self.ListeLiens] = MF.Navigate(self.url)
        if 'manganelo' in self.url:
            [self.soup,self.ListeLiens] = ML.Navigate(self.url)
        if 'mangareader' in self.url:
            [self.soup,self.ListeLiens] = MR.Navigate(self.url)
        if 'mangazuki' in self.url:
            [self.soup,self.ListeLiens] = MZ.Navigate(self.url)


    def Next(self):
        if 'mangafox' in self.url:
            self.url = MF.Next(self.soup)
        if 'manganelo' in self.url:
            self.url = ML.Next(self.soup)
        if 'mangareader' in self.url:
            self.url = MR.Next(self.soup)
        if 'mangazuki' in self.url:
            self.url = MZ.Next(self.soup)

    def ParcourSoup(self):
        u = 0
        while self.url != "Fin du Manga":
            [self.soup,self.ListeLiens] = self.Navigate()
            i = 0
            for urldown in self.ListeLiens:
                Download(urldown,str(u) + str(i))
                i += 1
            self.url = self.Next(self.soup,url)
            u+=1000


