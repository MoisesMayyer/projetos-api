from api import consultar_pokemon
from historico import ver_historico, salvar_json
from interface import (
    limpar_tela,
    mostrar_cabecalho,
    mostrar_menu,
    mostrar_pokemon,
    mostrar_historico,
    mostrar_pokemon_nao_encontrado,
)

def menu():
    while True:
        limpar_tela()
        mostrar_cabecalho()
        mostrar_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            mostrar_cabecalho()

            nome_pokemon = input("Digite o nome do Pokémon: ").strip().lower()

            informacoes = consultar_pokemon(nome_pokemon)

            if informacoes:
                salvar_json({
                    "nome": informacoes["nome"],
                    "id": informacoes["id"],
                    "tipo": informacoes["tipos"][0]
                })

                limpar_tela()
                mostrar_cabecalho()
                mostrar_pokemon(informacoes)

            else:
                mostrar_pokemon_nao_encontrado()

            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            limpar_tela()
            mostrar_cabecalho()

            historico = ver_historico()
            mostrar_historico(historico)

            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            break

        else:
            input("\nOpção inválida. Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu()