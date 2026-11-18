-- Exemplo dos slides de subconsultas (estudante e nota), com nomes trocados pela equipe.
CREATE TABLE estudante (id_estudante CHAR(4) PRIMARY KEY, nome VARCHAR(30) NOT NULL);
CREATE TABLE nota (id_estudante CHAR(4) PRIMARY KEY REFERENCES estudante (id_estudante), nota_total INTEGER NOT NULL);
INSERT INTO estudante VALUES ('V001', 'Alice'), ('V002', 'Bento'), ('V003', 'Cecília'), ('V004', 'Diego');
INSERT INTO nota VALUES ('V001', 95), ('V002', 80), ('V003', 74), ('V004', 81);
