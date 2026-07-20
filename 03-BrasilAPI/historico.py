import json


def salvar_json(dados):
    historico = carregar_json()
    historico.append(dados)

    with open('historico.json', 'w', encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)

def carregar_json():
    try:
        with open("historico.json", "r", encoding="utf-8") as arquivo:
            historico = json.load(arquivo)
            return historico
    except FileNotFoundError:
        return []
