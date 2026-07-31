import json


def criar_registro_favoritos(nome_pais, capital,continente,populacao):
    return {
        "nome": nome_pais,
        "capital": capital,
        "continente": continente,
        "populacao": populacao
    }


def adicionar_favoritos(dados: dict) -> None:
    favoritos = carregar_favoritos()

    ja_favoritado = any(
        favorito["nome"] == dados["nome"]
        for favorito in favoritos
    )

    if ja_favoritado:
        return

    registro = criar_registro_favoritos(
        nome_pais=dados["nome"],
        capital=dados["capital"],
        continente=dados["continente"],
        populacao=dados["populacao"]
    )

    favoritos.append(registro)
    salvar_favoritos(favoritos)


def salvar_favoritos(historico) -> None:

    with open("dados/favoritos.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def carregar_favoritos() -> list[dict]:
    try:
        with open("dados/favoritos.json", "r", encoding="utf-8") as arquivo:
            historico: list[dict] = json.load(arquivo)
            return historico
    except FileNotFoundError:
        return []
