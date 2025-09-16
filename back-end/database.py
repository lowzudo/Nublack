#IMPORTS OBRIGATÓRIOS
import psycopg2
from psycopg2 import sql, errors


#CRIAÇÃO DO BANCO DE DADOS
def create_database():

    #Conectando ao "banco de dados" padrão do Postgre
    conexao = psycopg2.connect(
        host = 'localhost',
        database = 'postgres',
        user = 'postgres',
        password = 'Vitinho07'
    )
    #Obrigatório para criar
    conexao.autocommit = True
    cursor = conexao.cursor()

    #Tentando criar o banco de dados
    try:
        cursor.execute('CREATE DATABASE Nublack')
        print("Banco de dados criado com sucesso.")
    
    #Não criará caso o banco já exista
    except errors.DuplicateDatabase:
        print("O banco de dados Nublack, já está criado.")

    #Tratamento de erro
    except Exception as e:
        print(f"Erro ao criar o banco de dados {e}")

    #Fechando as conexões que foram abertas
    finally:
        conexao.close()
        cursor.close()

#FUNÇÃO PARA SE CONECTAR COM O BANCO DE DADOS QUE CRIAMOS
def connect_database():
    try:
        #Aqui se conecta ao banco de dados criado
        print("Tentando se conectar ao banco de dados Nublack")

        conexao = psycopg2.connect(
            host = 'localhost',
            database = 'nublack',
            user = 'postgres',
            password = 'Vitinho07'
        )
        print("Conectado ao banco de dados Nublack com sucesso")
        return conexao
    
    #Tratamento de erro
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None