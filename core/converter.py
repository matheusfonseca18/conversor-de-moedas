from services.currency_api import pegar_cotacoes

def converter_moeda(valor, moeda_origem, moeda_destino):
    taxa = pegar_cotacoes(moeda_origem, moeda_destino)
    if taxa:
        return valor * taxa
    return None
