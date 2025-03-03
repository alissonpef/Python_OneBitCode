"""
Exercício 4:
* Banco de dados para uma editora independente

Crie um banco de dados atendendo aos seguintes requisitos:
“Somos uma editora independente especializada na publicação de livros de diversos gêneros literários, incluindo ficção, 
não-ficção, biografias e autoajuda. Para gerenciar nosso acervo de livros e o relacionamento com autores e leitores, 
precisamos de um sistema automatizado.

Esse sistema deverá permitir que novos livros sejam cadastrados com informações detalhadas, como título, autor, gênero, 
data de publicação, ISBN e um breve resumo. É essencial que o sistema também permita o cadastro de autores, com i
nformações como nome, biografia, data de nascimento e, é claro, uma lista de livros publicados. Como muitos autores 
publicam mais de um livro, é importante que o cadastro do autor seja reaproveitado para todos os seus livros publicados.

Outra funcionalidade importante é o registro de leitores. Os leitores podem se registrar de forma anônima, mas deve ser 
possível se registrar informando o nome, pois enviaremos e-mails com avisos, novidades e promoções. Considerando isso, 
o e-mail é uma informação obrigatória para o cadastro. Outras informações importantes sobre os nossos leitores são a 
idade e o gênero, mas que devem ser opcionais, para que possamos entender melhor o nosso público.

Por fim, queremos que o sistema permita a inclusão de resenhas e avaliações dos leitores para os livros que leram. Cada 
resenha deve estar associada a um livro específico e a um leitor, e deve incluir um campo para a avaliação (nota de 1 a 5) 
e um comentário detalhado.”

CREATE TABLE IF NOT EXISTS authors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  biography TEXT,
  birthday DATE
);

CREATE TABLE IF NOT EXISTS genres (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  genre_id INT NOT NULL REFERENCES genres(id),
  publication_date DATE,
  isbn VARCHAR(255),
  summary TEXT
);

CREATE TABLE IF NOT EXISTS book_authors (
  book_id INT,
  author_id INT,
  PRIMARY KEY (book_id, author_id),
  FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE IF NOT EXISTS readers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  gender CHAR(1),
  birthday DATE
);

CREATE TABLE IF NOT EXISTS reviews (
  id SERIAL PRIMARY KEY,
  book_id INT NOT NULL REFERENCES books(id),
  readers_id INT NOT NULL REFERENCES readers(id),
  rating INT CHECK (rating >= 1 AND rating <= 5),
  comment TEXT
);
"""