CREATE DATABASE cadastro_de_filmes_db;
USE cadastro_de_filmes_db;

CREATE TABLE filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    diretor VARCHAR(255) NOT NULL,
    genero VARCHAR(100) NOT NULL,
    ano INT NOT NULL
);

INSERT INTO filmes (titulo, genero, ano) VALUES
('O Poderoso Chefão', 'Drama', 1972),
('Star Wars', 'Ficção Científica', 1977),
('Toy Story', 'Animação', 1995);

SELECT * FROM filmes;