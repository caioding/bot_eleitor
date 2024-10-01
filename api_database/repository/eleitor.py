import database


# Verificar se eleitor existe
def verificar_eleitor_existe(cpf):
    existe: False

    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'"

        cursor.execute(sql)
        lista_eleitores = cursor.fetchall()

        if len(lista_eleitores) == 0:
            existe = False
        else:
            existe = True

    except Exception as ex:
        print(f"Erro: {ex}")

    return existe


# Add eleitor com as devidas informações
def criar_eleitor(eleitor):
    try:
        conect = database.criar_db()
        cursor = conect.cursor()

        # sql = f"INSERT INTO eleitor(cpf, nome, data_nascimento, nome_mae, cep, nro_endereco, nro_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais) VALUES('{eleitor['cpf']}','{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}', '{eleitor['cep']}', '{eleitor['nro_endereco']}', '{eleitor['nro_titulo']}', '{eleitor['situacao']}', '{eleitor['secao']}', '{eleitor['zona']}', '{eleitor['local_votacao']}', '{eleitor['endereco_votacao']}', '{eleitor['bairro']}', '{eleitor['municipio_uf']}', '{eleitor['pais']}')"
        sql = f"INSERT INTO eleitor(cpf, nome, data_nascimento, nome_mae, cep, nro_endereco, nro_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais) VALUES('{eleitor['cpf']}','{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}', '{eleitor['cep']}', '{eleitor['nro_endereco']}', '{eleitor['nro_titulo']}', '{eleitor['situacao']}', '{eleitor['secao']}', '{eleitor['zona']}', '{eleitor['local_votacao']}', '{eleitor['endereco_votacao']}', '{eleitor['bairro']}', '{eleitor['municipio_uf']}', '{eleitor['pais']}')"

        cursor.execute(sql)
        ultimo_cpf = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f"Erro: {ex}")

    finally:
        cursor.close()
        conect.close()

    return ultimo_cpf


# Fornecer lista de eleitores
def lista_eleitores():
    eleitores = list()

    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = "SELECT * FROM eleitor ORDER BY nome"

        cursor.execute(sql)
        lista_eleitores = cursor.fetchall()

        for eleitor in lista_eleitores:

            eleitores.append(
                {
                    "cpf": eleitor[0],
                    "nome": eleitor[1],
                    "data_nascimento": eleitor[2],
                    "nome_mae": eleitor[3],
                    "cep": eleitor[4],
                    "nro_endereco": eleitor[5],
                    "nro_titulo": eleitor[6],
                    "situacao": eleitor[7],
                    "secao": eleitor[8],
                    "zona": eleitor[9],
                    "local_votacao": eleitor[10],
                    "endereco_votacao": eleitor[11],
                    "bairro": eleitor[12],
                    "municipio_uf": eleitor[13],
                    "pais": eleitor[14],
                }
            )

    except Exception as ex:
        print(f"Erro: {ex}")

    finally:
        cursor.close()
        conect.close()

    return eleitores


# Buscar eleitor pelo cpf
def obter_eleitor_cpf(cpf):
    eleitores = list()

    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'"

        cursor.execute(sql)
        lista_eleitores = cursor.fetchall()

        for eleitor in lista_eleitores:

            eleitores.append(
                {
                    "cpf": eleitor[0],
                    "nome": eleitor[1],
                    "data_nascimento": eleitor[2],
                    "nome_mae": eleitor[3],
                    "cep": eleitor[4],
                    "nro_endereco": eleitor[5],
                    "nro_titulo": eleitor[6],
                    "situacao": eleitor[7],
                    "secao": eleitor[8],
                    "zona": eleitor[9],
                    "local_votacao": eleitor[10],
                    "endereco_votacao": eleitor[11],
                    "bairro": eleitor[12],
                    "municipio_uf": eleitor[13],
                    "pais": eleitor[14],
                }
            )

    except Exception as ex:
        print(f"Erro: {ex}")

    finally:
        cursor.close()
        conect.close()

    return eleitores


# Atualizar infos cadastradas
def atualizar_eleitor(eleitor):
    try:
        conect = database.criar_db()
        cursor = conect.cursor()

        # sql = f"UPDATE eleitor SET cpf = '{eleitor['cpf']}', nome = '{eleitor['nome']}', data_nascimento = '{eleitor['data_nascimento']}', nome_mae = '{eleitor['nome_mae']}', cep = '{eleitor['cep']}', nro_endereco = '{eleitor['nro_endereco']}', nro_titulo = '{eleitor['nro_titulo']}', situacao = '{eleitor['situacao']}', secao = '{eleitor['secao']}', zona = '{eleitor['zona']}', local_votacao = '{eleitor['local_votacao']}', endereco_votacao = '{eleitor['endereco_votacao']}', bairro = '{eleitor['bairro']}', municipio_uf = '{eleitor['municipio_uf']}', pais = '{eleitor['pais']}' WHERE cpf = '{eleitor['cpf']}'"

        sql = f"UPDATE eleitor SET cpf = '{eleitor['cpf']}', nome = '{eleitor['nome']}', data_nascimento = '{eleitor['data_nascimento']}', nome_mae = '{eleitor['nome_mae']}', cep = '{eleitor['cep']}', nro_endereco = '{eleitor['nro_endereco']}' WHERE cpf = '{eleitor['cpf']}'"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f"Erro: {ex}")

    finally:
        cursor.close()
        conect.close()


# Remover eleitor
def deletar_eleitor(cpf):
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"DELETE FROM eleitor WHERE cpf = {cpf}"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f"Erro: {ex}")

    finally:
        cursor.close()
        conect.close()