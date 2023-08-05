import unittest
from unittest.mock import patch
from validate_docbr import CPF
from faker import Faker

from utils.functions_cliente import receive_user


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
            received_user = receive_user()

        expected_user = (
            name,
            CPF().mask(cpf),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        )

        self.assertEquals(expected_user, received_user)
