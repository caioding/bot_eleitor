# bot_eleitor

Levantar o banco de dados MySQL no XAMPP ou Docker com a port 3306

Criar a conexão com o banco de dados por meio da extensão MySQL do VS Code (Jun Han)
    host: localhost
    user: root
    senha: (sem senha, só clicar enter)
    porta: 3306
    certificate file path: (sem nada, só clicar enter)

Executar o arquivo script.sql por meio do "Run MySQL Query" para criar o schema

Configurar o arquivo database.py
Exemplo
    host='localhost,
    port='3306',
    user='root',
    password='',
    database='banco'

Criar ambiente virtual chamado env_api_database
    python3 -m venv env_api_database

Ativar o ambiente (pode usar o Select Interpreter do VS Code para isso)
No Linux
    . env_api_database/bin/activate 
No Windows
    . \env_api_database\Script\activate.bat

Verificar se o ambiente está ativado e na versão correta
    python --version

Instlar o flask e mysql connector
    pip install mysql-connector-python

Testar a api com requisições

Criar ambiente virtual no Anaconda, caso não tenha um que possa usar
