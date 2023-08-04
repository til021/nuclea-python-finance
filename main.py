# %%
from utils.functions_main_menu import user_menu, titles_menu, wallet_menu, save_n_leave
from repository import get_db_connection

# %%


def main():
    connection = get_db_connection()

    while connection:
        cursor = connection.cursor()

        print(
            """
            Bem vindo! O que deseja realizar hoje?:
                    
            1 - Consultar usuários
            2 - Consultar títulos
            3 - Consultar carteiras
            4 - Salvar e sair
        """
        )

        choosen_option = input("Escolha uma opção: ")

        if choosen_option == "1":
            user_menu()

        elif choosen_option == "2":
            titles_menu()

        elif choosen_option == "3":
            wallet_menu()

        elif choosen_option == "4" or choosen_option == "":
            save_n_leave()
            cursor.close()
            connection.close()

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
