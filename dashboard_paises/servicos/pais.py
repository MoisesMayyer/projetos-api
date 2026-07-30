from dashboard_paises.api.cliente import dados_do_pais
from dashboard_paises.servicos.formatador import formata_dados

def pesquisar_pais():
    nome_pais = input("Digite o nome do país: ")

    resposta = dados_do_pais(nome_pais)
    dados = formata_dados(resposta)

    for campo, valor in dados.items():
        print(f"{campo}: {valor}")