from core.converter import converter_moeda
from services.currency_api import pegar_todos_dados
import pprint

moeda_origem = "BRL"
moeda_destino = "USD"
moedas = moeda_origem + moeda_destino
valor = 100

dados = pegar_todos_dados(moeda_origem, moeda_destino)

pprint.pprint(dados)

def main():
    resultado = converter_moeda(valor, moeda_origem, moeda_destino)

    if resultado:
        print(f"""{valor} {moeda_origem} é igual a {resultado:.2f} {moeda_destino}
teste {dados[moedas]['name'].split("/")[0]} e {dados[moedas]["name"].split("/")[1]}""")
    else:
        print("Erro na conversão de moeda.")

if __name__ == "__main__":
    main()
