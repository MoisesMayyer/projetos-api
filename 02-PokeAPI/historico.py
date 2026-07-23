import json


def ver_historico() -> list[dict]:
    return carregar_json()


def salvar_json(informacoes: dict) -> None:
    historico: list[dict] = carregar_json()
    historico.append(informacoes)

    with open('historico.json', 'w', encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def carregar_json() -> list[dict]:
    try:
        with open("historico.json", "r", encoding="utf-8") as arquivo:
            historico: list[dict] = json.load(arquivo)
            return historico
    except FileNotFoundError:
        return []