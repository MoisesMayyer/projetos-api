import json


def ver_historico():
    historico = carregar_json()

    if not historico:
        print("Nenhum histórico encontrado.")
        return

    for pokemon in historico:
        print(pokemon)


def salvar_json(informacoes):
    historico = carregar_json()
    historico.append(informacoes)

    with open('historico.json', 'w', encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def carregar_json():
    try:
        with open("historico.json", "r", encoding="utf-8") as arquivo:
            historico = json.load(arquivo)
            return historico
    except FileNotFoundError:
        return []