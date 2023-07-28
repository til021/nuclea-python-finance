# %%
import json

from utils.validations import (
    name_validation,
    cpf_validation,
    rg_validation,
    birth_validation,
    cep_validation,
)

with open("user_data.json", "r") as data_file:
    data = json.load(data_file)


# %%
def receive_user():
    """Recebe os dados do usuário.

    Returns:
        _type_: _description_
    """

    name = name_validation()
    cpf = cpf_validation()
    rg = rg_validation()
    birth_day = birth_validation()
    adress = cep_validation()

    return name, cpf, rg, birth_day, adress


# %%
def insert_user():
    """
    Aplica a função 'receive_user()' e insere os dados no banco.
    """

    name, cpf, rg, birth_day, adress = receive_user()
    try:
        new_id = max([int(item) for item in data.keys()]) + 1

    except:
        new_id = 0

    data[str(new_id)] = {
        "Nome": name,
        "CPF": cpf,
        "RG": rg,
        "Nascimento": birth_day,
        "Endereço": adress,
        "Status": "Ativo",
    }

    return str(new_id)


# %%
def user_info(user_id=data.keys()):
    """Mostra as alterações na base de dados."""

    print("----------------------------------")
    for id in user_id:
        print(
            f"""
        Id: {id}
        Status: {data[id]['Status']}
        Nome: {data[id]['Nome']}
        CPF: {data[id]['CPF']}
        RG: {data[id]['RG']}
        Nascimento: {data[id]['Nascimento']}
        Endereço: {data[id]['Endereço']}     
        """
        )
        print("----------------------------------")


# %%
def save_n_leave():
    """Salva as alterações realizadas."""

    import json

    commit = input("Deseja salvar as alterações? (y/n): ").lower()
    if commit == "y":
        with open("user_data.json", "w") as write_file:
            json.dump(data, write_file)
        print("Todas alterações foram salvas!")
    else:
        print("Não foram feitas alterações!")
