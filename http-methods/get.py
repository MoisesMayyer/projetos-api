import requests


def formatacao(dados):
    for item in dados:
        for nome, valor in item.items():
            print(f"{nome}: {valor}")
        print("-" * 30)


opcoes = {
    1: "https://jsonplaceholder.typicode.com/posts",
    2: "https://jsonplaceholder.typicode.com/comments",
    3: "https://jsonplaceholder.typicode.com/albums",
    4: "https://jsonplaceholder.typicode.com/photos",
    5: "https://jsonplaceholder.typicode.com/todos",
    6: "https://jsonplaceholder.typicode.com/users"
}


while True:
    print("-" * 30)
    print("MENU".center(30))
    print("-" * 30)

    for numero, url in opcoes.items():
        print(f"[{numero}] {url.split('/')[-1]}")

    print("[0] Sair")

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido")
        continue

    if opcao_escolhida == 0:
        break

    if opcao_escolhida in opcoes:
        requisicao = requests.get(opcoes[opcao_escolhida])

        if requisicao.status_code == 200:
            informacoes = requisicao.json()
            formatacao(informacoes)
        else:
            print("Erro na requisição")
    else:
        print("Opção inexistente")