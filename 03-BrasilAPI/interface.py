from api import consultar_cep
from historico import carregar_json

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def exibir_cabecalho():
    console.print(
        Panel.fit(
            "[bold cyan]Sistema de Consulta de CEP[/bold cyan]",
            border_style="cyan",
        )
    )


def exibir_menu():
    console.print()
    console.print("[bold]1[/bold] - Consultar CEP")
    console.print("[bold]2[/bold] - Ver histórico")
    console.print("[bold]3[/bold] - Sair")
    console.print()


def formatacao(dados: dict, titulo: str = "Resultado"):
    tabela = Table(title=titulo, show_header=True, header_style="bold magenta")
    tabela.add_column("Campo", style="cyan", no_wrap=True)
    tabela.add_column("Valor", style="white")

    for campo, valor in dados.items():
        tabela.add_row(str(campo), str(valor))

    console.print(tabela)


def opcao_consultar_cep():
    cep = Prompt.ask("[yellow]Digite o CEP[/yellow]")

    dados = consultar_cep(cep)

    if dados:
        formatacao(dados, titulo=f"CEP {cep}")
    else:
        console.print("[bold red]CEP não encontrado[/bold red]")


def opcao_ver_historico():
    historico = carregar_json()

    if historico:
        console.print(f"\n[bold]Histórico[/bold] ({len(historico)} registro(s))\n")
        for i, cep in enumerate(historico, start=1):
            formatacao(cep, titulo=f"Registro {i}")
    else:
        console.print("[yellow]Nenhum histórico encontrado[/yellow]")


opcoes_menu = {
    "1": ("Consultar CEP", opcao_consultar_cep),
    "2": ("Ver histórico", opcao_ver_historico),
    "3": ("Sair", None),
}
