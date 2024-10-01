# Import for the Web Bot
# from botcity.web import WebBot, Browser, By
import requests
# # Import for integration with BotCity Maestro SDK
from botcity.maestro import *
# #configuracao chromer
# from webdriver_manager.chrome import ChromeDriverManager
# #configurar http, antes tem executar terminal: pip install botcity-http-plugin
from botcity.plugins.http import BotHttpPlugin
from datetime import datetime

import planilha.planilha as planilha
import e_mail.e_mail as e_mail
import pdf.pdf as pdf

def criar_eleitor(eleitor):
    url = 'http://127.0.0.1:5000/eleitor'
    headers = {'Content-Type': 'application/json'}
    data_nascimento = eleitor["DATA_NASCIMENTO"].strftime('%d/%m/%Y')

    data = {
        "cpf": eleitor["CPF"],
        "nome": eleitor["NOME"],
        "data_nascimento": data_nascimento,
        "nome_mae": eleitor["NOME_MAE"],
        "cep": eleitor["CEP"],
        "nro_endereco": eleitor["NRO_ENDERECO"],
    }

    try:
        resposta = requests.post(url=url,headers=headers, json=data)
        resposta.raise_for_status()  # Verifica se houve algum erro na requisição
        # Retorna a resposta em formato JSON
        retorno = resposta.json()
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
    except Exception as e:
        print(f"Erro: {e}")

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    print('Leitura do arquivo Excel...')
    arq_excel = '/home/caio/bot_eleitor/bot_eleitor/resources/RelacaoEleitor.xlsx'
    sheet = 'CPF'  
    df = planilha.ler_excel(arq_excel,sheet)
    planilha.exibir_dados_excel(df)
    print('Inserindo eleitors no banco de dados...')
    for index, eleitor in df.iterrows():
        criar_eleitor(eleitor)
    # planilha.exibir_dados_excel(df)
    
    print('Fim do processamento...')
    
def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()