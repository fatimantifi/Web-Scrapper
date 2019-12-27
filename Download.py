import requests
import urllib.request
import os


def Download(download_url,name):
    if download_url != "Fin du Manga":
        #On fait une requête et on cache le fait que l'on est un robot
        req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

        #on prend le content de la page en bytes
        web_byte = urllib.request.urlopen(req).read()

        #on écrit le content dans un fichier test et on lui file le bon format
        open(name + '.jpg','wb').write(web_byte)

