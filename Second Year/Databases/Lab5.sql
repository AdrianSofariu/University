CREATE TABLE Processors(
    ProcessorID INT PRIMARY KEY,
    SerialNumber INT UNIQUE,
    Manufacturer VARCHAR(100),
    Model VARCHAR(100),
    Architecture VARCHAR(100)
)

DROP TABLE GraphicsCards

CREATE TABLE GraphicsCards(
    GraphicsCardID INT PRIMARY KEY,
    MemorySize INT
    Manufacturer VARCHAR(100),
    Model VARCHAR(100),
)

CREATE TABLE Computers(
    ComputerID INT PRIMARY KEY,
    ProcessorID INT FOREIGN KEY REFERENCES Processors(ProcessorID),
    GraphicsCardID INT FOREIGN KEY REFERENCES GraphicsCards(GraphicsCardID),
    Price DECIMAL(10,2)
)

--  insert data into the Processors table
INSERT INTO Processors VALUES (1, 123456, 'Intel', 'i7-9700K', 'x86_64')
INSERT INTO Processors VALUES (2, 654321, 'AMD', 'Ryzen 7 7800X3D', 'x86_64')
INSERT INTO Processors VALUES (3, 987654, 'Intel', 'i9-14900K', 'x86_64')
INSERT INTO Processors VALUES (4, 456789, 'AMD', 'Ryzen 9 9900', 'x86_64')
INSERT INTO Processors VALUES (5, 987754, 'Snapdragon', 'Snapdragon X Elite', 'ARM')
INSERT INTO Processors VALUES (6, 917754, 'Apple', 'M1 Pro', 'ARM')
INSERT INTO Processors VALUES (7, 913754, 'Apple', 'M1 Max', 'ARM')


--  insert data into the GraphicsCards table
INSERT INTO GraphicsCards VALUES (1, 8, 'Nvidia', 'RTX 3080')
INSERT INTO GraphicsCards VALUES (2, 16, 'Nvidia', 'RTX 3090')
INSERT INTO GraphicsCards VALUES (3, 4, 'AMD', 'RX 6700 XT')
INSERT INTO GraphicsCards VALUES (4, 8, 'AMD', 'RX 6800 XT')
INSERT INTO GraphicsCards VALUES (5, 6, 'Intel', 'Iris Xe Max')
INSERT INTO GraphicsCards VALUES (6, 8, 'Nvidia', 'RTX 3060')
INSERT INTO GraphicsCards VALUES (7, 8, 'Nvidia', 'RTX 3070')
INSERT INTO GraphicsCards VALUES (8, 8, 'Nvidia', 'RTX 3060 Ti')
INSERT INTO GraphicsCards VALUES (9, 8, 'Nvidia', 'RTX 3070 Ti')
INSERT INTO GraphicsCards VALUES (10, 8, 'Nvidia', 'RTX 3080 Ti')
INSERT INTO GraphicsCards VALUES (11, 8, 'Nvidia', 'RTX 3090 Ti')
INSERT INTO GraphicsCards VALUES (12, 8, 'Nvidia', 'RTX 3080 Super')
INSERT INTO GraphicsCards VALUES (13, 16, 'Nvidia', 'RTX 3090 Super')
INSERT INTO GraphicsCards VALUES (14, 16, 'Nvidia', 'RTX 4080 Super')
INSERT INTO GraphicsCards VALUES (15, 16, 'Nvidia', 'RTX 4090')

-- insert data into the Computers table
INSERT INTO Computers VALUES (1, 1, 1, 2000.00)
INSERT INTO Computers VALUES (2, 2, 2, 3000.00)
INSERT INTO Computers VALUES (3, 3, 3, 2500.00)
INSERT INTO Computers VALUES (4, 4, 4, 3500.00)
INSERT INTO Computers VALUES (5, 5, 5, 1500.00)
INSERT INTO Computers VALUES (6, 3, 2, 4000.00)
INSERT INTO Computers VALUES (7, 4, 3, 5000.00)
INSERT INTO Computers VALUES (8, 5, 4, 4500.00)
INSERT INTO Computers VALUES (9, 6, 5, 5500.00)
INSERT INTO Computers VALUES (10, 7, 6, 3500.00)
INSERT INTO Computers VALUES (11, 6, 7, 6000.00)
INSERT INTO Computers VALUES (12, 7, 8, 7000.00)
INSERT INTO Computers VALUES (13, 1, 9, 6500.00)
INSERT INTO Computers VALUES (14, 2, 10, 7500.00)
INSERT INTO Computers VALUES (15, 1, 11, 5500.00)
INSERT INTO Computers VALUES (16, 1, 12, 8000.00)
INSERT INTO Computers VALUES (17, 2, 13, 9000.00)
INSERT INTO Computers VALUES (18, 3, 14, 8500.00)
INSERT INTO Computers VALUES (19, 4, 15, 9500.00)
INSERT INTO Computers VALUES (20, 7, 1, 7500.00)

/*
a. Write queries on Processors such that their execution plans contain the following operators:
    clustered index scan;
    clustered index seek;
    nonclustered index scan;
    nonclustered index seek;
    key lookup.
*/

--clustered index scan
SELECT * FROM Processors

--clustered index seek
SELECT * FROM Processors WHERE ProcessorID > 2

--create a nonclustered index on the Manufacturer column
CREATE NONCLUSTERED INDEX IX_Manufacturer ON Processors(Manufacturer) INCLUDE(Model)

--nonclustered index scan
SELECT Manufacturer, Model FROM Processors

--nonclustered index seek 
SELECT Manufacturer, Model FROM Processors WHERE Manufacturer <> 'Intel'

-- key lookup
SELECT Manufacturer, Model FROM Processors WHERE SerialNumber = 987754


/*
b. Write a query on table Tb with a WHERE clause of the form WHERE b2 = value and analyze its execution plan.
 Create a nonclustered index that can speed up the query. Examine the execution plan again.
*/
SELECT MemorySize, Model
FROM GraphicsCards
WHERE MemorySize = 8

CREATE NONCLUSTERED INDEX IX_MemorySize ON GraphicsCards(MemorySize) INCLUDE(Model)


/*
c. Create a view that joins at least 2 tables.
Check whether existing indexes are helpful; if not, reassess existing indexes / examine the cardinality of the tables.
*/

CREATE OR ALTER VIEW ComputerDetails
AS
SELECT P.Manufacturer as PMan, P.Model as PModel, C.Price
FROM Computers C
JOIN Processors P ON C.ProcessorID = P.ProcessorID
WHERE P.Manufacturer in ('Intel', 'AMD') AND C.Price < 7000

SELECT * FROM ComputerDetails


DROP INDEX IX_ProcessorID ON Computers
CREATE NONCLUSTERED INDEX IX_ProcessorID ON Computers(ProcessorID) INCLUDE (Price)




