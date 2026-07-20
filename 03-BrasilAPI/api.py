import requests


def consultar_cep():
    while True:
        cep = input("Digite o CEP: ").strip()

        if cep.isdigit():
            break

        print("Digite apenas números")

    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        print("Erro de conexão")
        return None