CREATE OR ALTER PROCEDURE InsertFullAtomicPick
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

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Insert player if not exists
        IF NOT EXISTS (SELECT 1 FROM Players WHERE playerName = @playerName)
        BEGIN
            INSERT INTO Players(playerName, realName, position, teamId, regionId, birthDate)
            VALUES (@playerName, @realName, @position, @teamId, @regionId, @birthDate);
        END

        -- Insert champion if not exists
        IF NOT EXISTS (SELECT 1 FROM Champions WHERE championName = @championName)
        BEGIN
            INSERT INTO Champions(championName, championRole)
            VALUES (@championName, @championRole);
        END

        -- Get the IDs
        DECLARE @playerId INT = (SELECT playerId FROM Players WHERE playerName = @playerName);
        DECLARE @championId INT = (SELECT championId FROM Champions WHERE championName = @championName);

        -- Insert into Picks
        INSERT INTO Picks(playerId, championId, wins, losses)
        VALUES (@playerId, @championId, @wins, @losses);

        -- Log success
        INSERT INTO ActionLog(ActionDescription, Success)
        VALUES ('FullAtomicPick: Inserted player, champion, pick successfully.', 1);

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;

        -- Log failure
        INSERT INTO ActionLog(ActionDescription, Success, ErrorMessage)
        VALUES (
            'FullAtomicPick: Failed to insert player/champion/pick.',
            0,
            ERROR_MESSAGE()
        );
    END CATCH
END

EXEC InsertFullAtomicPick
    @playerName = 'Faker',
    @realName = 'Lee Sang-hyeok',
    @position = 'Mid',
    @teamId = 1,
    @regionId = 1,
    @birthDate = '1996-05-07',
    @championName = 'Ahri',
    @championRole = 'Mage',
    @wins = -50,
    @losses = 20;