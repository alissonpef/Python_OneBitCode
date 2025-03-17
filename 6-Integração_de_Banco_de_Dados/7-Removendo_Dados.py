import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# 1 - Solicitando Dados do Usuário
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}") 
id = int(input("Informe o ID do filme que deseja excluir: "))

# 2 - Removendo Dados
cursor.execute("""
DELETE FROM movies 
WHERE id = ?
""", (id,))

connection.commit()
print("Dados atualizados com sucesso.")
connection.close()