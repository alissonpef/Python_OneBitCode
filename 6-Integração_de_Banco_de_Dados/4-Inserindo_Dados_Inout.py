import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# 1 - Solicitando Dados do Usuário
name = input("\nNome do Filme: ")
year = int(input("Ano de lançamento: "))
score = float(input("Nota do filme: "))

# 2 - Inserindo Dados via Input
cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES (?,?,?)
""", (name, year, score))

connection.commit()
print("Dados inseridos com sucesso.")
connection.close()