
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from rich.rule import Rule
from rich.text import Text

console = Console()


CORES = {
    "primaria": "bright_cyan",
    "secundaria": "grey62",
    "sucesso": "green3",
    "erro": "red3",
    "aviso": "yellow3",
    "info": "dodger_blue2",
    "destaque": "bold white",
}


# UTILITÁRIO
def limpar_tela() -> None:
    console.clear()



# CABEÇALHO
def mostrar_cabecalho() -> None:
    titulo = Text("WEATHER API", style=f"bold {CORES['primaria']}", justify="center")
    subtitulo = Text(
        "consulta de clima em tempo real  •  terminal edition",
        style=f"italic {CORES['secundaria']}",
        justify="center",
    )

    conteudo = Group(titulo, subtitulo)

    painel = Panel(
        Align.center(conteudo),
        border_style=CORES["primaria"],
        padding=(1, 4),
        expand=True,
    )
    console.print(painel)


# MENU PRINCIPAL
def mostrar_menu() -> None:
    tabela = Table.grid(padding=(0, 3))
    tabela.add_column(justify="center")

    tabela.add_row(Text("1  ·  Consultar clima", style=CORES["destaque"]))
    tabela.add_row(Text("2  ·  Ver histórico", style=CORES["destaque"]))
    tabela.add_row(Text("3  ·  Sair", style="bold " + CORES["erro"]))

    painel = Panel(
        Align.center(tabela),
        title="[bold]Menu Principal[/bold]",
        title_align="center",
        border_style=CORES["secundaria"],
        padding=(1, 6),
    )
    console.print(Align.center(painel))



# TELA DE CONSULTA DE CLIMA
def mostrar_clima(informacoes: dict) -> None:
    localizacao = Table.grid(padding=(0, 2))
    localizacao.add_column(justify="left")
    localizacao.add_row(Text(f"📍 {informacoes.get('cidade', '—')}", style=CORES["destaque"]))
    localizacao.add_row(Text(f"🌍 {informacoes.get('pais', '—')}", style=CORES["secundaria"]))
    localizacao.add_row(Text(f"🗺 {informacoes.get('regiao', '—')}", style=CORES["secundaria"]))

    condicao = Table.grid(padding=(0, 2))
    condicao.add_column(justify="left")
    condicao.add_row(Text(f"🌤 {informacoes.get('condicao', '—')}", style=f"bold {CORES['info']}"))
    condicao.add_row(Text(f"🌡 {informacoes.get('temperatura', '—')}°C", style=f"bold {CORES['primaria']}"))
    condicao.add_row(Text(f"🥵 Sensação: {informacoes.get('sensacao', '—')}°C", style=CORES["secundaria"]))

    medidas = Table.grid(padding=(0, 2))
    medidas.add_column(justify="left")
    medidas.add_row(Text(f"💧 Umidade: {informacoes.get('umidade', '—')}%", style=CORES["secundaria"]))
    medidas.add_row(Text(f"💨 Vento: {informacoes.get('vento', '—')} km/h", style=CORES["secundaria"]))

    colunas = Columns(
        [localizacao, condicao, medidas],
        expand=True,
        equal=True,
        align="center",
    )

    painel = Panel(
        colunas,
        title="[bold]Resultado da Consulta[/bold]",
        title_align="left",
        border_style=CORES["primaria"],
        padding=(1, 3),
    )

    console.print(Rule(style=CORES["secundaria"]))
    console.print(painel)
    console.print(Rule(style=CORES["secundaria"]))



# HISTÓRICO
def mostrar_historico(historico: list) -> None:
    if not historico:
        mostrar_historico_vazio()
        return

    tabela = Table(
        title="Histórico de Consultas",
        title_style=f"bold {CORES['primaria']}",
        border_style=CORES["secundaria"],
        header_style=f"bold {CORES['destaque']}",
        expand=True,
    )

    tabela.add_column("Cidade", justify="left")
    tabela.add_column("País", justify="left")
    tabela.add_column("Condição", justify="center")
    tabela.add_column("Temperatura", justify="right")

    for item in historico:
        tabela.add_row(
            item.get("cidade", "—"),
            item.get("pais", "—"),
            item.get("condicao", "—"),
            f"{item.get('temperatura', '—')}°C",
        )

    console.print(tabela)



# MENSAGENS DE ESTADO
def mostrar_erro(mensagem: str) -> None:
    painel = Panel(
        Text(mensagem, style="bold white", justify="center"),
        title="[bold]✖ Erro[/bold]",
        border_style=CORES["erro"],
        padding=(1, 2),
    )
    console.print(painel)


def mostrar_sucesso(mensagem: str) -> None:
    painel = Panel(
        Text(mensagem, style="bold white", justify="center"),
        title="[bold]✔ Sucesso[/bold]",
        border_style=CORES["sucesso"],
        padding=(1, 2),
    )
    console.print(painel)


def mostrar_cidade_nao_encontrada(mensagem: str = "Cidade não encontrada.") -> None:
    painel = Panel(
        Text(mensagem, style="bold white", justify="center"),
        title="[bold]⚠ Não Encontrado[/bold]",
        border_style=CORES["aviso"],
        padding=(1, 2),
    )
    console.print(painel)


def mostrar_historico_vazio() -> None:
    painel = Panel(
        Text("Nenhuma consulta registrada até o momento.", style="italic", justify="center"),
        title="[bold]Histórico Vazio[/bold]",
        border_style=CORES["info"],
        padding=(1, 2),
    )
    console.print(painel)