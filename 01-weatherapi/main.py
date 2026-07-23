from api import consultar_clima
from historico import salvar_json, carregar_json
from interface import (
    limpar_tela,
    mostrar_cabecalho,
    mostrar_menu,
    mostrar_clima,
    mostrar_historico,
    mostrar_cidade_nao_encontrada,
)

def menu() -> None:
    while True:
        limpar_tela()
        mostrar_cabecalho()
        mostrar_menu()

        try:
            opcao = int(input("\nDigite sua opção: "))
        except ValueError:
            print("Digite apenas números!\n")
            input("Pressione Enter para continuar...")
            continue

        if opcao == 1:
            limpar_tela()
            cidade_escolhida: str = input("Digite o nome da cidade: ")

            informacoes: dict | None = consultar_clima(cidade_escolhida)

            if informacoes:
                salvar_json({
                    "cidade": informacoes["cidade"],
                    "pais": informacoes["pais"],
                    "condicao": informacoes["condicao"],
                    "temperatura": informacoes["temperatura"]
                })

                limpar_tela()
                mostrar_cabecalho()
                mostrar_clima(informacoes)

            else:
                limpar_tela()
                mostrar_cabecalho()
                mostrar_cidade_nao_encontrada()

            input("\nPressione Enter para voltar ao menu...")

        elif opcao == 2:
            limpar_tela()
            mostrar_cabecalho()
            mostrar_historico(carregar_json())

            input("\nPressione Enter para voltar ao menu...")

        elif opcao == 3:
            print("\nAté logo!")
            break

        else:
            print("\nOpção inválida.")
            input("Pressione Enter para continuar...")
    

if __name__ == "__main__":
    menu()