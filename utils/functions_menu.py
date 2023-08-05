from repository.banco_de_dados import BancoDeDados


def menu_clientes():
    working = True

    while working:
        print(
            """
           Consultar informações de usuário:
                    
            1 - Inserir novo cliente
            2 - Alterar informações de cliente
            3 - Mostrar informações de cliente
            4 - Desativar cliente (deleção virtual)
            5 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")
        banco = BancoDeDados()

        if choosen_option == "1":
            return banco.inserir_cliente()

        elif choosen_option == "2":
            return banco.alterar_cliente()

        elif choosen_option == "3":
            return banco.selecionar_cliente()

        elif choosen_option == "4":
            return banco.desativar_cliente()

        elif choosen_option == "5" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")


# %%
def menu_acoes():
    working = True

    while working:
        print(
            """
           Consultar informações de ações:
                    
            1 - Inserir nova ação
            2 - Mostrar cotação de ação
            3 - Desativar ação
            4 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "2":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "3":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "4" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")


# %%
def menu_carteira():
    working = True

    while working:
        print(
            """
           Consultar informações de carteiras:
                    
            1 - Saldo
            2 - Extrato
            3 - Análise de performance
            4 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "2":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "3":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "4" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")


# %%
def menu_relatorio():
    return print("Seu relatório está sendo impresso!")
