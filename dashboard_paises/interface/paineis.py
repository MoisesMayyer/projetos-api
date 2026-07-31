from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

console = Console()


def montar_texto_pais(dados: dict) -> Text:

    texto = Text()

    texto.append(f"🌎  {dados['nome']}", style="bold green")
    texto.append(f" ({dados['codigo_pais']})\n\n", style="dim")

    texto.append("Nome oficial: ", style="bold cyan")
    texto.append(f"{dados['nome_oficial']}\n")

    texto.append("Capital: ", style="bold cyan")
    texto.append(f"{dados['capital']}\n")

    texto.append("Continente: ", style="bold cyan")
    texto.append(f"{dados['continente']}\n")

    texto.append("Região / Sub-região: ", style="bold cyan")
    texto.append(f"{dados['regiao']} / {dados['sub_regiao']}\n")

    texto.append("População: ", style="bold cyan")
    texto.append(f"{dados['populacao']:,}\n")

    texto.append("Área territorial: ", style="bold cyan")
    texto.append(f"{dados['area_territorial']:,} km²\n")

    texto.append("Idiomas: ", style="bold cyan")
    texto.append(f"{', '.join(dados['idiomas'])}\n")

    texto.append("Moedas: ", style="bold cyan")
    texto.append(f"{', '.join(dados['moedas'])}\n")

    texto.append("Fuso horário: ", style="bold cyan")
    texto.append(f"{', '.join(dados['fuso_horarios'])}\n")

    texto.append("Bandeira: ", style="bold cyan")
    texto.append(f"{dados['bandeira_url']}\n")

    return texto


def mostrar_painel_pais(dados_formatados_1):

    dados = dados_formatados_1
    conteudo = montar_texto_pais(dados)

    painel = Panel(
        conteudo,
        title="[bold white]Detalhes do País[/bold white]",
        border_style="green",
        padding=(1, 2),
        expand=True,
    )
    console.print(painel)


def mostrar_painel_continente(continentes):

    dados = continentes

    texto = Text()
    texto.append("Continente: ", style="bold cyan")
    texto.append(f"{dados['continente']}\n\n")
    texto.append("Total de países cadastrados: ", style="bold cyan")
    texto.append(f"{dados['total_paises']}\n\n")
    texto.append("Alguns países: ", style="bold cyan")
    texto.append(f"{dados['paises']}")

    painel = Panel(
        texto,
        title="[bold white]Países por Continente[/bold white]",
        border_style="magenta",
        padding=(1, 2),
        expand=True,
    )
    console.print(painel)


def mostrar_paineis_lado_a_lado(dados_formatados_1, dados_formatados_2):

    painel_pais1 = Panel(
        montar_texto_pais(dados_formatados_1),
        title=dados_formatados_1["nome"],
        border_style="green",
        padding=(1, 2),
    )

    painel_pais2 = Panel(
        montar_texto_pais(dados_formatados_2),
        title=dados_formatados_2["nome"],
        border_style="red",
        padding=(1, 2),
    )

    console.print(Columns([painel_pais1, painel_pais2]))