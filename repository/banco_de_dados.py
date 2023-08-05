import psycopg2
import os
from dotenv import load_dotenv

from utils.client_validation import (
    name_validation,
    cpf_validation,
    rg_validation,
    birth_validation,
    cep_validation,
)

# CLASSE:
# FORMA DE BOLO, ESTEIRA DE PRODUÇÃO DE UM VEICULO;
# ATRIBUTO/CARICTERISTICA;
# CHASSI, COR, QUANTIDADE DE PORTAS, POTENCIA MOTOR, CAMBIO;
# METODOS/FUNCOES:
# ACOES, COMPORTAMENTO, 4X4, TURBO, ANDAR, ESTACIONAR, TROCAR DE MARCHA
# __init__
# Construcao do objeto
# __del__
# Delecao do objeto

# java objeto = new Class();
# python objeto = Class()

# variavel = cliente
# funcao = cliente()
# classe = Cliente()


class BancoDeDados:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        # Obtém os valores de conexão do ambiente usando 'os.getenv'
        database_url = os.getenv("DATABASE_URL")
        self.connection = psycopg2.connect(database_url)
        print("Conexão ao banco de dados PostgreSQL realizada com sucesso!")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def receber_cliente(self):
        client_info = {
            "nome": name_validation(),
            "cpf": cpf_validation(),
            "rg": rg_validation(),
            "birth_day": birth_validation(),
        }
        estado, cidade, bairro, logradouro, cep = cep_validation()
        client_info["estado"] = estado
        client_info["cidade"] = cidade
        client_info["bairro"] = bairro
        client_info["logradouro"] = logradouro
        client_info["cep"] = cep

        return client_info

    def inserir_cliente(self):
        client_info = self.receber_cliente()
        insert_query = """
                INSERT INTO users (nome, cpf, rg, birth_day, estado, cidade, bairro,
	            logradouro, cep, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, True);
                """
        values = (
            client_info["nome"],
            client_info["cpf"],
            client_info["rg"],
            client_info["birth_day"],
            client_info["estado"],
            client_info["cidade"],
            client_info["bairro"],
            client_info["logradouro"],
            client_info["cep"],
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print("Alterações salvas com sucesso.")

    def alterar_cliente(self):
        changed_id = int(input("Qual o id do cliente que você quer alterar? "))

        client_info = self.receber_cliente()
        update_query = """
               UPDATE users
               SET nome = %s,
                   cpf = %s,
                   rg = %s,
                   birth_day = %s,
                   estado = %s,
                   cidade = %s,
                   bairro = %s,
                   logradouro = %s,
                   cep = %s
               WHERE id = %s;
               """
        values = (
            client_info["nome"],
            client_info["cpf"],
            client_info["rg"],
            client_info["birth_day"],
            client_info["estado"],
            client_info["cidade"],
            client_info["bairro"],
            client_info["logradouro"],
            client_info["cep"],
            changed_id,
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()
        self.selecionar_cliente(changed_id)
        print("Alterações salvas com sucesso.")

    def selecionar_cliente(self, id=False):
        if id:
            select_query = "SELECT * FROM public.users WHERE id = %s;"
            value = (id,)
            self.cursor.execute(select_query, value)
        else:
            select_query = "SELECT * FROM public.users;"
            self.cursor.execute(select_query)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        return clientes

    def desativar_cliente(self):
        changed_id = int(input("Qual o id do cliente que você quer desativar? "))

        update_query = """
               UPDATE users
               SET status = False
               WHERE id = %s;
               """
        values = (changed_id,)
        self.cursor.execute(update_query, values)
        self.connection.commit()
        self.selecionar_cliente(changed_id)
        print("Alterações salvas com sucesso.")
