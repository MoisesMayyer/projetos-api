import requests

LINK_API = "https://pokeapi.co/api/v2/pokemon/"
LINK_DESCRICAO = f"https://pokeapi.co/api/v2/pokemon-species/"

def ver_pokemon(pokemon):

    link = f"{LINK_API}{pokemon}"

    resposta = requests.get(link)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    informacoes = {
        "nome": dados["name"],
        "id": dados["id"],
        "altura": dados["height"],
        "peso": dados["weight"],
        "tipos": []
    }

    for tipo in dados["types"]:
        informacoes["tipos"].append(
            tipo["type"]["name"]
        )

    return informacoes


def buscar_descricao(pokemon):

    link = f"{LINK_DESCRICAO}{pokemon}"

    resposta = requests.get(link)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    descricao = None

    for texto in dados["flavor_text_entries"]:
        if texto["language"]["name"] == "pt":
            descricao = texto["flavor_text"]
            break

    if descricao is None:
        for texto in dados["flavor_text_entries"]:
            if texto["language"]["name"] == "en":
                descricao = texto["flavor_text"]
                break

    return descricao


def consultar_pokemon(pokemon):
    informacoes = ver_pokemon(pokemon)

    if informacoes is None:
        return None

    descricao = buscar_descricao(pokemon)

    informacoes["descricao"] = descricao

    return informacoes


def formatacao(informacoes):
    for texto, dados in informacoes.items():
        print(f"{texto}: {dados}")