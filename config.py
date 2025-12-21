API_URL = "https://economia.awesomeapi.com.br/json/last/{moedas}?token={api_key}"
API_KEY = "f93f6d97445a4a6c87ea751d6f48ce12b5ae1de289be2e02fa2fa0e6f5ee7b71"


# API_URL = "https://economia.awesomeapi.com.br/json/last/{moedas}?token={API_KEY}"

# API_KEY = "f93f6d97445a4a6c87ea751d6f48ce12b5ae1de289be2e02fa2fa0e6f5ee7b71"

# import requests
# import pprint

# def pegar_cotacoes(moedas):
#     url = api_URL.format(moedas=moedas, api_key=api_key)
#     resposta = requests.get(url)
#     print(resposta.status_code)
#     if resposta.status_code == 200:
#         dados = resposta.json()
#         pprint.pprint(dados)
#         nome = dados['BRLEUR']['name']
#         convert = dados['BRLEUR']['ask']
#         print(f'A cotação de {nome} é {convert}')
#     else:
#         print({"error": resposta.status_code})

# moeda1 = "BRL"
# moeda2 = "EUR"

# moedinhas = f'{moeda1}-{moeda2}'

# pegar_cotacoes(moedinhas)