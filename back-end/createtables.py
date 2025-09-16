import psycopg2
from psycopg2 import sql
from database import connect_database

#FUNÇÃO PARA CRIAR AS TABELAS DO BANCO DE DADOS
def create_tables():

    #Aqui nós usamos o import connect_database para estabelecer a conexão com o banco de dados
    conexao = connect_database()
    #Caso não exista ou não consiga se conectar, dara erro e mostrará a mensagem abaixo
    if not conexao:
        return "Conexão não estabelecida."
    
    #Tudo que será executado no banco de dados, será feito através do cursor, aqui estamos criando ele
    cur = conexao.cursor()

    #Criação da tabela em sí
    try:
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS conta_pessoa(
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    idade INT NOT NULL CHECK(idade >= 18),
                    cpf INT NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    senha VARCHAR(20) NOT NULL,
                    conta_bancaria VARCHAR(50) NOT NULL
                )
""")
        #SERIAL PRIMARY KEY cria uma coluna de ID que é auto-incrementada
        #VARCHAR(50) define o tamanho máximo da string
        #NOT NULL garante que o campo não pode ser nulo
        #CHECK(idade >= 18) garante que a idade seja maior ou igual a 18
        #UNIQUE garante que o email seja único na tabela
        #INT Número inteiro

        #Obrigatório para salvar as alterações
        conexao.commit()

    #Tratamento de erro
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")

    #Fechando o cursor e a conexão
    finally:
        cur.close()
        conexao.close()
        print("Tabelas criadas com sucesso.")