"""
-- Insere um novo cliente na tabela
INSERT INTO clientes (name, address, phone, created_at) 
	VALUES ('Isaac', 'Rua A, nº 12', '(11) 99876-5432', '2024-01-31');

-- Insere um novo fornecedor na tabela com a data default
INSERT INTO fornecedores (name, phone, email, notes)
	VALUES ('ACME Inc.', '(11) 1111-1111', 'acme@email.com', 'N/a');

-- Insere um novos lanches na tabela de outra maneira
INSERT INTO lanches (name, preco, descricao) 
	VALUES (
    'Hamburguer',
    8,
    'Pão, carne, alface, tomate, molho especial, batata palha'
);

-- Insere varios ingredientes ao mesmo tempo na tabela
INSERT INTO estoque_ingredientes (name, categoria, quantidade)
VALUES
	('Ovos', 'Diversos', 24),
    ('Tomate', 'Frutas', 14),
    ('Queijo', 'Diversos', 40),
    ('Presunto', 'Carnes', 40);

-- Retorna todas as tabelas de clientes
SELECT * FROM clientes;

-- Também é possível especificar quais campos queremos obter da tabela
SELECT id, name, phone FROM clientes;

-- Mdificar o formato dos resultados, como o nome das colunas
SELECT
	id AS Código,
	name AS Lanche,
	descricao AS Descrição,
	preco AS Preço
FROM lanches;

-- Permite filtrarmos os resultados de acordo com uma condição
SELECT * FROM estoque_ingredientes WHERE quantidade < 20;
SELECT * FROM estoque_ingredientes WHERE categoria = 'Diversos';
SELECT * FROM estoque_ingredientes WHERE categoria = 'Diversos' and quantidade < 25;
SELECT * FROM estoque_ingredientes WHERE categoria = 'Diversos' or categoria = 'Frutas';
SELECT * FROM estoque_ingredientes WHERE categoria IN ('Carnes', 'Frutas'); -- Carnes and Frutas

-- Ordena pelo nome em ordem alfabética decrescente
SELECT * FROM Clientes ORDER BY name DESC;
-- Ordena por telefone baseado nos primeiros dígitos em ordem crescente
SELECT * FROM Clientes ORDER BY phone ASC;

SELECT * FROM Clientes LIMIT 4;
SELECT * FROM Clientes ORDER BY name ASC LIMIT 4 OFFSET 4; -- Seleciona os 4 primeiros e pula os 4 primeiros

SELECT COUNT(id) FROM Clientes;
SELECT COUNT(id) AS Clients_count FROM Clientes;
SELECT SUM(quantidade) AS Total FROM estoque_ingredientes;
SELECT AVG(quantidade) AS Média FROM estoque_ingredientes;

-- Obtém todos os clientes com nome começando com 'V'
SELECT * FROM Clientes WHERE name LIKE 'V%';
-- Obtém todos os clientes onde a segunda letra do nome é 'a'
SELECT * FROM Clientes WHERE name LIKE '_a%';
-- Obtém todos os clientes onde a última letra do nome é 'd'
SELECT * FROM Clientes WHERE name LIKE '%d';
-- Obtém todos os clientes que possuem 'an' em alguma parte do nome
SELECT * FROM Clientes WHERE name LIKE '%an%';

-- Obtém os clientes com a letra 'B' em qualquer parte do nome
SELECT * FROM Clients WHERE name LIKE '%B%';
-- Obtém os clientes com as letras 'B' ou 'b' em qualquer parte do nome
SELECT * FROM Clients WHERE name ILIKE '%B%';
"""