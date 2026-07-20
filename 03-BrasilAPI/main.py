from rich.console import Console
from rich.prompt import Prompt

from interface import exibir_cabecalho, exibir_menu, opcoes_menu


console = Console()


def main():
    exibir_cabecalho()

    while True:
        exibir_menu()

        opcao = Prompt.ask(
            "Escolha uma opção",
            choices=list(opcoes_menu.keys())
        )

        if opcao == "3":
            console.print("[bold red]Saindo...[/bold red]")
            break

        funcao = opcoes_menu[opcao][1]
        funcao()


if __name__ == "__main__":
    main()