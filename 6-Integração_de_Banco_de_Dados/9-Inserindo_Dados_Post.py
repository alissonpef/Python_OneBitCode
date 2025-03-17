from conexao_post import conn

cursor_obj = conn.cursor()

# Tem que ser uma lista com uma tupla
games = [
    ('Star Wars Survivor', 2023, 9.5),
    ('The Last of Us', 2023, 8.5)
]

for game in games:
    cursor_obj.execute("""
                       INSERT into game(name, year, score) 
                       VALUES (%s, %s, %s)
                       """, game)

conn.commit()
conn.close()
