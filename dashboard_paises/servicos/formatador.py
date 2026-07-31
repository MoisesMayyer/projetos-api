
def formata_dados(dados) -> dict:
    pais = dados["data"]["objects"][0]

    dados_formatados = {
            "nome": pais["names"]["common"],
            "nome_oficial": pais["names"]["official"],
            "capital": pais["capitals"][0]["name"],
            "continente": pais["continents"][0],
            "regiao": pais["region"],
            "sub_regiao": pais["subregion"],
            "populacao": pais["population"],
            "area_territorial": pais["area"]["kilometers"],
            "idiomas": [idioma["name"] for idioma in pais["languages"]],
            "moedas": [moeda["name"] for moeda in pais["currencies"]],
            "fuso_horarios": pais["timezones"],
            "bandeira_url": pais["flag"]["url_png"],
            "codigo_pais": pais["codes"]["alpha_3"],
    }

    return dados_formatados

