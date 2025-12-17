# DROP DATABASE IF EXISTS disney;

# CREATE DATABASE IF NOT EXISTS disney;

# USE disney;

# CREATE TABLE filmes_disney (
#     id INT PRIMARY KEY ,
#     titulo VARCHAR(255),
#     diretor VARCHAR(255),
#     ano INT,
#     tamanho_minutos INT
# );

# CREATE TABLE bilheteria (
#     filme_id INT NOT NULL,
#     rating DECIMAL(2,1),
#     vendas_nacionais DECIMAL(15, 2),
#     vendas_internacionais DECIMAL(15, 2),
#     FOREIGN KEY (filme_id) REFERENCES filmes_disney(id)
# );




# INSERT INTO filmes_disney (id, titulo, diretor, ano, tamanho_minutos) VALUES
# (1, 'O Rei Leão', 'Roger Allers', 1994, 88),
# (2, 'A Pequena Sereia', 'Ron Clements', 1989, 83),
# (3, 'Aladdin', 'Ron Clements', 1992, 90),
# (4, 'Mulan', 'Tony Bancroft', 1998, 88),
# (5, 'Tarzan', 'Kevin Lima', 1999, 88),
# (6, 'Pocahontas', 'Mike Gabriel', 1995, 81),
# (7, 'Branca de Neve e os Sete Anões', 'David Hand', 1937, 83),
# (8, 'A Bela e a Fera', 'Gary Trousdale', 1991, 84),
# (9, 'Hércules', 'Ron Clements', 1997, 93),
# (10, 'Ratatouille', 'Brad Bird', 2007, 111),
# (11, 'Up: Altas Aventuras', 'Pete Docter', 2009, 96),
# (12, 'Frozen: Uma Aventura Congelante', 'Chris Buck', 2013, 102),
# (13, 'Moana', 'Ron Clements', 2016, 107),
# (14, 'Divertida Mente', 'Pete Docter', 2015, 95),
# (15, 'Zootopia', 'Byron Howard', 2016, 108),
# (16, 'A Princesa e o Sapo', 'Ron Clements', 2009, 97),
# (17, 'Luca', 'Enrico Casarosa', 2021, 95),
# (18, 'Encanto', 'Jared Bush', 2021, 102),
# (19, 'Os Incríveis', 'Brad Bird', 2004, 115),
# (20, 'Cinderela', 'Clyde Geronimi', 1950, 74),
# (21, 'A Dama e o Vagabundo', 'Clyde Geronimi', 1955, 76),
# (22, 'Peter Pan', 'Clyde Geronimi', 1953, 77),
# (23, 'Alice no País das Maravilhas', 'Clyde Geronimi', 1951, 75),
# (24, 'O Livro da Selva', 'Wolfgang Reitherman', 1967, 78),
# (25, 'Os Aristogatas', 'Wolfgang Reitherman', 1970, 78),
# (26, 'O Corcunda de Notre Dame', 'Gary Trousdale', 1996, 91),
# (27, 'A Nova Onda do Imperador', 'Mark Dindal', 2000, 78),
# (28, 'Bolt: Supercão', 'Byron Howard', 2008, 96),
# (29, 'Winnie the Pooh', 'Don Hall', 2011, 63),
# (30, 'Ariel e o Mistério do Mar', 'Lynn Roth', 2000, 83),
# (31, 'Detona Ralph', 'Rich Moore', 2012, 101),
# (32, 'Os Muppets', 'James Bobin', 2011, 103),
# (33, 'Descendentes', 'Kenny Ortega', 2015, 111),
# (34, 'A Tartaruga Vermelha', 'Michael Dudok de Wit', 2016, 80),
# (35, 'O Estranho Mundo de Jack', 'Henry Selick', 1993, 76),
# (36, 'A Era do Gelo', 'Chris Wedge', 2002, 81),
# (37, 'Raya e o Último Dragão', 'Don Hall', 2021, 107),
# (38, 'O Príncipe do Egito', 'Brenda Chapman', 1998, 100),
# (39, 'Coco', 'Lee Unkrich', 2017, 105),
# (40, 'A Casa do Lago', 'Randy Moore', 2006, 102),
# (41, 'A Menina e o Porquinho', 'Gary Winick', 2006, 96),
# (42, 'A Festa da Salsicha', 'Greg Tiernan', 2016, 89),
# (43, 'A Chapeuzinho Vermelho', 'David Stoten', 2005, 75),
# (44, 'Valente', 'Brenda Chapman', 2012, 93),
# (45, 'Atlantis: O Reino Perdido', 'Gary Trousdale', 2001, 97),
# (46, 'O Fantasma da Ópera', 'Joel Schumacher', 2004, 143),
# (47, 'Peter Rabbit', 'Will Gluck', 2018, 95),
# (48, 'A Fera e a Fera', 'David Hand', 1994, 84),
# (49, 'O Mundo dos Pequeninos', 'Hiromasa Yonebayashi', 2010, 97),
# (50, 'O Rei Leão 2: O Caminho de Simba', 'Darrell Rooney', 1998, 80),
# (200, 'MUFASA', 'Darrell Rooney', 2025, 160);

