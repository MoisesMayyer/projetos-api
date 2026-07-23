import json


def carregar_json() -> list[dict]:
    try:
        with open("historico.json", "r", encoding="utf-8") as arquivo:
            informacoes = json.load(arquivo)
            return informacoes

    except FileNotFoundError:
        return []


def salvar_json(informacoes: dict) -> None:
    historico: list[dict] = carregar_json()
    historico.append(informacoes)

    with open("historico.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)