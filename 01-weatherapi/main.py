from api import consultar_clima, ver_historico

def menu():
    opcoes = [
        "Consultar clima",
        "Ver histórico",
        "Sair"
    ]

    while True:
        print("Bem-Vindo ao Weather API".center(30," "))
        print("-"*30)

        for numero, texto in enumerate(opcoes, 1):
            print(f"{texto:<20} [{numero}]")

        print("-"*30)

        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Digite apenas números!\n")
            continue

        if opcao == 1:
            cidade_escolhida = str(input("Digite o nome da cidade: "))

            informacoes = consultar_clima(cidade_escolhida)

            if informacoes:
                print(informacoes)
            else:
                print("Cidade não encontrada!")


        elif opcao == 2:
            ver_historico()
        elif opcao == 3:
            break


if __name__ == "__main__":
    menu()