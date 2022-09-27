CREATE DATABASE RestauranteLunary;

USE RestauranteLunary;

/* REGISTRO DE USUARIO */


CREATE TABLE RedeRestaurantes (
	Id int identity(1,1) primary key,
	Endereco varchar(450) Not null,
	Numero int Not null,
	Cidade varchar(120) Not null,
	Estado varchar(45) Not null,
	CEP varchar(9) check(len(CEP) = 9) Not null,
	)
INSERT INTO RedeRestaurantes(Endereco, Numero, Cidade, Estado, CEP)
	VALUES ('Praça Barão Rio Branco', '141', 'Estância', 'Sergipe', '49200-000'),
		   ('Praça Cajuzinho123', '825', 'Aracaju', 'Sergipe', '49400-000');

--SELECT * FROM RedeRestaurantes;
--DROP TABLE RedeRestaurantes;

CREATE TABLE Funcionario (
	IdFuncionario int identity(1,1) unique,
	CodFuncionario varchar(25) primary key,
	)
INSERT INTO Funcionario(CodFuncionario)
	VALUES ('a001');
	 
--SELECT * FROM Funcionario;
--DROP TABLE Funcionario;

CREATE TABLE Funcionarios (
	IdRestaurante int foreign key references RedeRestaurantes(Id) Not null,
	CodFuncionario varchar(25) foreign key references Funcionario(CodFuncionario) Not null,
	)
INSERT INTO Funcionarios(IdRestaurante, CodFuncionario)
	SELECT Id, CodFuncionario
		FROM RedeRestaurantes, Funcionario

--SELECT * FROM Funcionarios;
--DROP TABLE Funcionarios;

CREATE TABLE UsuarioLunary (
	Id int identity(1,1) primary key,
	Usuario varchar(45) unique Not null,
	Senha varchar(45) check(len(Senha) >= 8) Not null,
	IdRestaurante int foreign key references RedeRestaurantes(Id) Not null,
	CodFuncionario varchar(25) foreign key references Funcionario(CodFuncionario) Not null,
	)
INSERT INTO UsuarioLunary(Usuario, Senha, IdRestaurante, CodFuncionario)
	VALUES ('Filaupe', '12345678', 1, 'a001'),
		   ('Pedro', '12345678', 2, 'a001');

--SELECT * FROM UsuarioLunary;
--DROP TABLE UsuarioLunary;

CREATE TABLE SessaoDoDispositivo (
	CodSessao varchar(36) primary key,
	Autenticado int default 0,
	)
DELETE SessaoDoDispositivo

--SELECT * FROM SessaoDoDispositivo;
--DROP TABLE SessaoDoDispositivo;

/* CARDAPIO */

CREATE TABLE Cardapio (
	Id int identity(1,1) primary key,
	Nome varchar(120) Not null,
	Descricao varchar(max) Not null,
	Preco numeric(18,2) Not null,
	Imagem varbinary(max) null,
	Promocional int check(Promocional = 0
						  or
						  Promocional = 1) default 0 Not null,
	Categoria varchar(16) check(Categoria = 'Aperitivo'
								or 
								Categoria = 'Entrada' 
								or 
								Categoria = 'Prato Principal' 
								or 
								Categoria = 'Sobremesa'
								or
								Categoria = 'Bebida') Not null,
	VezesConsumo int default 0 Not null,
	)

INSERT INTO Cardapio (Nome, Descricao, Preco, Categoria, VezesConsumo)
	VALUES ('Coca-Cola', 'Refrigerante', 6.50, 'Bebida', 5),
		   ('Azeitonas Recheadas', '', 12, 'Aperitivo', 8),
		   ('Coquetel de camarão', 'Coquetel de camarão com molho de iogurte picante', 42.20, 'Entrada', 4),
		   ('Camarão na champagne com arroz de maçã', 'Camarão ao molho a base de alho, cebola, creme de leite, caldo de peixe e champagne. Vem acompanhado de arroz de maçã.', 150.70, 'Prato Principal', 3),
		   ('Frozen Yogurt', 'Iogurte natural quase congelado', 10, 'Sobremesa', 7);

--SELECT * FROM Cardapio;
--SELECT * FROM Cardapio WHERE Categoria = 'Bebida'
--UPDATE Cardapio SET Imagem = NULL WHERE Id = 1;
--UPDATE Cardapio SET Promocional = 1 WHERE Id = 2;
--SELECT * FROM Cardapio ORDER BY VezesConsumo DESC;
--DROP TABLE Cardapio; 