"""
-- UPDATE nome_da_tabela 
-- SET campo1 = valor1, campo2 = valor2 
-- WHERE condicao;
UPDATE series SET situacao = 'Airing' WHERE situacao = 'Ongoing';
UPDATE filmes SET titulo='Star Wars: A New Hope', genero='Sci-Fi/Fantasy' WHERE id=2;
UPDATE filmes SET rating=8; -- Cuidar para não fazer isso

-- DELETE FROM nome_da_tabela 
-- WHERE condicao;
DELETE FROM series WHERE titulo='The Office';
DELETE FROM series WHERE ano < 2000 AND temporadas > 5;
DELETE FROM series; -- Cuidar para não fazer isso
"""