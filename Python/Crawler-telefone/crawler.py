import requests
from bs4 import BeautifulSoup

URL = "https://django-anuncios.solyd.com.br/"

def buscar(url):
    try:
        respota = requests.get(url)
        if respota.status_code == 200:
            print(respota.text)
        else:
            print("Erro ao fazer requisição")
    except Exception as error:
        print("Erro ao fazer requisição")
        print(error)


def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)

def encontrar_links(texto):
    cards_pai = soup.find("div", {"class": "card"})
    cards = cards_pai.findAll('a')

    links = []
    for card in cards:
        link = card['href']
        links.append(link)

    return links


def encontrar_telefones(link):
    try:
        respota = requests.get(link)
        if respota.status_code == 200:
            print(respota.text)
        else:
            print("Erro ao fazer requisição")
    except Exception as error:
        print("Erro ao fazer requisição")
        print(error)


resposta = buscar(URL)
if resposta:
    soup = parsing(resposta)
    if soup:
        links = encontrar_links(soup)
        print(links)