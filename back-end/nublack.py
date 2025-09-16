import psycopg2
from psycopg2 import sql, errors
from database import create_database
from createtables import create_tables

# Função principal para criar o banco de dados e as tabelas
def main():
    # Primeiro, cria o banco de dados
    create_database()
    # Em seguida, cria as tabelas dentro do banco de dados
    create_tables()

if __name__ == "__main__":
    main()
    # Executa a função principal