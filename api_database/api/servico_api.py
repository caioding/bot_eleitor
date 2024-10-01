from flask import Flask, make_response, jsonify, request

import sys
import os

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repository"))
sys.path.append(module)

import eleitor  # noqa: E402

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
        # cpf_eleitor = eleitor.criar_eleitor(eleitor_json)  # noqa: F841
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


app_api.run()