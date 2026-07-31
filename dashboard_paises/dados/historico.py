import json
from datetime import datetime


def criar_registro_historico(nome_pais, acao):
    return {
        "data": datetime.now().strftime("%d/%m/%Y"),
        "pais": nome_pais,
        "acao": acao
    }

def salvar_historico(historico) -> None:

    with open("dados/historico.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def carregar_historico() -> list[dict]:
    try:
        with open("dados/historico.json", "r", encoding="utf-8") as arquivo:
            historico: list[dict] = json.load(arquivo)
            return historico
    except FileNotFoundError:
        return []

