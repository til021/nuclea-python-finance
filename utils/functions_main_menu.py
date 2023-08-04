from utils.functions_user import insert_user, user_info

import json

with open("user_data.json", "r") as data_file:
    data = json.load(data_file)


# %%
def user_menu():
    working = True

    while working:
        print(
            """
           Consultar informações de usuário:
                    
            1 - Inserir novo usuário
            2 - Alterar informações de usuário
            3 - Mostrar informações de usuário
            4 - Desativar usuário
            5 - Retornar ao menu anterior
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            return user_info(insert_user())

        elif choosen_option == "2":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "3":
            return user_info()

        elif choosen_option == "4":
            return print("Essa opção ainda não foi implementada.")

        elif choosen_option == "5" or choosen_option == "":
            return

        else:
            print("Opção inválida. Tente novamente.")


# %%
def titles_menu():
    working = True

    while working:
        print(
            """
           Consultar informações de títulos:
                    
            1 - Inserir novo título
            2 - Mostrar informações de título
            3 - Desativar título
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
def wallet_menu():
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
def save_n_leave():
    """Salva as alterações realizadas."""

    import json

    commit = input("Deseja salvar as alterações? (y/N): ").lower()
    if commit == "y":
        with open("user_data.json", "w") as write_file:
            json.dump(data, write_file)
        print("Todas alterações foram salvas!")
    else:
        print("Nenhuma alteração foi salva!")
