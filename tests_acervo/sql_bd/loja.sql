-- Dados da equipe TutorON no lugar do banco Northwind dos slides de BD2 (mesmas consultas, tabelas menores).
CREATE TABLE cliente (id_cliente INTEGER PRIMARY KEY, nome VARCHAR(40) NOT NULL, cidade VARCHAR(30), pais VARCHAR(30) NOT NULL);
CREATE TABLE fornecedor (id_fornecedor INTEGER PRIMARY KEY, nome VARCHAR(40) NOT NULL, cidade VARCHAR(30), pais VARCHAR(30) NOT NULL);
CREATE TABLE produto (id_produto INTEGER PRIMARY KEY, nome VARCHAR(40) NOT NULL,
                      id_fornecedor INTEGER NOT NULL REFERENCES fornecedor (id_fornecedor), preco NUMERIC(10,2) NOT NULL);
CREATE TABLE vendedor (id_vendedor INTEGER PRIMARY KEY, sobrenome VARCHAR(40) NOT NULL);
CREATE TABLE pedido (id_pedido INTEGER PRIMARY KEY, id_cliente INTEGER NOT NULL REFERENCES cliente (id_cliente),
                     id_vendedor INTEGER NOT NULL REFERENCES vendedor (id_vendedor), data DATE NOT NULL);
CREATE TABLE item_pedido (id_pedido INTEGER NOT NULL REFERENCES pedido (id_pedido),
                          id_produto INTEGER NOT NULL REFERENCES produto (id_produto),
                          quantidade INTEGER NOT NULL, PRIMARY KEY (id_pedido, id_produto));
INSERT INTO cliente VALUES (1, 'Ana Lima', 'Maceió', 'Brasil'), (2, 'Bruno Costa', 'Recife', 'Brasil'),
    (3, 'Carla Dias', 'Porto', 'Portugal'), (4, 'Davi Melo', 'Maceió', 'Brasil'), (5, 'Elisa Nunes', 'Lisboa', 'Portugal'),
    (6, 'Fábio Rocha', NULL, 'Brasil'), (7, 'Gil Souza', 'Recife', 'Brasil'), (8, 'Hana Ito', 'Osaka', 'Japão');
INSERT INTO fornecedor VALUES (1, 'Papelaria Sul', 'Recife', 'Brasil'), (2, 'Gráfica Norte', 'Porto', 'Portugal'),
    (3, 'Tintas Leste', 'Maceió', 'Brasil'),
    (4, 'Livraria Oeste', 'Natal', 'Brasil');
INSERT INTO produto VALUES (1, 'Caderno', 1, 18), (2, 'Caneta', 1, 3), (3, 'Cartaz', 2, 22), (4, 'Tinta azul', 3, 35),
    (5, 'Pincel', 3, 12);
INSERT INTO vendedor VALUES (1, 'Ramos'), (2, 'Freitas'), (3, 'Ramos');
INSERT INTO pedido VALUES (101, 1, 1, '2024-03-01'), (102, 2, 1, '2024-03-02'), (103, 4, 2, '2024-03-02'),
    (104, 3, 1, '2024-03-05'), (105, 1, 2, '2024-03-06'), (106, 5, 3, '2024-03-07');
INSERT INTO item_pedido VALUES (101, 1, 10), (101, 2, 5), (102, 2, 10), (103, 4, 2), (104, 3, 30), (105, 1, 40), (106, 5, 10);
