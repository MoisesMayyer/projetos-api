from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from rich.rule import Rule
from rich.text import Text


console = Console()

COR_PRIMARIA = "#E3350D"
COR_DESTAQUE = "yellow"
COR_TEXTO = "white"
COR_SECUNDARIA = "grey62"
COR_FUNDO_ESCURO = "black"


def limpar_tela() -> None:
    console.clear()


def mostrar_cabecalho() -> None:
    titulo = Text("P O K É D E X", style=f"bold {COR_TEXTO} on {COR_PRIMARIA}")
    titulo.justify = "center"

    subtitulo = Text("Consulte qualquer Pokémon", style=f"italic {COR_SECUNDARIA}")
    subtitulo.justify = "center"

    conteudo = Group(
        Align.center(titulo),
        Align.center(subtitulo),
    )

    painel = Panel(
        conteudo,
        border_style=COR_PRIMARIA,
        title="[bold]●[/bold]",
        title_align="left",
        subtitle="[bold]●[/bold]",
        subtitle_align="right",
        padding=(1, 4),
    )

    console.print(Align.center(painel))
    console.print(Rule(style=COR_PRIMARIA))


def mostrar_menu() -> None:
    tabela_menu = Table.grid(padding=(0, 2))
    tabela_menu.add_column(justify="right", style=f"bold {COR_DESTAQUE}")
    tabela_menu.add_column(justify="left", style=COR_TEXTO)

    tabela_menu.add_row("[1]", "Buscar Pokémon")
    tabela_menu.add_row("[2]", "Histórico")
    tabela_menu.add_row("[3]", "Sair")

    painel = Panel(
        Align.center(tabela_menu),
        title="[bold white]MENU[/bold white]",
        title_align="center",
        border_style=COR_PRIMARIA,
        padding=(1, 6),
    )

    console.print(Align.center(painel))


def mostrar_pokemon(dados: dict) -> None:
    nome = str(dados.get("nome", "Desconhecido")).capitalize()
    numero = dados.get("id", "?")
    altura = dados.get("altura", "?")
    peso = dados.get("peso", "?")
    tipos = dados.get("tipos", [])
    descricao = dados.get("descricao", "Sem descrição disponível.")
    sprite = dados.get("sprite", "")

    cabecalho = Text(f"#{numero:04d}  {nome}" if isinstance(numero, int) else f"#{numero}  {nome}")
    cabecalho.stylize(f"bold {COR_DESTAQUE}")

    tabela_info = Table.grid(padding=(0, 2))
    tabela_info.add_column(justify="right", style=f"bold {COR_SECUNDARIA}")
    tabela_info.add_column(justify="left", style=COR_TEXTO)

    tabela_info.add_row("Altura:", f"{altura}")
    tabela_info.add_row("Peso:", f"{peso}")
    tabela_info.add_row("Tipo(s):", ", ".join(t.capitalize() for t in tipos) if tipos else "—")

    bloco_descricao = Panel(
        Text(descricao, style=COR_TEXTO, justify="left"),
        title="Descrição",
        title_align="left",
        border_style=COR_SECUNDARIA,
        padding=(1, 2),
    )

    bloco_sprite = Text(f"🔗 {sprite}", style=f"underline {COR_DESTAQUE}") if sprite else Text(
        "Sprite indisponível.", style=COR_SECUNDARIA
    )

    conteudo = Group(
        Align.center(cabecalho),
        Rule(style=COR_SECUNDARIA),
        Align.center(tabela_info),
        Text(""),
        bloco_descricao,
        Text(""),
        Align.center(bloco_sprite),
    )

    painel = Panel(
        conteudo,
        border_style=COR_PRIMARIA,
        title="[bold]POKÉDEX[/bold]",
        title_align="center",
        padding=(1, 3),
    )

    console.print(Align.center(painel))


def mostrar_historico(historico: list) -> None:
    if not historico:
        painel_vazio = Panel(
            Align.center(Text("Nenhum Pokémon foi consultado ainda.", style=COR_SECUNDARIA)),
            title="Histórico",
            border_style=COR_SECUNDARIA,
            padding=(1, 4),
        )
        console.print(Align.center(painel_vazio))
        return

    tabela = Table(
        title="Histórico de Consultas",
        title_style=f"bold {COR_DESTAQUE}",
        border_style=COR_PRIMARIA,
        header_style=f"bold {COR_TEXTO} on {COR_PRIMARIA}",
        expand=False,
    )

    tabela.add_column("Nome", justify="left", style=COR_TEXTO)
    tabela.add_column("ID", justify="center", style=COR_DESTAQUE)
    tabela.add_column("Tipo", justify="left", style=COR_SECUNDARIA)

    for item in historico:
        nome = str(item.get("nome", "—")).capitalize()
        numero = str(item.get("id", "—"))
        tipo = str(item.get("tipo", "—")).capitalize()
        tabela.add_row(nome, numero, tipo)

    console.print(Align.center(tabela))


def mostrar_erro(mensagem: str = "Ocorreu um erro inesperado.") -> None:

    painel = Panel(
        Align.center(Text(mensagem, style="bold white")),
        title="✖ ERRO",
        title_align="center",
        border_style="bold red",
        style="on #3a0a0a",
        padding=(1, 4),
    )
    console.print(Align.center(painel))


def mostrar_sucesso(mensagem: str = "Operação realizada com sucesso.") -> None:

    painel = Panel(
        Align.center(Text(mensagem, style="bold white")),
        title="✔ SUCESSO",
        title_align="center",
        border_style="bold green",
        style="on #0a2a0a",
        padding=(1, 4),
    )
    console.print(Align.center(painel))


def mostrar_pokemon_nao_encontrado() -> None:
    painel = Panel(
        Align.center(
            Text("Pokémon não encontrado na Pokédex.", style="bold black")
        ),
        title="⚠ NÃO ENCONTRADO",
        title_align="center",
        border_style="bold yellow",
        style="on #3a3a0a",
        padding=(1, 4),
    )
    console.print(Align.center(painel))