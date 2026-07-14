def menu():
    opcoes = [
        "Consultar clima",
        "Ver histórico",
        "Alterar cidade",
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
            print("Digite apenas números!")
            continue
            
        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            break


if __name__ == "__main__":
    menu()