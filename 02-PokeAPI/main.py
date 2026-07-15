from api import consultar_pokemon, formatacao


def menu():
    while True:
        print("MENU POKEMON".center(30, " "))
        print("-"*30)
        print("1. Ver pokemon")
        print("2. Historico")
        print("3. Sair")

        opcao = int(input("opcao escolher: "))

        if opcao == 1:
            nome_pokemon = input("nome do pokemon: ")

            informacoes = consultar_pokemon(nome_pokemon)

            if informacoes:
                formatacao(informacoes)
            else:
                print("Pokemon não encontrado!")

        elif opcao == 2:
            print("funcionou")

        elif opcao == 3:
            break


if __name__ == "__main__":
    menu()