# INSERT INTO bilheteria (filme_id, rating, vendas_nacionais, vendas_internacionais) VALUES
# (1, 8.5, 543000000.00, 950000000.00),
# (2, 7.8, 211000000.00, 300000000.00),
# (3, 8.7, 504000000.00, 600000000.00),
# (4, 7.5, 204000000.00, 250000000.00),
# (5, 8.1, 171000000.00, 250000000.00),
# (6, 7.2, 142000000.00, 200000000.00),
# (7, 8.0, 184000000.00, 150000000.00),
# (8, 8.3, 145000000.00, 380000000.00),
# (9, 7.6, 252000000.00, 120000000.00),
# (10, 7.9, 206000000.00, 250000000.00),
# (11, 8.8, 731000000.00, 450000000.00),
# (12, 8.0, 400000000.00, 600000000.00),
# (13, 9.0, 688000000.00, 1000000000.00),
# (14, 7.4, 470000000.00, 400000000.00),
# (15, 7.9, 371000000.00, 380000000.00),
# (16, 7.5, 113000000.00, 190000000.00),
# (17, 8.2, 250000000.00, 300000000.00),
# (18, 8.0, 146000000.00, 220000000.00),
# (19, 7.9, 240000000.00, 150000000.00),
# (20, 8.1, 159000000.00, 180000000.00),
# (21, 8.9, 530000000.00, 700000000.00),
# (22, 7.6, 120000000.00, 210000000.00),
# (23, 8.5, 207000000.00, 250000000.00),
# (24, 6.8, 50000000.00, 80000000.00),
# (25, 7.7, 160000000.00, 290000000.00),
# (26, 7.4, 100000000.00, 150000000.00),
# (27, 8.1, 295000000.00, 200000000.00),
# (28, 8.0, 240000000.00, 300000000.00),
# (29, 7.5, 197000000.00, 450000000.00),
# (30, 8.3, 300000000.00, 500000000.00),
# (31, 8.0, 460000000.00, 320000000.00),
# (32, 7.9, 185000000.00, 140000000.00),
# (33, 7.6, 120000000.00, 200000000.00),
# (34, 8.4, 460000000.00, 380000000.00),
# (35, 7.5, 204000000.00, 220000000.00),
# (36, 7.3, 89000000.00, 50000000.00),
# (37, 7.8, 140000000.00, 180000000.00),
# (38, 8.0, 220000000.00, 170000000.00),
# (39, 8.2, 360000000.00, 420000000.00),
# (40, 7.5, 150000000.00, 100000000.00),
# (41, 8.1, 380000000.00, 250000000.00),
# (42, 8.7, 520000000.00, 700000000.00),
# (43, 7.0, 110000000.00, 190000000.00),
# (44, 7.4, 155000000.00, 120000000.00),
# (45, 8.1, 190000000.00, 300000000.00),
# (46, 7.2, 72000000.00, 80000000.00),
# (47, 8.3, 150000000.00, 250000000.00),
# (48, 6.9, 60000000.00, 50000000.00),
# (49, 7.8, 180000000.00, 220000000.00),
# (50, 7.5, 120000000.00, 180000000.00);



# SELECT titulo,id FROM filmes_disney;

# SELECT titulo,diretor FROM filmes_disney;

# SELECT titulo,tamanho_minutos FROM filmes_disney;

# SELECT titulo,id,ano,diretor,tamanho_minutos FROM filmes_disney;

# SELECT * FROM filmes_disney WHERE tamanho_minutos < 75;

# SELECT * FROM  filmes_disney WHERE id = 6 ;

# SELECT COUNT(*) FROM filmes_disney WHERE ano > 2000 AND ano < 2010;

# SELECT * FROM filmes_disney WHERE NOT ano > 2000 AND ano < 2010;

# SELECT * FROM filmes_disney ORDER BY ano LIMIT 1;

# SELECT * FROM filmes_disney ORDER BY ano LIMIT 5;

# SELECT * FROM filmes_disney  WHERE ano > 2000 AND ano < 2010 ORDER BY titulo;

# SELECT * FROM bilheteria ORDER BY rating LIMIT 1;

# SELECT
#     *
# FROM
#     filmes_disney
# INNER JOIN
# 	bilheteria
# ON
#     filmes_disney.id = bilheteria.filme_id;