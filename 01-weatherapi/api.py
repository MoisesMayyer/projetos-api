import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
link_api = "http://api.weatherapi.com/v1/current.json"

def consultar_clima(cidade):
    parametros ={
        "key": api_key,
        "q": cidade,
        "lang": "pt"
    }

    resposta = requests.get(link_api, params=parametros)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    informacoes ={
        "cidade":dados["location"]["name"],
        "país": dados["location"]["country"],
        "Região":dados["location"]["region"],
        "condição":dados["current"]["condition"]["text"],
        "temperatura":dados["current"]["temp_c"],
        "sensação":dados["current"]["feelslike_c"],
        "umidade":dados["current"]["humidity"],
        "vento":dados["current"]["wind_kph"]
    }

    return informacoes


def ver_historico():
    pass
