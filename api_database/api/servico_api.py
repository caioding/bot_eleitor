from flask import Flask, make_response, jsonify, request

import sys
import os

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repository"))
sys.path.append(module)

import eleitor
import usuario

app_api = Flask("bot_eleitor")
app_api.config["JSON_SORT_KEYS"] = False


# Rota pra inicio da API #
@app_api.route("/", methods=["GET"])
def hello_world():
    return "API do Eleitor - OK"


# -- Inicio: Serviços da api usuário
@app_api.route("/eleitor", methods=["POST"])
def criar_eleitor():
    eleitor_json = request.json
    # cpf_eleitor=0

    try:
        eleitor.criar_eleitor(eleitor_json)
        successo = True
        _messagemm = "Eleitor Inserido!"

    except Exception as ex:
        successo = False
        _messagemm = f"Erro: {ex}"

    return make_response(jsonify(status=successo, message=_messagemm))


@app_api.route("/eleitor", methods=["GET"])
def lista_eleitores():
    lista_eleitores = list()
    lista_eleitores = eleitor.lista_eleitores()

    if len(lista_eleitores) == 0:
        successo = False
        _messagem = "Lista vazia"
    else:
        successo = True
        _messagem = "Lista OK"

    return make_response(jsonify(status=successo, message=_messagem, data=lista_eleitores))


@app_api.route("/eleitor/<int:cpf>", methods=["GET"])
def obter_eleitor_cpf(cpf):
    eleitor_cpf = list()
    eleitor_cpf = eleitor.obter_eleitor_cpf(cpf)

    if len(eleitor_cpf) == 0:
        successo = False
        _messagem = "Eleitor não encontrado!"
    else:
        successo = True
        _messagem = "Eleitor encontrado!"

    return make_response(jsonify(status=successo, _messagem=_messagem, data=eleitor_cpf))


@app_api.route("/eleitor", methods=["PUT"])
def atualizar_eleitor():
    eleitor_json = request.json

    try:
        eleitor.atualizar_eleitor(eleitor_json)
        successo = True
        _messagem = "Infos eleitor atualizadas"

    except Exception as ex:
        successo = False
        _messagem = f"Erro: {ex}"

    return make_response(jsonify(status=successo, message=_messagem))


@app_api.route("/eleitor/<int:cpf>", methods=["DELETE"])
def deletar_eleitor(cpf):
    try:
        eleitor.deletar_eleitor(cpf)
        successo = True
        _messagem = "Eleitor removido!"

    except Exception as ex:
        successo = False
        _messagem = f"Erro: {ex}"

    return make_response(jsonify(status=successo, mensagem=_messagem))

# Usuário

# Inserir usuário
@app_api.route('/usuario', methods=['POST'])
def criar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    id_usuario=0
    try:
        id_usuario = usuario.criar_usuario(usuario_json)
        sucesso = True
        _mensagem = 'Usuario inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_usuario
        )
    )
# Fim: criar_usuario()

# Atualizar usuário
@app_api.route('/usuario', methods=['PUT'])
def atualizar_usuario():
    usuario_json = request.json
    id = int(usuario_json['id'])
    try:
        if usuario.existe_usuario(id) == True:
            usuario.atualizar_usuario(usuario_json)
            sucesso = True
            _mensagem = 'Usuario alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Alteracao do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

# Deletar usuário
@app_api.route('/usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        if usuario.existe_usuario(id) == True:
            usuario.deletar_usuario(id)
            sucesso = True
            _mensagem = 'Usuario deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusao de usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

# Serviço: Obter usuário pelo id
@app_api.route('/usuario/<int:id>', methods=['GET'])
def obter_usuario_id(id):
    # Declarando uma tupla vazia
    usuario_id = ()
    sucesso = False
    if usuario.existe_usuario(id) == True:
        usuario_id = usuario.obter_usuario_id(id)
        sucesso = True
        _mensagem = 'Usuario encontrado com sucesso'
    else:
        sucesso = False
        _mensagem = 'Usuario existe'
    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = usuario_id
        )
    )
# Fim: obter_usuario_id(id)

# Serviço: Obter a lista de usuário
@app_api.route('/usuario', methods=['GET'])
def lista_usuarios():
    lista_usuario = list()
    lista_usuario = usuario.lista_usuarios()
    if len(lista_usuario) == 0:
        sucesso = False
        _mensagem = 'Lista de usuario vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de usuario'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_usuario
        )
    )
# Fim: lista_usuarios()


app_api.run()