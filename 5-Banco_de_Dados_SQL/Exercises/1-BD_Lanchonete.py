"""
Exercicio 1:
* Banco de dados para uma lanchonete
Crie um arquivo SQL (no formato do PostgreSQL) com os comandos para criar um banco de dados para uma lanchonete 
armazenar as informações do seu sistema. Esse arquivo deve então criar, caso não existam, as seguintes tabelas e colunas:

1. Clientes  
   - id  
   - nome  
   - telefone  
   - endereço  
   - data_de_cadastro  

2. Fornecedores  
   - id  
   - nome  
   - telefone  
   - email  
   - data_de_contratacao  
   - observacoes  

3. Lanches  
   - id  
   - nome  
   - descricao  
   - preco  

4. Pedidos  
   - id  
   - mesa  
   - data_hora_pedido  
   - situacao  

5. Ingredientes em estoque  
   - id  
   - nome  
   - categoria  
   - quantidade  
"""
"""
CREATE DATABASE db_lanchonete;

CREATE TABLE IF NOT EXISTS clientes (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   phone VARCHAR(20),
   addres VARCHAR(255),
   created_at DATE NOT NULL DEFAULT CURRENT_DATE 
);

CREATE TABLE IF NOT EXISTS fornecedores (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   phone VARCHAR(20),
   email VARCHAR(100),
   hiring_date DATE NOT NULL DEFAULT CURRENT_DATE,
   notes TEXT
);

CREATE TABLE IF NOT EXISTS lanches (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) NOT NULL,
   descricao TEXT,
   preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
   id SERIAL PRIMARY KEY,
   mesa INT NOT NULL,
   data_pedido TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   situacao VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS estoque_ingredientes (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255),
   categoria VARCHAR(50),
   quantidade INT NOT NULL DEFAULT 0
);

INSERT INTO clientes (name, phone, address) VALUES
   ('Nadeen Nassy', '(894) 3770999', '344 Comanche Circle'),
   ('Rufe Woolforde', '(876) 3190195', '1199 Garrison Junction'),
   ('Erl Bumphrey', '(828) 4611193', '279 Carey Way'),
   ('Libbey Allbut', '(780) 9682663', '0 Tennyson Pass'),
   ('Vick Saterthwait', '(858) 2707342', '8098 Carpenter Crossing'),
   ('Valma Leathlay', '(988) 1855788', '52 Pankratz Point'),
   ('Cathrin Balcers', '(854) 2908154', '58 Kipling Alley'),
   ('Fidelity Hurleston', '(169) 2896946', '99412 Nova Place'),
   ('Lane Beggio', '(102) 4251437', '625 Mcguire Place'),
   ('Abigale Ofield', '(414) 2709709', '4526 Ronald Regan Point'),
   ('Melisse Stappard', '(828) 1752818', '4 Sunnyside Lane'),
   ('Vito Breach', '(516) 2554781', '86120 Towne Court'),
   ('Jessalin Duckett', '(333) 6498842', '02 Artisan Center'),
   ('Bo Collie', '(163) 2032492', '0 Straubel Terrace'),
   ('Raphaela Krates', '(916) 8872820', '7798 3rd Street'),
   ('Lucian Draxford', '(827) 4937186', '739 Toban Way'),
   ('Philippa Sidon', '(475) 4933015', '64985 Clarendon Way'),
   ('Cordie Voce', '(937) 6629079', '767 Prairieview Road'),
   ('Easter Petrescu', '(135) 9137473', '32 Dayton Crossing');
"""

