-- Relação EMPREGADO dos slides de álgebra relacional (as três primeiras linhas; a quarta é da equipe).
CREATE TABLE EMPREGADO (
    CPF        CHAR(11) PRIMARY KEY,
    PNOME      VARCHAR(30),
    UNOME      VARCHAR(30),
    SEXO       CHAR(1),
    SALARIO    NUMERIC(10,2),
    SUPERVISOR INTEGER
);
INSERT INTO EMPREGADO VALUES
    ('11122233344', 'Maria',  'Silva',  'F', 7500, 542),
    ('22233344455', 'Josefa', 'Lemos',  'F', 8000, 668),
    ('33344455566', 'Rafael', 'Campos', 'M', 3850, 542),
    ('44455566677', 'Luana',  'Reis',   'F', 7500, 668);
