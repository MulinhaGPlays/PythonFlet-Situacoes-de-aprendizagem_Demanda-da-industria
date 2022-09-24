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
	Imagem varchar(max) default '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' Not null,
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
--UPDATE Cardapio SET VezesConsumo = 7 WHERE Id = 5;
--UPDATE Cardapio SET Promocional = 1 WHERE Id = 2;
--SELECT * FROM Cardapio ORDER BY VezesConsumo DESC;
--DROP TABLE Cardapio; 