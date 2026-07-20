import requests
from historico import salvar_json


def consultar_cep(cep):
    cep = cep.strip()

    if not cep.isdigit():
        return None

    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            salvar_json(dados)
            return dados

        return None

    except requests.exceptions.RequestException:
        print("Erro de conexão")
        return None