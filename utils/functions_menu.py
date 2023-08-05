from repository.banco_de_dados import BancoDeDados

from utils.relatorio import obter_dados_acao

banco = BancoDeDados()


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
            0 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return banco.inserir_cliente()

        elif choosen_option == "2":
            return banco.alterar_cliente()

        elif choosen_option == "3":
            return banco.selecionar_cliente()

        elif choosen_option == "4":
            return banco.desativar_cliente()

        elif choosen_option == "0" or choosen_option == "":
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
                    
            1 - Cadastrar Ordem de Compra
            2 - Deletar ação
            0 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return banco.inserir_acao()

        elif choosen_option == "2":
            return banco.deletar_acao()

        elif choosen_option == "0" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")


# %%
def menu_carteira():
    working = True

    while working:
        print(
            """
           Consultar performace de carteiras:
                    
            1 - Performace
            0 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return banco.analise_carteira()

        elif choosen_option == "0" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")


# %%
def menu_relatorio():
    working = True

    while working:
        print(
            """
           Consultar informações de carteiras:
                    
            1 - Obter relatório
            2 - consultar acao
            0 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return banco.relatorio_carteira()

        elif choosen_option == "2":
            return obter_dados_acao()

        elif choosen_option == "0" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")
