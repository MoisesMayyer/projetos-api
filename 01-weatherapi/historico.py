import json

def salvar_json(informacoes):
    historico = carregar_json()
    historico.append(informacoes)

    with open("historico.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def carregar_json():
    try:
        with open("historico.json",'r') as arquivo:
            informacoes = json.load(arquivo)
            return informacoes
    except FileNotFoundError:
        return []
