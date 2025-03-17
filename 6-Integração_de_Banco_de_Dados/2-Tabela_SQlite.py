import sqlite3

connection = sqlite3.connect("movies.db") 

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Criando a Tabela  
cursor.execute("""
CREATE TABLE movies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
       );
""")
print("Tabela criada com sucesso.")

# 4 - Fechando conexão
connection.close()