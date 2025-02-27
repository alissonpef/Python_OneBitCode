"""
CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	total DECIMAL(10, 2),
	customer_id INT,
	FOREIGN KEY (customer_id) REFERENCES customers (id)
);

INSERT INTO customers (name, email) VALUES
	('Clark Kent', 'clark@email.com'),
	('Bruce Wayne', 'bruce@email.com'),
	('Diana Prince', 'diana@email.com');

INSERT INTO orders (total, customer_id) VALUES
	(100.00, 1),
	(240.00, 2),
	(200.00, 1),
	(420.00, 3),
	(700.00, 2);

DELETE FROM customers WHERE id = 1; -- Lançará um erro de violação de constraint

CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	total DECIMAL(10, 2),
	customer_id INT,
	FOREIGN KEY (customer_id) REFERENCES customers (id)
        ON DELETE CASCADE (Deleta tudo em cascata (todos os pedidos))
        ON CHANGE CASCADE
        
        -- ON DELETE RESTRICT (Padrão, vai dar erro e não deixa)
        -- ON CHANGE RESTRICT 

        -- ON DELETE SET NULL (Seta para nulo)
        -- ON CHANGE SET NULL 

        -- ON DELETE DEFAULT (Seta para o valor default da chave)
        -- ON CHANGE DEFAULT 
);

DELETE FROM customers WHERE id = 1; -- Exclua um cliente e observe o efeito nos pedidos
UPDATE customers SET id = 40 WHERE id = 2; -- Atualize um cliente e observe o efeito nos pedidos

"""