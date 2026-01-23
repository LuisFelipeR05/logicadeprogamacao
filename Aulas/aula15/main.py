-- PARA CRIAR UMA NOVA BASE DE DADOS DDL DATA DEFINITION LANGUAGE
CREATE DATABASE escola;
-- PARA SELECIONAR A BASE PARA MANIPULAÇÃO UTILIZAMOS
USE escola;

-- faça uma tabela para representar aluno
-- que contenha as caracteristicas 
-- id(chave primária), 
-- nome (obrigatório), 
-- cpf(obrigatório e único), 
-- email(único), 
-- ra,
 

-- DDL 
CREATE TABLE aluno(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL ,
    email VARCHAR(255) UNIQUE
);
-- DML data manipulation language
INSERT INTO aluno (nome,cpf) VALUES
("ANDREIA","12345678910"),
("Gabriel","12345678911"),
("Jéssica","12345678912"),
("Felipe","12345678913"),
("Bernardo","12345678914");

UPDATE aluno 
SET nome = "Gabriel"
WHERE id = 1;

DELETE FROM aluno
WHERE id = 1;


-- DQL
SELECT * FROM aluno;


SELECT * FROM filmes_disney
INNER JOIN bilheteria
ON filmes_disney.id = bilheteria
==========================================================

-- PARA CRIAR UMA NOVA BASE DE DADOS DDL DATA DEFINITION LANGUAGE
CREATE DATABASE escola;

-- PARA SELECIONAR A BASE PARA MANIPULAÇÃO UTILIZAMOS
USE escola;

-- faça uma tabela para representar aluno
-- que contenha as caracteristicas 
-- id(chave primária), nome (obrigatório), cpf(obrigatório e único), email(único), ra,
 

-- 

-- PARA CRIAR UMA NOVA BASE DE DADOS DDL DATA DEFINITION LANGUAGE
CREATE DATABASE escola;
-- PARA SELECIONAR A BASE PARA MANIPULAÇÃO UTILIZAMOS
USE escola;

-- faça uma tabela para representar aluno
-- que contenha as caracteristicas 
-- id(chave primária), 
-- nome (obrigatório), 
-- cpf(obrigatório e único), 
-- email(único), 
-- ra,
 

-- DDL 
CREATE TABLE aluno(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL ,
    email VARCHAR(255) UNIQUE
);
-- DML data manipulation language
INSERT INTO aluno (nome,cpf) VALUES
("ANDREIA","12345678910"),
("Gabriel","12345678911"),
("Jéssica","12345678912"),
("Felipe","12345678913"),
("Bernardo","12345678914");

UPDATE aluno 
SET nome = "Gabriel"
WHERE id = 1;

DELETE FROM aluno
WHERE id = 1;



DQL
SELECT * FROM aluno;


import mysql.connector as mysql

db = mysql.connect(
  host="localhost",
  user="root",
  password="in12345678",
  database="escola"
) 

cursor = db.cursor()
cursor.execute("SHOW DATABASES")
resultado = cursor.fetchone()
print(resultado)

import mysql.connector as mysql

db = mysql.connect(
  host="localhost",
  user="root",
  port=3306,
  password="in12345678",
  database="escola"
) 

# cursor 
cursor = db.cursor()
nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
cursor.execute(f"INSERT INTO aluno(nome,cpf) VALUES ('{nome}','{cpf}');")
db.commit()
# cursor.execute("SELECT * FROM aluno;")
resultado = cursor.fetchall()
print(resultado)

import mysql.connector as mysql
from time import sleep
import os 
from tabulate import tabulate

db = mysql.connect(
  host="localhost",
  user="root",
  port=3306,
  password="in12345678",
  database="escola"
) 
cursor = db.cursor()


while True: 
    print("="*30)
    print("Cadastro de Alunos".center(30))
    print("1 - Para listar alunos.")
    print("2 - Para cadastrar aluno.")
    print("3 - Para atualizar aluno.")
    print("4 - Para deletar aluno.")
    print("q - Sair.")
    opcao = input("->")
    if opcao == "1":
        cursor.execute("SELECT * FROM aluno;")
        resultado = cursor.fetchall()
        print(tabulate(resultado))
    
    
    elif opcao == "2":
        nome = input("Digite seu nome: ")	
        cpf = input("Digite seu cpf: ")
        cursor.execute(f"INSERT INTO aluno(nome,cpf) VALUES('{nome}', '{cpf}')")
    
    
    elif opcao == "3":
        pass 

    
    elif opcao == "4":
        pass 


    elif opcao == "q":
        print("Finalizando")
        break


db.close()