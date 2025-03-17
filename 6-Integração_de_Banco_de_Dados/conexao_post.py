import psycopg2

conn = psycopg2.connect(
    database='fliperama',
    user='postgres',
    password='qwe12345',
    host='localhost',
    port= '5432'
)
