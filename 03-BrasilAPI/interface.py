from api import consultar_cep


def formatacao(dados):
    print("\n")
    for dado, valor in dados.items():
        print(f"{dado}: {valor}")


def consultar_cep_menu():
    dados = consultar_cep()

    if dados:
        formatacao(dados)
    else:
        print("CEP não encontrado")


opcoes_menu = {
        1:("Consultar cep",consultar_cep_menu),
        2:("Ver historico",None),
        3:("Sair",None)
}


def menu():
    print("-"*30)
    print("MENU".center(30))
    print("-"*30)

    for numero, dados in opcoes_menu.items():
        nome = dados[0]
        print(f"[{numero}] {nome}")

    while True:
        try:
            opc = int(input("digite "))
            break
        except ValueError:
            print("valor invalido")

    if opc in opcoes_menu:
        funcao = opcoes_menu[opc][1]

        if funcao:
            funcao()