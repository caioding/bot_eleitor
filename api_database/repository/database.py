import mysql.connector


def criar_db():
    try:
        # Configuração do Banco de Dados MySQL
        mydb = mysql.connector.connect(
            host='172.17.0.2',
            port='3306',
            user='mydb',
            password='neosdb',
            database='banco'
        )
    except Exception as ex:
        print(f'Ocorreu erro na conexao com o Banco de Dados: {ex}')

    return mydb


        # mydb = mysql.connector.connect(
        #     host='localhost',
        #     port='3306',
        #     user='root',
        #     password='',
        #     database='banco'
        # )