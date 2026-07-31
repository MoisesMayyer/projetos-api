from dashboard_paises.api.cliente import dados_do_pais
from dashboard_paises.servicos.formatador import formata_dados


def pesquisar_pais() -> dict:
    nome_pais =input("digite o nome do país: ")

    resposta = dados_do_pais(nome_pais)
    dados = formata_dados(resposta)

    return dados

def comparar_paises(pais1, pais2):
    dados_pais = dados_do_pais(pais1)
    dados_pais2 = dados_do_pais(pais2)

    dados_pais = formata_dados(dados_pais)
    dados_pais2 = formata_dados(dados_pais2)

    return dados_pais, dados_pais2