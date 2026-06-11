import json
import requests

URL_ALL = "https://restcountries.com/v2/all"
URLNAME = "https://restcountries.com/v2/name/brazil"


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisicao em: ", url)


def parsing(textoResposta):
    try:
        return json.loads(textoResposta)
    except:
        print("Erro ao fazer parsing")


if __name__ == "__main__":
    textoResposta = requisicao(URL_ALL)
    if textoResposta:
        textoRespostaDepoisParsing = parsing(textoResposta)
        if textoRespostaDepoisParsing:
            print(textoRespostaDepoisParsing)