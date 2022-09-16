CREATE DATABASE RestauranteLunary;

CREATE TABLE UsuarioLunary (
	id int identity(1,1) primary key,
	Usuario varchar(45) unique Not null,
	Senha varchar(45) check(len(Senha) >= 9) Not null,
)
INSERT INTO UsuarioLunary(Usuario, Senha)
VALUES ('LunaryRestaurant', '123456789abc');

/*SELECT * FROM UsuarioLunary;*/
/*DROP TABLE UsuarioLunary;*/
