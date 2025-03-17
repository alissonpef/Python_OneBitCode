import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# 1 - Solicitando Dados do Usuário
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}") 
id = int(input("Informe o ID do filme que deseja atualizar: "))
name = input("Nome do Filme: ")

# 2 - Atualizando Dados
cursor.execute("""
UPDATE movies set name = ? 
WHERE id = ?
""", (name, id))

connection.commit()
print("Dados atualizados com sucesso.")
connection.close()