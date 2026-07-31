from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from interface import paineis
from interface import tabelas
from servicos.pais import pesquisar_pais

console = Console()

opcoes_menu = [
    "\n[bold yellow][1][/bold yellow] Pesquisar país",
    "[bold yellow][2][/bold yellow] Comparar países",
    "[bold yellow][3][/bold yellow] Países por continente",
    "[bold yellow][4][/bold yellow] Histórico",
    "[bold yellow][5][/bold yellow] Favoritos",
    "[bold yellow][6][/bold yellow] Sair\n",
    ]


def exibir_titulo():
    titulo = text_titulo()
    console.print(
        Panel(
            titulo,
            title="🌍 Dashboard Países",
            subtitle="Dados via REST Countries",
            border_style="bold cyan",
            expand=True,
        )
    )


def text_titulo():
    from rich.text import Text
    texto = Text()
    texto.append("Bem-vindo(a) ao ", style="white")
    texto.append("Dashboard de Países", style="bold green")
    texto.append("!\nEscolha uma opção abaixo para continuar.", style="white")
    return texto


def exibir_opcoes():
    for opc in opcoes_menu:
        console.print(f"{opc}")


def capturar_escolha():

    escolha = Prompt.ask(
        "[bold cyan]Digite o número da opção desejada[/bold cyan]",
        choices=["1", "2", "3", "4", "5", "6"],
        default="6",
    )
    return escolha


def encaminhar_escolha(escolha: str):

    if escolha == "1":
        pais_a = pesquisar_pais()
        paineis.mostrar_painel_pais(pais_a)

    elif escolha == "2":
        pais_a = pesquisar_pais()
        pais_b = pesquisar_pais()
        tabelas.mostrar_tabela_comparacao(pais_a, pais_b)

    elif escolha == "3":
        print("esta função ainda nn foi adicionada")
        #paineis.mostrar_painel_continente(continentes)

    elif escolha == "4":
        #nao funcionando
        tabelas.mostrar_tabela_historico()

    elif escolha == "5":
        #nao funcionando
        tabelas.mostrar_tabela_favoritos()

    elif escolha == "6":
        console.print("\n[bold red]Encerrando o Dashboard de Países...[/bold red]")
        return False

    return True


def iniciar_menu():

    continuar = True
    while continuar:
        console.clear()
        exibir_titulo()
        exibir_opcoes()
        escolha = capturar_escolha()
        continuar = encaminhar_escolha(escolha)

        if continuar:
            Prompt.ask("\n[dim]Pressione ENTER para voltar ao menu[/dim]", default="")