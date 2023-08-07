import unittest
from unittest.mock import patch
from validate_docbr import CPF
from faker import Faker

from repository.banco_de_dados import BancoDeDados

banco = BancoDeDados()


class TestStringMethods(unittest.TestCase):
    def fake_name_generator(self):
        name = Faker().name()
        return name.upper()

    def fake_cpf_generator(self):
        cpf = CPF().generate()
        return cpf

    def test_user_insertion(self):
        name = self.fake_name_generator()
        cpf = self.fake_cpf_generator()
        inputs = [
            name,
            cpf,
            "",
            "",
            "",
        ]

        with patch("builtins.input", side_effect=inputs):
            received_user = banco.receber_cliente()

        expected_user = {}
        expected_user["nome"] = name
        expected_user["cpf"] = CPF().mask(cpf)
        expected_user["rg"] = None
        expected_user["birth_day"] = None
        expected_user["estado"] = None
        expected_user["cidade"] = None
        expected_user["bairro"] = None
        expected_user["logradouro"] = None
        expected_user["cep"] = None

        self.assertEquals(expected_user, received_user)


if __name__ == "__main__":
    test_user_insertion()
