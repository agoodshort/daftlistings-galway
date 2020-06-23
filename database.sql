CREATE DATABASE daftlistings;

USE daftlistings;

CREATE TABLE Galway (
	date DATE,
	area VARCHAR(255),
	beds INT,
	location VARCHAR(255),
	url VARCHAR(510),
	price DECIMAL(10,2));

CREATE TABLE GalwayAreas (
	areaID INT NOT NULL AUTO_INCREMENT,
	areaName VARCHAR(255),
	Primary Key (areaID));

INSERT INTO GalwayAreas(areaName) VALUES
	('Galway City Centre'),
	('Galway City Suburbs'),
	('Galway Commuter Towns');

CREATE OR REPLACE VIEW GalwayReview AS 
	SELECT Galway.date,
	Galway.area,
	COUNT(GalwayAreas.areaID) as housesListedThisDay,
	AVG(Galway.price) as averagePrice
	FROM Galway 
	LEFT JOIN GalwayAreas ON Galway.area = GalwayAreas.areaName 
	GROUP BY Galway.date,Galway.area;
