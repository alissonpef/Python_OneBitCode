import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# 1 - Inserindo Dados
# ID é gerado automaticamente
cursor.execute("""
INSERT INTO movies (name, year, score) 
VALUES ('Super Mario Bros', 2025, 9.5)
""")

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Avatar', 2025, 10.0)
""")

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Velozes & Furiosos', 2025, 8.5)
""")    

# 2 - Gravando Dados no BD
connection.commit()
print("Dados inseridos com sucesso.")

connection.close()