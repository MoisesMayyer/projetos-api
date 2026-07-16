import requests
import pprint

URL = "https://jsonplaceholder.typicode.com/posts"

while True:
    print("menu adicionar".center(30))
    print("-"*30)
    print(
        f"[1] post"
        f"\n[2] listar"
        f"\n[3] sair"
    )

    try:
        opcao_escolha = int(input("escolha qual voce quer adicionar: "))
    except ValueError:
        print("opcao invalida")
        continue

    if opcao_escolha == 1:
        titulo = input("Digite o título: ")
        mensagem = input("Digite a mensagem: ")

        dados = {
            "title": titulo,
            "body": mensagem,
            "userId": 1
        }

        resposta = requests.post(URL, json=dados)

        if resposta.status_code == 201:
            print("Post criado:")
            pprint.pprint(resposta.json())
        else:
            print("Erro ao criar post")

    elif opcao_escolha == 2:
        requisicao = requests.get(URL)

        if requisicao.status_code == 200:
            informacao = requisicao.json()
            pprint.pprint(informacao)

    elif opcao_escolha == 3:
        break

    else:
        print("opção invalida")


