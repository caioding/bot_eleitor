from repository import database

# Inserir eleitor
def criar_eleitor(eleitor):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = (
            f"INSERT INTO eleitor(cpf, nome, data_nascimento, nome_mae, nro_titulo, situacao, secao, zona, local_votacao, endereço, bairro, municipio_uf, pais) "
            " VALUES('{eleitor['cpf']}','{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}','{eleitor['nro_titulo']}', "
            " '{eleitor['situacao']}', '{eleitor['secao']}','{eleitor['zona']}','{eleitor['local_votacao']}','{eleitor['endereço']}','{eleitor['bairro']}', "
            " '{eleitor['municipio_uf']}','{eleitor['pais']}' )"
        )
        
        print(sql)
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: criar_eleitor(produto)

# Ver se eleitor existe 
def existe_eleitor(cpf):
    exite: False
    eleitor = ()
    try:
        conect = database.criar_db
        cursor = conect.cursor()
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'"
        cursor.execute(sql)
        eleitor = cursor.fetchone()
        if eleitor is not None:
            if len(eleitor) == 1:
                exite = True
            else:
                exite = False
        else:
            exite = False
    except Exception as ex:
        print(f'Erro: Ver se eleitor existe: {ex}')
    finally:
        cursor.close()
        conect.close()
    return exite

# Fim: existe_eleitor

# Obter o eleitor pelo cpf
def obter_eleitor_cpf(cpf):
    eleitor = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'" 
        cursor.execute(sql)
        eleitor = cursor.fetchone()
    except Exception as ex:
        print(f'Erro: Obter eleitor: {ex}')
    finally:
        cursor.close()
        conect.close()
    return eleitor

# Fim: obter_eleitor_cpf
                  
# Listar Eleitores
def lista_eleitores():
    eleitores = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = 'SELECT * FROM eleitor ORDER BY nome'
        cursor.execute(sql)
        lista_eleitor = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for eleitor in lista_eleitor:
            eleitores.append(
                {
                    'cpf': eleitor[0],
                    'nome': eleitor[1],
                    'data_nascimento': eleitor[2],
                    'nome_mae': eleitor[3],
                    'nro_titulo': eleitor[4],
                    'situacao': eleitor[5],
                    'secao': eleitor[6],
                    'zona': eleitor[7],
                    'local_votacao': eleitor[8],
                    'endereço': eleitor[9],
                    'bairro': eleitor[10],
                    'municipio_uf': eleitor[11],
                    'pais': eleitor[12]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar eleitores: {ex}')
    finally:
        cursor.close()
        conect.close()
    return eleitores

# Fim: lista_eleitores

# Deletar eleitor pelo cpf
def deletar_eleitor(cpf):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"DELETE FROM eleitor WHERE cpf = '{cpf}'"
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na exclusão: {ex}')
    finally:
        cursor.close()
        conect.close()  

# Fim: deletar_eleitor
