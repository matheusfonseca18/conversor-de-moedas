import requests
from config import API_URL, API_KEY


def montar_url(moeda_origem, moeda_destino):
    chave_url = f"{moeda_origem}-{moeda_destino}"
    return API_URL.format(moedas=chave_url, api_key=API_KEY)


def call_api(moeda_origem, moeda_destino):
    url = montar_url(moeda_origem, moeda_destino)
    resposta = requests.get(url)
    if resposta.status_code != 200:
        print({"error": resposta.status_code})
        return None
    return resposta


def pegar_cotacoes(moeda_origem, moeda_destino):

    resposta = call_api(moeda_origem, moeda_destino)

    if resposta is None:
        return None

    dados = resposta.json()
    chave_json = f"{moeda_origem}{moeda_destino}"
    return float(dados[chave_json]["ask"])

def pegar_todos_dados(moeda_origem, moeda_destino):

    resposta = call_api(moeda_origem, moeda_destino)

    if resposta is None:
        return None

    return resposta.json()
