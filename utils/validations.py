# %%
import re


def name_validation():
    """Verifica se o nome contém apenas letras e espaços em branco.
        O nome não pode conter números nem caracteres especiais.

    Returns:
        str: Retorna o nome capitalizado.
    """
    standard = r"^[a-zA-Z\s]+$"

    while True:
        name = input("Insira o nome do usuário: ")

        if re.match(standard, name):
            return name.capitalize()
        else:
            print("Você não digitou um nome válido. Tente novamente.")


if __name__ == "__main__":
    name_validation()

# %%

from validate_docbr import CPF


def cpf_validation():
    """Função que valida o CPF fornecido.

    Returns:
        str: CPF formatado.
    """

    validator = CPF()

    while True:
        cpf = input("Número do CPF (apenas números): ")

        if cpf == "":
            return "Não informado"

        elif validator.validate(cpf):
            formatted_cpf = validator.mask(cpf)
            print(formatted_cpf)
            return formatted_cpf

        else:
            print("Você não digitou um CPF válido. Tente novamente.")


if __name__ == "__main__":
    cpf_validation()

# %%


def rg_validation():
    """Verifica se o RG contém apenas números.

    Returns:
        str: Retorna o RG.
    """
    while True:
        rg = input("Número do RG (apenas números): ")

        if rg == "":
            return "Não informado"

        else:
            try:
                int(rg)
                return rg

            except:
                print("Você não digitiou um RG válido. Tente novamente.")


if __name__ == "__main__":
    rg_validation()

# %%

from datetime import datetime


def birth_validation():
    """Verifica se a data de nascimento é possível.

    Returns:
        str: Retorna a data de nascimento no formato dd/mm/aaa.
    """
    while True:
        bd = input("Data de nascimento (dd/mm/aaaa): ")

        if bd == "":
            return "Não informado"

        try:
            bd_converted = datetime.strptime(bd, "%d/%m/%Y").date()
            today = datetime.now().date()

            if bd_converted < today:
                return bd_converted.strftime("%d/%m/%Y")

            else:
                print("Você não digitou uma data válida. Tente novamente.")

        except:
            print("Você não digitou uma data válida. Tente novamente.")


if __name__ == "__main__":
    birth_validation()

# %%

import requests


def cep_validation():
    """Verifica o CEP e fornece o endereço.

    Returns:
        dict: Fornece o endereço no formato de dicionário.
    """
    while True:
        cep = input("Endereço do CEP (apenas números): ")

        if cep == "":
            return "Não informado"

        try:
            url = f"http://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)
            return response.json()

        except:
            print("Você não digitou um CEP válido. Tente novamente.")


if __name__ == "__main__":
    cep_validation()

# %%
