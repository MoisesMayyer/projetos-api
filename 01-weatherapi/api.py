import os
import requests
from dotenv import load_dotenv
from historico import carregar_json

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
link_api = "http://api.weatherapi.com/v1/current.json"

def consultar_clima(cidade):
    parametros = {
        "key": api_key,
        "q": cidade,
        "lang": "pt"
    }

    resposta = requests.get(link_api, params=parametros)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    return {
        "cidade": dados["location"]["name"],
        "pais": dados["location"]["country"],
        "regiao": dados["location"]["region"],
        "condicao": dados["current"]["condition"]["text"],
        "temperatura": dados["current"]["temp_c"],
        "sensacao": dados["current"]["feelslike_c"],
        "umidade": dados["current"]["humidity"],
        "vento": dados["current"]["wind_kph"]
    }



def ver_historico():
    historico = carregar_json()

    if not historico:
        print("Você não tem histórico ainda.\n")
        return

    print("-" * 30)
    print("Histórico de consultas")
    print("-" * 30)

    for consulta in historico:
        print(f"Cidade: {consulta['cidade']}")
        print(f"País: {consulta['pais']}")
        print(f"Condição: {consulta['condicao']}")
        print(f"Temperatura: {consulta['temperatura']}°C")
        print("-" * 30)
