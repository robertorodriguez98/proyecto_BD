CREATE DATABASE monster_hunter;

CREATE USER 'jugador'@'%' IDENTIFIED BY 'jugador';
GRANT ALL PRIVILEGES ON monster_hunter.* TO 'jugador'@'%';
FLUSH PRIVILEGES;

USE monster_hunter;

CREATE TABLE Monstruos(
idMonstruo VARCHAR(2),
nombre VARCHAR(15),
tipo ENUM('Dragon Anciano','Bestia de Colmillos','Anfibio'),
tamano DECIMAL(6,2),
CONSTRAINT PRIMARY KEY (idMonstruo)
);

CREATE TABLE Mapas(
idMapa VARCHAR(2),
nombre VARCHAR(15),
nZonas DECIMAL(2),
bioma ENUM('Selva','Desierto','Montania'),
CONSTRAINT PRIMARY KEY (idMapa)
);

CREATE TABLE Objetos(
idObjetos VARCHAR(2),
idMapa VARCHAR(2),
monstruo VARCHAR(2),
nombre VARCHAR(15),
valor DECIMAL(4),
rareza VARCHAR(1),
conseguido DATE,
CONSTRAINT fk_mapa FOREIGN KEY (idMapa) REFERENCES Mapas(idMapa),
CONSTRAINT fk_monstruo FOREIGN KEY (monstruo) REFERENCES Monstruos(idMonstruo),
CONSTRAINT PRIMARY KEY (idObjetos)
);

INSERT INTO Monstruos
VALUES('01','Tetsucabra','Anfibio',1582.25);
INSERT INTO Monstruos
VALUES('02','Kecha Wacha','Bestia de Colmillos',1019.01);
INSERT INTO Monstruos
VALUES('03','Shagaru Magala','Dragon Anciano',2187.06);

INSERT INTO Mapas
VALUES('01','Selva Jurasica',10,'Selva');
INSERT INTO Mapas
VALUES('02','Sima Hueca',8,'Montania');
INSERT INTO Mapas
VALUES('03','Estepa otonial',7,'Desierto');

INSERT INTO Objetos
VALUES('01','02','01','Aceite de prado',200,'4','2022-2-10');
INSERT INTO Objetos
VALUES('02','01','02','Garra de kecha',1680,'6','2022-1-23');
INSERT INTO Objetos
VALUES('03','03','03','Escama pura',720,'4','2022-2-27');

commit;