"""
Exercício 2:
* Banco de dados para filmes e séries

Crie utilizando a linguagem SQL um banco de dados com duas tabelas: filmes e séries de TV. 
Inclua também o código de inserção dos dados usando como referência as tabelas abaixo:

Tabela de Filmes:
| ID | Título                                          | Diretor                         | Ano  | Gênero     | Duração | Avaliação | Bilheteria      | Custo          |
|----|-------------------------------------------------|---------------------------------|------|------------|---------|-----------|-----------------|----------------|
| 1  | Mad Max: Fury Road                              | George Miller                   | 2015 | Ação       | 120     | 8.1       | 375.200.000,00  | 150.000.000,00 |
| 2  | Star Wars                                       | George Lucas                    | 1977 | Sci-Fi     | 121     | 8.6       | 775.398.007,00  | 11.000.000,00  |
| 3  | Super Mario Bros                                | Aaron Horvath, Michael Jelenic  | 2023 | Animação   | 92      | 7.3       | 1.300.000.000,00| 100.000.000,00 |
| 4  | Pride and Prejudice                             | Joe Wright                      | 2005 | Romance    | 129     | 7.8       | 121.147.947,00  | 28.000.000,00  |
| 5  | Back to the Future                              | Robert Zemeckis                 | 1985 | Sci-Fi     | 116     | 8.5       | 381.109.762,00  | 19.000.000,00  |
| 6  | The Godfather                                   | Francis Ford Coppola            | 1972 | Crime      | 175     | 9.2       | 246.120.974,00  | 6.000.000,00   |
| 7  | The Lord of the Rings: The Return of the King   | Peter Jackson                   | 2003 | Fantasia   | 201     | 9.0       | 1.146.030.912,00| 94.000.000,00  |
| 8  | Treasure Planet                                 | Ron Clements, John Musker       | 2002 | Animação   | 95      | 7.2       | 109.578.115,00  | 140.000.000,00 |
| 9  | Jurassic Park                                   | Steven Spielberg                | 1993 | Aventura   | 127     | 8.1       | 1.043.580.597,00| 63.000.000,00  |
| 10 | About Time                                      | Richard Curtis                  | 2013 | Romance    | 123     | 7.8       | 87.100.000,00   | 12.000.000,00  |
| 11 | Transformers                                    | Michael Bay                     | 2007 | Ação       | 144     | 7.0       | 709.709.780,00  | 150.000.000,00 |

Tabela de Séries de TV:
| ID  | Título             | Criador                                     | Ano  | Gênero         | Temporadas | Episódios | Avaliação | Canal           | Situação     |           
|----|---------------------|---------------------------------------------|------|----------------|------------|-----------|-----------|-----------------|--------------|
| 1  | Breaking Bad        | Vince Gilligan                              | 2008 | Drama          | 5          | 62        | 9.5       | AMC             | Finalizada   |
| 2  | Game of Thrones     | David Benioff, D.B. Weiss                   | 2011 | Fantasia       | 8          | 73        | 9.3       | HBO             | Finalizada   |
| 3  | Stranger Things     | The Duffer Brothers                         | 2016 | Sci-Fi         | 4          | 34        | 8.7       | Netflix         | Em Andamento |
| 4  | Friends             | David Crane, Marta Kauffman                 | 1994 | Comédia        | 10         | 236       | 8.9       | NBC             | Finalizada   |
| 5  | The Office          | Greg Daniels                                | 2005 | Comédia        | 9          | 201       | 8.8       | NBC             | Finalizada   |
| 6  | Vikings             | Michael Hirst                               | 2013 | Drama Histórico| 6          | 89        | 8.5       | History Channel | Finalizada   |
| 7  | Lost                | J.J. Abrams, Damon Lindelof                 | 2004 | Mistério       | 6          | 121       | 8.4       | ABC             | Finalizada   |
| 8  | Once Upon a Time    | Edward Kitsis, Adam Horowitz                | 2011 | Fantasia       | 7          | 155       | 7.7       | ABC             | Finalizada   |
| 9  | The Mentalist       | Bruno Heller                                | 2008 | Crime          | 7          | 151       | 8.1       | CBS             | Finalizada   |
| 10 | Star Trek           | Gene Roddenberry                            | 1966 | Sci-Fi         | 3          | 79        | 8.4       | NBC             | Finalizada   |
| 11 | Cobra Kai           | Josh Heald, Jon Hurwitz, Hayden Schlossberg | 2018 | Ação           | 5          | 50        | 8.6       | Netflix         | Em Andamento |

Além disso, crie também as seguintes consultas:
- Todos os filmes em ordem alfabética.
- Todos os filmes com bilheteria acima de US$ 500 milhões.
- Os IDs, nomes, anos de lançamento, gêneros, número de temporadas e episódios, avaliações e situações das séries, ordenadas da mais recente para a mais antiga.
- Todas as séries já finalizadas ordenadas da melhor avaliação para a pior.
- Todos os filmes lançados antes dos anos 2000.
- Os títulos, anos de lançamento, gênero e avaliação dos filmes ordenados por sua avaliação pela crítica.
- A média de avaliação entre os filmes de até 2 horas e a média de avaliação dos filmes de mais de 2 horas (em colunas separadas).
- Os nomes, anos de lançamento e avaliações dos filmes ordenados pelo lucro obtido, além do próprio lucro obtido (considere lucro como bilheteria - custo).

CREATE TABLE IF NOT EXISTS filmes (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    diretor VARCHAR(255),
    ano INT,
    genero VARCHAR(100),
    duracao INT,
    avaliacao DECIMAL(3, 2),
    bilheteria DECIMAL(15, 2),
    custo DECIMAL(15, 2)
);

CREATE TABLE IF NOT EXISTS series (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    diretor VARCHAR(255),
    ano INT,
    genero VARCHAR(100),
    temporadas INT,
    episodios INT,
    avaliacao DECIMAL(3, 2),
    canal VARCHAR(100),
    situacao VARCHAR(50) NOT NULL
);

-- Linhas da tabela de filmes
INSERT INTO filmes (titulo, diretor, ano, genero, duracao, avaliacao, bilheteria, custo) VALUES
	('Mad Max: Fury Road', 'George Miller', 2015, 'Action', 120, 8.1, 375200000.00, 150000000.00),
	('Star Wars', 'George Lucas', 1977, 'Sci-Fi', 121, 8.6, 775398007.00, 11000000.00),
	('Super Mario Bros', 'Aaron Horvath, Michael Jelenic', 2023, 'Animation', 92, 7.3, 1300000000.00, 100000000.00),
	('Pride and Prejudice', 'Joe Wright', 2005, 'Romance', 129, 7.8, 121147947.00, 28000000.00),
	('Back to the Future', 'Robert Zemeckis', 1985, 'Sci-Fi', 116, 8.5, 381109762.00, 19000000.00),
	('The Godfather', 'Francis Ford Coppola', 1972, 'Crime', 175, 9.2, 246120974.00, 6000000.00),
	('The Lord of the Rings: The Return of the King', 'Peter Jackson', 2003, 'Fantasy', 201, 9.0, 1146030912.00, 94000000.00),
	('Treasure Planet', 'Ron Clements, John Musker', 2002, 'Animation', 95, 7.2, 109578115.00, 140000000.00),
	('Jurassic Park', 'Steven Spielberg', 1993, 'Adventure', 127, 8.1, 1043580597.00, 63000000.00),
	('About Time', 'Richard Curtis', 2013, 'Romance', 123, 7.8, 87100000.00, 12000000.00),
	('Transformers', 'Michael Bay', 2007, 'Action', 144, 7.0, 709709780.00, 150000000.00);

-- Linhas da tabela de séries
INSERT INTO series (titulo, diretor, ano, genero, temporadas, episodios, avaliacao, canal, situacao) VALUES
	('Breaking Bad', 'Vince Gilligan', 2008, 'Drama', 5, 62, 9.5, 'AMC', 'Ended'),
	('Game of Thrones', 'David Benioff, D.B. Weiss', 2011, 'Fantasy', 8, 73, 9.3, 'HBO', 'Ended'),
	('Stranger Things', 'The Duffer Brothers', 2016, 'Sci-Fi', 4, 34, 8.7, 'Netflix', 'Ongoing'),
	('Friends', 'David Crane, Marta Kauffman', 1994, 'Comedy', 10, 236, 8.9, 'NBC', 'Ended'),
	('The Office', 'Greg Daniels', 2005, 'Comedy', 9, 201, 8.8, 'NBC', 'Ended'),
	('Vikings', 'Michael Hirst', 2013, 'Historical Drama', 6, 89, 8.5, 'History Channel', 'Ended'),
	('Lost', 'J.J. Abrams, Damon Lindelof', 2004, 'Mystery', 6, 121, 8.4, 'ABC', 'Ended'),
	('Once Upon a Time', 'Edward Kitsis, Adam Horowitz', 2011, 'Fantasy', 7, 155, 7.7, 'ABC', 'Ended'),
	('The Mentalist', 'Bruno Heller', 2008, 'Crime', 7, 151, 8.1, 'CBS', 'Ended'),
	('Star Trek', 'Gene Roddenberry', 1966, 'Sci-Fi', 3, 79, 8.4, 'NBC', 'Ended'),
	('Cobra Kai', 'Josh Heald, Jon Hurwitz, Hayden Schlossberg', 2018, 'Action', 6, 50, 8.6, 'Netflix', 'Ongoing');

SELECT * FROM filmes ORDER BY titulo ASC;
SELECT nome FROM filmes WHERE bilheteria > 500000;
SELECT id, nome, ano, genero, temporada, episodio, avaliacao, situacao FROM series ORDER BY ASC;
SELECT * FROM series where situacao > 0;
SELECT * FROM filmes where lancamento > 2000;
SELECT titulo, lancamento, genero, avaliacao FROM filmes ORDER BY ASC;
"""
