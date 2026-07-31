import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.restcountries.com/countries/v5?q="

HEADERS = {
    "Authorization": f"Bearer {os.getenv('API_KEY')}"
}


def fazer_requisicao(url):
    resposta = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )
    resposta.raise_for_status()

    return resposta


def dados_do_pais(nome):
    url = f"{BASE_URL}{nome}"
    resposta = fazer_requisicao(url)

    return resposta.json()


"""def dados_continentes():""" # -> ainda nn sei como pegar todos os continentes do json
