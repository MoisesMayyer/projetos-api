from rich.console import Console
from rich.table import Table

from dados.historico import carregar_historico

console = Console()


def mostrar_tabela_comparacao(dado_pais1, dado_pais2):

    tabela = Table(
        title=f"Comparação: {dado_pais1['nome']} x {dado_pais2['nome']}",
        show_header=True,
        header_style="bold cyan",
        border_style="blue",
    )

    tabela.add_column("Informação", style="bold white")
    tabela.add_column(
        dado_pais1["nome"],
        justify="center",
        style="green"
    )
    tabela.add_column(
        dado_pais2["nome"],
        justify="center",
        style="red"
    )

    tabela.add_row(
        "Código",
        dado_pais1["codigo_pais"],
        dado_pais2["codigo_pais"]
    )

    tabela.add_row(
        "Capital",
        dado_pais1["capital"],
        dado_pais2["capital"]
    )

    tabela.add_row(
        "Continente",
        dado_pais1["continente"],
        dado_pais2["continente"]
    )

    tabela.add_row(
        "Região",
        dado_pais1["regiao"],
        dado_pais2["regiao"]
    )

    tabela.add_row(
        "Sub-região",
        dado_pais1["sub_regiao"],
        dado_pais2["sub_regiao"]
    )

    tabela.add_row(
        "População",
        f"{dado_pais1['populacao']:,}",
        f"{dado_pais2['populacao']:,}"
    )

    tabela.add_row(
        "Área territorial",
        f"{dado_pais1['area_territorial']:,} km²",
        f"{dado_pais2['area_territorial']:,} km²"
    )

    tabela.add_row(
        "Idiomas",
        ", ".join(dado_pais1["idiomas"]),
        ", ".join(dado_pais2["idiomas"])
    )

    tabela.add_row(
        "Moedas",
        ", ".join(dado_pais1["moedas"]),
        ", ".join(dado_pais2["moedas"])
    )

    tabela.add_row(
        "Fuso horário",
        ", ".join(dado_pais1["fuso_horarios"]),
        ", ".join(dado_pais2["fuso_horarios"])
    )

    console.print(tabela)


def mostrar_tabela_favoritos():

    tabela = Table(
        title="Países Favoritos",
        show_header=True,
        header_style="bold yellow",
        border_style="yellow",
    )

    tabela.add_column("País", style="bold white")
    tabela.add_column("Capital", justify="center")
    tabela.add_column("Continente", justify="center")
    tabela.add_column("População", justify="right")


    console.print(tabela)


def mostrar_tabela_historico():
    paises_historico = carregar_historico()

    tabela = Table(
        title="Histórico de Pesquisas",
        show_header=True,
        header_style="bold magenta",
        border_style="magenta",
    )

    tabela.add_column("nome", style="dim")
    tabela.add_column("país pesquisado", style="bold white")
    tabela.add_column("Ação", justify="center")


    if paises_historico:
        for pesquisa in paises_historico:
            tabela.add_row(
                pesquisa["data"],
                pesquisa["pais"],
                pesquisa["acao"]
            )

    console.print(tabela)