-- Esquema dos exercícios de álgebra relacional (slides de BD), com dados da equipe para conferir as resoluções.
CREATE TABLE Ambulatorios (nroa INTEGER PRIMARY KEY, andar INTEGER NOT NULL, capacidade INTEGER);
CREATE TABLE Medicos (codm INTEGER PRIMARY KEY, CPF CHAR(11) UNIQUE, nome VARCHAR(40), idade INTEGER, cidade VARCHAR(30),
                      especialidade VARCHAR(30), nroa INTEGER REFERENCES Ambulatorios (nroa));
CREATE TABLE Pacientes (codp INTEGER PRIMARY KEY, CPF CHAR(11) UNIQUE, nome VARCHAR(40), idade INTEGER, cidade VARCHAR(30),
                        doenca VARCHAR(40));
CREATE TABLE Consultas (codm INTEGER REFERENCES Medicos (codm), codp INTEGER REFERENCES Pacientes (codp), data DATE,
                        hora TIME, PRIMARY KEY (codm, data, hora));
CREATE TABLE Funcionarios (codf INTEGER PRIMARY KEY, CPF CHAR(11) UNIQUE, nome VARCHAR(40), idade INTEGER,
                           cidade VARCHAR(30), salario NUMERIC(10,2));
INSERT INTO Ambulatorios VALUES (1, 1, 30), (2, 2, 60), (3, 3, 50), (4, 4, 50), (5, 4, 8), (6, 3, 70), (12, 4, 30), (100, 2, 40);
INSERT INTO Medicos VALUES (46, '101', 'João', 40, 'Maceió', 'ortopedia', 1), (79, '102', 'Pedro', 60, 'Recife', 'ortopedia', 2),
    (13, '103', 'Maria', 58, 'Maceió', 'pediatria', 3), (22, '104', 'Ana', 56, 'Arapiraca', 'ortopedia', NULL);
INSERT INTO Pacientes VALUES (122, '201', 'Paulo', 30, 'Maceió', 'sarampo'), (725, '202', 'Lia', 8, 'Recife', 'gripe'),
    (300, '203', 'Rui', 45, 'Maceió', 'sarampo'), (410, '204', 'Bia', 20, 'Penedo', 'tendinite');
INSERT INTO Consultas VALUES (46, 122, '2024-06-10', '08:00'), (79, 725, '2024-06-10', '09:00'), (13, 300, '2024-06-11', '10:00'),
    (46, 725, '2024-06-12', '08:00'), (22, 410, '2024-06-11', '14:00'), (79, 122, '2024-06-13', '15:00');
INSERT INTO Funcionarios VALUES (1, '1001', 'Rita', 35, 'Maceió', 3000), (2, '1002', 'Caio', 28, 'Recife', 2500),
    (3, '1003', 'Lúcio', 50, 'Maceió', 4200), (4, '1004', 'Nina', 41, 'Penedo', 3000);
