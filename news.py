import requests
from bs4 import BeautifulSoup
from datetime import date
import colorama as color
import termcolor as colors
color.init()

# Funkcje


def status(address_url, nazwa_strony):

    """ Sprawdza czy serwer strony zwraca odpowiedź i jest dostępny"""

    url = address_url
    info = requests.get(url, headers = {'User-Agent':'Firefox/80.0.1 (64)'}) # Nagłówek przeglądarki by ominąć blokadę
    status_url = info.status_code
    if status_url == 200:
        print("  ", nazwa_strony, "--")
        print(colors.colored("   [Działa]", "green"))
    else:
        print("  ", nazwa_strony, "--")
        print(colors.colored("   [Nie działa]", "red"))


def lista(adres, dzien):

    """ Pobiera adresy url z ogłoszeniami"""

    file = open("newsy.txt", "w")
    url = adres
    info = requests.get(url, headers = {'User-Agent':'Firefox/80.0.1 (64)'})
    html = info.text
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('item')
    for i in tags:
        tytul = i.find('title')
        tytul = str(tytul)
        tytul = tytul[7:]
        tytul = tytul[:-8]
        data = i.find('pubdate')
        data = str(data)
        dzien_2 = int(data[14:16])
        if dzien == dzien_2:
            print(" ", tytul)
            file.writelines(tytul + "\n")
            print("------------------------------------------------------------")
    file.close()

def datka():

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    dzieniuch=  int(d1[:2])
    return dzieniuch


status('https://news.google.com/rss/search?q=bitcoin', 'Google')
dzien = datka()
zwrot = str(input("\n  Szukane słowo:  \n  "))
print(" ")
print(colors.colored("##########################", "yellow"))
print("  [", zwrot, " - wiadomości z ostatniej godziny]")
print(colors.colored("##########################", "yellow"))
print(" ")
szukan = 'https://news.google.com/rss/search?q=' + zwrot + '%20when%3A1h&hl=en-US&gl=US&ceid=US%3Aen'
lista(szukan, dzien)
input("Koniec..")
