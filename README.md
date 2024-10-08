# bot_eleitor

### Passo 1. Levantar o banco de dados MySQL no XAMPP ou Docker com a port 3306

### Passo 2. Criar a conexão com o banco de dados por meio da extensão MySQL do VS Code (Jun Han)
    - host: localhost
    - user: root
    - senha: (sem senha, só clicar enter)
    - porta: 3306
    - certificate file path: (sem nada, só clicar enter)

### Passo 3. Executar o arquivo script.sql por meio do "Run MySQL Query" para criar o schema

### Passo 4. Configurar o arquivo database.py
#### Exemplo

    - host='localhost',
    - port='3306',
    - user='root',
    - password='',
    - database='banco'

### Passo 5. Criar ambiente virtual chamado env_api_database
```sh
python3 -m venv env_api_database
```

### Passo 6. Ativar o ambiente (pode usar o Select Interpreter do VS Code para isso)
#### No Linux
```sh
. env_api_database/bin/activate
```
#### No Windows
```sh
. \env_api_database\Script\activate.bat
```

### Passo 7. Verificar se o ambiente está ativado e na versão correta
```sh
python --version
```

### Passo 8. Instlar o flask e mysql connector
```sh
pip install mysql-connector-python
```

### Passo 9. Testar a api com requisições

### Passo 10. Instalar cookiecutter
```sh
python -m pip install --upgrade cookiecutter
```

### Passo 11. Criar e escolher tipo de bot
```sh
python -m cookiecutter https://github.com/botcity-dev/bot-python-template/archive/v2.zip
```

### Passo 12. Criar ambiente virtual no Anaconda, caso não tenha um que possa usar
```sh
conda create --name bot_eleitor python=3.10
```

### Passo 13. Ativar o ambinte do Anaconda (pode usar o VS Code igual foi usado no env)
```sh
conda activate bot_eleitor
```

### Passo 14. Instalar requirements
```sh
pip install -r requirements.txt
```

### Passo 15. Atualizar o requirements
```sh
pip freeze > requirements.txt
```
