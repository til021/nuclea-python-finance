# %%
from utils.functions import insert_user, user_info, save_n_leave

# %%
working = True

while working:
    print(
        """
        Welcome to Tiago's Data Management Engine!
                
        1 - Inserir Novo Usuário
        4 - Informações de Usuário
        7 - Salvar e Sair
    """
    )

    option = input("Escolha uma opção: ")

    if option == "1":
        user_info(insert_user())

    elif option == "4":
        user_info()

    elif option == "7":
        save_n_leave()
        working = False

    elif option == "":
        print("Você escolheu sair. Nenhuma alteração foi salva.")
        working = False

    else:
        print("Opção inválida. Tente novamente.")
