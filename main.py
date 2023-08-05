# %%
from utils.functions_menu import (
    menu_clientes,
    menu_acoes,
    menu_carteira,
    menu_relatorio,
)


def main():
    working = True

    while working:
        print(
            """
            Bem vindo! O que deseja realizar hoje?:
                    
            1 - Consultar Clientes
            2 - Consultar Ações
            3 - Analisar Carteira
            4 - Relatório da Carteira
            0 - Sair
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            menu_clientes()

        elif choosen_option == "2":
            menu_acoes()

        elif choosen_option == "3":
            menu_carteira()

        elif choosen_option == "4":
            menu_relatorio()

        elif choosen_option == "0" or choosen_option == "":
            print("Você escolheu sair.")
            working = False

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
