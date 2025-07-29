import psycopg2
from psycopg2 import sql, errors

def create_database():
    conexao = psycopg2.connect(
        host = 'localhost',
        database = 'postgres',
        user = 'postgres',
        password = 'Vitinho07'
    )
    conexao.autocommit = True
    cursor = conexao.cursor()

    try:
        cursor.execute('CREATE DATABASE Nublack')
        print("Banco de dados criado com sucesso.")
    
    except errors.DuplicateDatabase:
        print("O banco de dados Nublack, já está criado.")

    except Exception as e:
        print(f"Erro ao criar o banco de dados {e}")

    finally:
        conexao.close()
        cursor.close()

def connect_database():
    try:
        conexao = psycopg2.connect(
            host = 'locahost',
            database = 'Nublack',
            user = 'postgres',
            password = 'Vitinho07'
        )
        print("Conectado ao banco de dados Nublack com sucesso")
        return conexao
    
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None