import sqlite3

# 1 - Criando o Banco de Dados
connection = sqlite3.connect("movies.db") # connection é a variavél e movies.db é o Banco de Dados

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)