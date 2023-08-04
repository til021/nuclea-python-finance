import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


def get_db_connection():
    try:
        # Obtém os valores de conexão do ambiente usando 'os.getenv'
        database_url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(database_url)
        print("Conexão ao banco de dados PostgreSQL realizada com sucesso!")
        return connection
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False


def select_users_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    clients = cursor.fetchall()
    for client in clients:
        print(client)
    cursor.close()
    connection.close()
