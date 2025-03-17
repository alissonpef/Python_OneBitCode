from conexao_post import conn

cursor_obj = conn.cursor()

sql = """ 
        DELETE FROM game
        WHERE id = %s
"""

cursor_obj.execute(sql, (1,)) # Tem que ser "1," e não "1"

conn.commit()
conn.close()
