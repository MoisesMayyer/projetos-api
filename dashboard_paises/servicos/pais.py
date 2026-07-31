from dados.historico import (
    carregar_historico,
    adicionar_historico
)

from dashboard_paises.api.cliente import dados_do_pais

from dashboard_paises.servicos.formatador import formata_dados


historico_paises = carregar_historico()


def pesquisar_pais(nome_pais: str, acao="Pesquisa simples") -> dict:
    resposta = dados_do_pais(nome_pais)
    dados = formata_dados(resposta)

    ja_existe = any(
        pais["nome"] == dados["nome"]
        for pais in historico_paises
    )

    if not ja_existe:
        adicionar_historico(
            nome_pais=dados["nome"],
            acao=acao
        )

    return dados


def comparar_paises(pais1: str, pais2: str) -> tuple[dict, dict]:
    dados_pais1 = pesquisar_pais(
        nome_pais=pais1,
        acao="Comparação"
    )

    dados_pais2 = pesquisar_pais(
        nome_pais=pais2,
        acao="Comparação"
    )

    return dados_pais1, dados_pais2
