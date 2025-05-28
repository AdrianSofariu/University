-- create a procedure that makes the type of the monetaryValue column from Decimal to Money
CREATE OR ALTER PROCEDURE sp_ChangeSponsorshipMonetaryValueToMoney
AS
BEGIN
    ALTER TABLE Sponsorships ALTER COLUMN monetaryValue MONEY
END
GO

-- reverse the change made in the previous procedure
CREATE OR ALTER PROCEDURE sp_ChangeSponsorshipMonetaryValueToDecimal
AS
BEGIN
    ALTER TABLE Sponsorships ALTER COLUMN monetaryValue DECIMAL(15,2)
END
GO


-- create a procedure that adds the column birthDate to the Players table
CREATE OR ALTER PROCEDURE sp_AddBirthDateToPlayers
AS
BEGIN
    IF NOT EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Players' AND COLUMN_NAME = 'birthDate') BEGIN
        ALTER TABLE Players ADD birthDate DATE
    END
END
GO

-- create a procedure that removes the column birthDate from the Players table
CREATE OR ALTER PROCEDURE sp_RemoveBirthDateFromPlayers
AS
BEGIN
    IF EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Players' AND COLUMN_NAME = 'birthDate') BEGIN
        ALTER TABLE Players DROP COLUMN birthDate
    END
END
GO


-- create a procedure that adds a new default value to venue capacity
CREATE OR ALTER PROCEDURE sp_AddDefaultValueToVenueCapacity
AS
BEGIN
    IF NOT EXISTS(SELECT * FROM sys.default_constraints WHERE name = 'DF_VenueCapacity') BEGIN
        ALTER TABLE Venues ADD CONSTRAINT DF_VenueCapacity DEFAULT 100 FOR capacity
    END
END
GO


-- create a procedure that removes the default value from venue capacity
CREATE OR ALTER PROCEDURE sp_RemoveDefaultValueFromVenueCapacity
AS
BEGIN
    IF EXISTS(SELECT * FROM sys.default_constraints WHERE name = 'DF_VenueCapacity') BEGIN
        ALTER TABLE Venues DROP CONSTRAINT DF_VenueCapacity
    END
END
GO

-- create a procedure that makes the championName column in the Champions a candidate key
CREATE OR ALTER PROCEDURE sp_ChampionNameCandidateKey
AS
BEGIN
    IF NOT EXISTS(SELECT * FROM sys.key_constraints WHERE name = 'CK_ChampionName') BEGIN
        ALTER TABLE Champions ADD CONSTRAINT CK_ChampionName UNIQUE(championName)
    END
END
GO

-- create a procedure that removes the candidate key from the Champions table
CREATE OR ALTER PROCEDURE sp_RemoveChampionNameCandidateKey
AS
BEGIN
    IF EXISTS(SELECT * FROM sys.key_constraints WHERE name = 'CK_ChampionName') BEGIN
        ALTER TABLE Champions DROP CONSTRAINT CK_ChampionName
    END
END
GO

-- create a procedure that creates a new table called abilites
CREATE OR ALTER PROCEDURE sp_CreateAbilitiesTable
AS
BEGIN
    IF NOT EXISTS(SELECT * FROM sys.tables WHERE name = 'Abilities') BEGIN
        CREATE TABLE Abilities(
            abilityId INT,
            abilityName VARCHAR(100),
        )
    END
END
GO

-- create a procedure that removes the abilities table
CREATE OR ALTER PROCEDURE sp_RemoveAbilitiesTable
AS
BEGIN
    IF EXISTS(SELECT * FROM sys.tables WHERE name = 'Abilities') BEGIN
        DROP TABLE Abilities
    END
END
GO

-- create a procedure that adds a primary key to the abilities table
CREATE OR ALTER PROCEDURE sp_AddPrimaryKeyToAbilities
AS
BEGIN
    IF NOT EXISTS(SELECT * FROM sys.key_constraints WHERE name = 'PK_Abilities') BEGIN
        ALTER TABLE Abilities ADD CONSTRAINT PK_Abilities PRIMARY KEY(abilityId)
    END
END
GO

-- create a procedure that removes the primary key from the abilities table
CREATE OR ALTER PROCEDURE sp_RemovePrimaryKeyFromAbilities
AS
BEGIN
    IF EXISTS(SELECT * FROM sys.key_constraints WHERE name = 'PK_Abilities') BEGIN
        ALTER TABLE Abilities DROP CONSTRAINT PK_Abilities
    END
END
GO

-- create a procedure that adds a foreign key to the abilities table
CREATE OR ALTER PROCEDURE sp_AddForeignKeyToAbilities
AS
BEGIN
    IF NOT EXISTS(SELECT * FROM sys.foreign_keys WHERE name = 'FK_Abilities_Champions') BEGIN
        ALTER TABLE Abilities ADD CONSTRAINT FK_Abilities_Champions FOREIGN KEY(abilityId) REFERENCES Champions(championId)
    END
END
GO

-- create a procedure that removes the foreign key from the abilities table
CREATE OR ALTER PROCEDURE sp_RemoveForeignKeyFromAbilities
AS
BEGIN
    IF EXISTS(SELECT * FROM sys.foreign_keys WHERE name = 'FK_Abilities_Champions') BEGIN
        ALTER TABLE Abilities DROP CONSTRAINT FK_Abilities_Champions
    END
END
GO

-- execute procedure examples


