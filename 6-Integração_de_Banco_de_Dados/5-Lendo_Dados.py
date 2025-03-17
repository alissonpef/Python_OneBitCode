import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# 1 - Lendo Dados
data = cursor.execute("""
                    SELECT * FROM movies
""")
print(data.fetchall()) # Printa todos os dados do Banco de Dados
print("\n")
# 2 - Iterando os Dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}") # Printa cada filme(linha) em uma linha diferente
    
# 3 - Ordenando pelo Score
print("\nFilmes Ordenados pelo Score:")
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f"{row}")

connection.close()
