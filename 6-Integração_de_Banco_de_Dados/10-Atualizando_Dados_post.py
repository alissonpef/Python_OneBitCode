from conexao_post import conn

cursor_obj = conn.cursor()

sql = """ 
        UPDATE game
        SET name = %s
        WHERE id = %s
"""

cursor_obj.execute(sql, ("Fifa 25", 1))

conn.commit()
conn.close()
