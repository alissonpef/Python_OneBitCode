# A principal vantagem de ter um ambiente virtual de desenvolvimento, é que isolamos as bibliotecas que serão utilizadas 
# em um projeto, o que vai facilitar bastante quando se quiser fazer o deploy de um projeto.

# Para criar o ambiente virtual de desenvolvimento, pode-se executar o comando no terminal: python -m venv .venv
# 1. Estamos indicando que vamos criar um diretório .venv, que vai ser o diretório que armazenará as bibliotecas que ]
# instalarmos nesse ambiente de desenvolvimento.
# 2. Para ativar o ambiente virtual de desenvolvimento, pode ser executado o comando: ./.venv/Scripts/activate
# 3. Como pode ser visto na imagem abaixo, já estamos dentro do ambiente virtual de desenvolvimento.

# source ./.venv/Scripts/activate

# pip install nome_do_pacote
# 1. pip list
# 2. pip freeze -l > requirements.txt.
# 3. pip install -r requirements.txt