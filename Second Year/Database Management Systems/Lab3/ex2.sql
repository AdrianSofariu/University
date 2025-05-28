CREATE OR ALTER PROCEDURE InsertPartialPick
    @playerName NVARCHAR(100),
    @realName NVARCHAR(100),
    @position NVARCHAR(50),
    @teamId INT,
    @regionId INT,
    @birthDate DATE,
    @championName NVARCHAR(100),
    @championRole NVARCHAR(50),
    @wins INT,
    @losses INT
AS
BEGIN

    DECLARE @playerId INT;
    DECLARE @championId INT;

    -- Insert Player
    BEGIN TRY
        IF NOT EXISTS (SELECT 1 FROM Players WHERE playerName = @playerName)
        BEGIN
            INSERT INTO Players(playerName, realName, position, teamId, regionId, birthDate)
            VALUES (@playerName, @realName, @position, @teamId, @regionId, @birthDate);
        END

        SET @playerId = (SELECT playerId FROM Players WHERE playerName = @playerName);

        INSERT INTO ActionLog(ActionDescription, Success)
        VALUES ('PartialPick: Player inserted or already exists.', 1);
    END TRY
    BEGIN CATCH
        INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
        VALUES ('PartialPick: Failed to insert player.', 0, ERROR_MESSAGE());
    END CATCH

    -- Insert Champion
    BEGIN TRY
        IF NOT EXISTS (SELECT 1 FROM Champions WHERE championName = @championName)
        BEGIN
            INSERT INTO Champions(championName, championRole)
            VALUES (@championName, @championRole);
        END

        SET @championId = (SELECT championId FROM Champions WHERE championName = @championName);

        INSERT INTO ActionLog(ActionDescription, Success)
        VALUES ('PartialPick: Champion inserted or already exists.', 1);
    END TRY
    BEGIN CATCH
        INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
        VALUES ('PartialPick: Failed to insert champion.', 0, ERROR_MESSAGE());
    END CATCH

    -- Insert Pick
    BEGIN TRY
        SET @playerId = (SELECT playerId FROM Players WHERE playerName = @playerName);
        SET @championId = (SELECT championId FROM Champions WHERE championName = @championName);

        INSERT INTO Picks(playerId, championId, wins, losses)
        VALUES (@playerId, @championId, @wins, @losses);

        INSERT INTO ActionLog(ActionDescription, Success)
        VALUES ('PartialPick: Pick inserted.', 1);
    END TRY
    BEGIN CATCH
        INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
        VALUES ('PartialPick: Failed to insert pick.', 0, ERROR_MESSAGE());
    END CATCH
END

CREATE OR ALTER PROCEDURE InsertPartialPick
    @playerName NVARCHAR(100),
    @realName NVARCHAR(100),
    @position NVARCHAR(50),
    @teamId INT,
    @regionId INT,
    @birthDate DATE,
    @championName NVARCHAR(100),
    @championRole NVARCHAR(50),
    @wins INT,
    @losses INT
AS
BEGIN
    DECLARE @playerId INT;
    DECLARE @championId INT;

    BEGIN TRANSACTION;  -- Start the overall transaction

    -- Insert Player
    BEGIN
        SAVE TRANSACTION SavePointPlayer;  -- Set savepoint for player insertion

        BEGIN TRY
            IF NOT EXISTS (SELECT 1 FROM Players WHERE playerName = @playerName)
            BEGIN
                INSERT INTO Players(playerName, realName, position, teamId, regionId, birthDate)
                VALUES (@playerName, @realName, @position, @teamId, @regionId, @birthDate);
            END

            SET @playerId = (SELECT playerId FROM Players WHERE playerName = @playerName);

            INSERT INTO ActionLog(ActionDescription, Success)
            VALUES ('PartialPick: Player inserted or already exists.', 1);
        END TRY
        BEGIN CATCH
            ROLLBACK TRANSACTION SavePointPlayer;  -- Rollback to savepoint on error
            INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
            VALUES ('PartialPick: Failed to insert player.', 0, ERROR_MESSAGE());
        END CATCH
    END

    -- Insert Champion
    BEGIN
        SAVE TRANSACTION SavePointChampion;  -- Set savepoint for champion insertion

        BEGIN TRY
            IF NOT EXISTS (SELECT 1 FROM Champions WHERE championName = @championName)
            BEGIN
                INSERT INTO Champions(championName, championRole)
                VALUES (@championName, @championRole);
            END

            SET @championId = (SELECT championId FROM Champions WHERE championName = @championName);

            INSERT INTO ActionLog(ActionDescription, Success)
            VALUES ('PartialPick: Champion inserted or already exists.', 1);
        END TRY
        BEGIN CATCH
            ROLLBACK TRANSACTION SavePointChampion;  -- Rollback to savepoint on error
            INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
            VALUES ('PartialPick: Failed to insert champion.', 0, ERROR_MESSAGE());
        END CATCH
    END

    -- Insert Pick
    BEGIN
        SAVE TRANSACTION SavePointPick;  -- Set savepoint for pick insertion

        BEGIN TRY
            SET @playerId = (SELECT playerId FROM Players WHERE playerName = @playerName);
            SET @championId = (SELECT championId FROM Champions WHERE championName = @championName);

            INSERT INTO Picks(playerId, championId, wins, losses)
            VALUES (@playerId, @championId, @wins, @losses);

            INSERT INTO ActionLog(ActionDescription, Success)
            VALUES ('PartialPick: Pick inserted.', 1);
        END TRY
        BEGIN CATCH
            ROLLBACK TRANSACTION SavePointPick;  -- Rollback to savepoint on error
            INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
            VALUES ('PartialPick: Failed to insert pick.', 0, ERROR_MESSAGE());
        END CATCH
    END

    COMMIT TRANSACTION;  -- Commit the overall transaction if everything was successful
END



EXEC InsertPartialPick
    @playerName = 'Faker',
    @realName = 'Lee Sang-hyeok',
    @position = 'Mid',
    @teamId = 1,
    @regionId = 1,
    @birthDate = '1996-05-07',
    @championName = 'Galio',
    @championRole = 'Tank',
    @wins = -50,
    @losses = 10;