import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

if not API_URL or not API_KEY:
    raise ValueError("Variáveis de ambiente API_URL ou API_KEY não encontradas")

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
