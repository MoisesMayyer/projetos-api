from api import consultar_cep
from historico import carregar_json


def formatacao(dados):
    print()

    for dado, valor in dados.items():
        print(f"{dado}: {valor}")


def consultar_cep_menu():
    cep = input("Digite o CEP: ")

    dados = consultar_cep(cep)

    if dados:
        formatacao(dados)
    else:
        print("CEP não encontrado")


def historico_cep():
    historico = carregar_json()

    if historico:
        for cep in historico:
            formatacao(cep)
    else:
        print("Nenhum histórico encontrado")


opcoes_menu = {
    1: ("Consultar CEP", consultar_cep_menu),
    2: ("Ver histórico", historico_cep),
    3: ("Sair", None)
}


def menu():
    while True:
        print("-" * 30)
        print("MENU".center(30))
        print("-" * 30)

        for numero, dados in opcoes_menu.items():
            nome = dados[0]
            print(f"[{numero}] {nome}")

        while True:
            try:
                opc = int(input("Digite: "))
                break
            except ValueError:
                print("Valor inválido")

        if opc == 3:
            print("Saindo...")
            break

        if opc in opcoes_menu:
            funcao = opcoes_menu[opc][1]

            if funcao:
                funcao()

        else:
            print("Opção inválida")