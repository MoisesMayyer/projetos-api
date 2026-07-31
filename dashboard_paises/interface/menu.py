from dashboard_paises.servicos.pais import pesquisar_pais, comparar_paises

opcoes = [
    "[1] pesquisar pais:",
    "[2] Comparar países:",
    "[3] historico:",
    "[4] sair:",
]

def menu_principal() -> None:
    while True:
        print("-"*30)
        print("Dashboard Países".center(30))
        print("-"*30)

        for opc in opcoes:
            print(opc)

        while True:
            try:
                opc_escolhida = int(input(""))
                break
            except ValueError:

                print("Valor invalido")

        if opc_escolhida == 1:
            nome_pais = input("Digite o nome do país: ")
            pesquisar_pais(nome_pais)

        elif opc_escolhida == 2:
            pais1 = input("digite o primeiro país: ")
            pais2 = input("digite o segundo país para comparar:")

            comparar_paises(pais1, pais2)

        elif opc_escolhida == 3:
            break

        else:
            print("opc invalida")
