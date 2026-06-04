import requests

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


buscar(URL)