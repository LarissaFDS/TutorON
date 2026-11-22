-- Esquema da Lista 2 de SQL da turma de Ciência da Computação, com dados inventados pela equipe (não vem do dump da turma).
CREATE TABLE Cidade (codCidade INTEGER PRIMARY KEY, descricao VARCHAR(40), uf CHAR(2));
CREATE TABLE Especialidade (codEsp INTEGER PRIMARY KEY, nome VARCHAR(30));
CREATE TABLE Ambulatorio (numeroA INTEGER PRIMARY KEY, andar INTEGER NOT NULL, capacidade INTEGER);
CREATE TABLE Medico (CRM INTEGER PRIMARY KEY, nome VARCHAR(40), idade INTEGER, codcidade INTEGER REFERENCES Cidade (codCidade),
                     especialidade INTEGER REFERENCES Especialidade (codEsp), numeroA INTEGER REFERENCES Ambulatorio (numeroA));
CREATE TABLE Paciente (RG INTEGER PRIMARY KEY, nome VARCHAR(40), idade INTEGER, codcidade INTEGER REFERENCES Cidade (codCidade));
CREATE TABLE Doenca (codDoenca INTEGER PRIMARY KEY, descricao VARCHAR(40));
CREATE TABLE Consulta (CRM INTEGER REFERENCES Medico (CRM), RG INTEGER REFERENCES Paciente (RG), data DATE, hora TIME,
                       coddoenca INTEGER REFERENCES Doenca (codDoenca), PRIMARY KEY (CRM, data, hora));
CREATE TABLE Funcionario (RG INTEGER PRIMARY KEY, nome VARCHAR(40), idade INTEGER, codcidade INTEGER REFERENCES Cidade (codCidade),
                          salario NUMERIC(10,2));
INSERT INTO Cidade VALUES (1, 'Maceió', 'AL'), (2, 'Florianópolis', 'SC'), (3, 'Recife', 'PE');
INSERT INTO Especialidade VALUES (1, 'ortopedia'), (2, 'pediatria'), (3, 'cardiologia');
INSERT INTO Ambulatorio VALUES (1, 1, 30), (4, 4, 50), (12, 4, 60), (15, 5, 40), (20, 2, 80), (7, 4, 20);
INSERT INTO Medico VALUES (46, 'Carla', 45, 1, 1, 1), (79, 'Davi', 38, 2, 1, 4), (13, 'Elisa', 52, 2, 2, 15), (30, 'Fábio', 41, 3, 3, NULL);
INSERT INTO Paciente VALUES (22, 'Gil', 30, 1), (25, 'Hana', 8, 2), (31, 'Ivo', 60, 3);
INSERT INTO Doenca VALUES (1, 'sarampo'), (2, 'pneumonia'), (3, 'gripe');
INSERT INTO Consulta VALUES (46, 22, '2024-03-01', '08:00', 1), (79, 25, '2024-03-02', '09:00', 1),
    (13, 25, '2024-03-05', '10:00', 3), (46, 31, '2024-03-06', '11:00', 2), (46, 22, '2024-03-08', '08:00', 1);
INSERT INTO Funcionario VALUES (101, 'Júlia', 29, 2, 4800), (102, 'Kauã', 35, 1, 6000);
