"""
Server [localhost]: (pressione Enter, se for local)
Database [postgres]: Nome do banco de dados
Port [5432]: (pressione Enter, se for a padrão)
Username [postgres]: (digite seu usuário, ou pressione Enter se for "postgres")
Password for user postgres: (digite sua senha e pressione Enter)

CREATE DATABASE first_database;
DROP DATABASE first_database;
ALTER RENAME to teste;

CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
	email VARCHAR(100) UNIQUE
);

ALTER TABLE clientes ADD COLUMN birthday DATE;
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
ALTER TABLE clientes ALTER COLUMN phone DROP NOT NULL;
ALTER TABLE clientes RENAME COLUMN name TO full_name;
ALTER TABLE clientes DROP COLUMN birthday;
"""