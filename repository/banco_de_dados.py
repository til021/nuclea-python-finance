import psycopg2
import os
from dotenv import load_dotenv
import yfinance as yf


from utils.client_validation import (
    name_validation,
    cpf_validation,
    rg_validation,
    birth_validation,
    cep_validation,
)
from utils.analise_carteira import analise


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

    def receber_acao(self):
        while True:
            try:
                acao_info = {
                    "nome": input("nome: "),
                    "ticket": input("ticket: "),
                    "valor_compra": float(input("valor_compra: ")),
                    "quantidade_compra": int(input("quantidade_compra: ")),
                    "data_compra": input("data_compra: "),
                    "client_id": int(input("client_id: ")),
                }
                return acao_info
            except:
                continue

    def inserir_acao(self):
        acao_info = self.receber_acao()
        insert_query = """
                INSERT INTO acao (nome, ticket, valor_compra, quantidade_compra, data_compra, client_id)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
        values = (
            acao_info["nome"],
            acao_info["ticket"],
            acao_info["valor_compra"],
            acao_info["quantidade_compra"],
            acao_info["data_compra"],
            acao_info["client_id"],
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print("Alterações salvas com sucesso.")

    def deletar_acao(self):
        deleted_id = int(input("Qual o id da acao que você quer deletar? "))

        delete_query = """
               DElETE * FROM public.users WHERE id = %s;
               """
        values = (deleted_id,)
        self.cursor.execute(delete_query, values)
        self.connection.commit()
        print("Alterações salvas com sucesso.")

    def analise_carteira(self):
        client_cpf = cpf_validation()
        select_query = """SELECT a.ticket FROM acao as a INNER JOIN users as u ON a.cliente_id = u.id WHERE u.cpf = %s; 
        """
        values = (client_cpf,)
        self.cursor.execute(select_query, values)
        tickets = self.cursor.fetchall()
        analise(tickets)

    def relatorio_carteira(self):
        client_cpf = cpf_validation()
        select_query = """SELECT a.ticket FROM acao as a INNER JOIN users as u ON a.cliente_id = u.id WHERE u.cpf = %s; 
        """
        values = (client_cpf,)
        self.cursor.execute(select_query, values)
        tickets = self.cursor.fetchall()

        for acao in tickets:
            acao = yf.download(acao + ".SA", progress=False)
            print(acao.tail(), "\n")
