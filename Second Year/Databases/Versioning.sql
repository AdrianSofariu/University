-- CREATE Versions table
CREATE TABLE CurrentVersion(
    versionId INT PRIMARY KEY
)

-- CREATE VersionChanges table that links verions which procedures to execute
CREATE TABLE VersionChanges(
    versionId INT,
    procedureName VARCHAR(100),
    FOREIGN KEY (versionId) REFERENCES Versions(versionId),
)

-- CREATE Procedure to update to a version
CREATE OR ALTER PROCEDURE sp_UpdateToVersion
    @targetVersion INT
AS
BEGIN
    DECLARE @procedureName VARCHAR(100)
    DECLARE @currentVersion INT

    SELECT @currentVersion = versionId FROM CurrentVersion

    DECLARE versionProcedures CURSOR FOR
        SELECT procedureName
        FROM VersionChanges
        WHERE versionId = @targetVersion

    OPEN versionProcedures
    FETCH NEXT FROM versionProcedures INTO @procedureName

    WHILE @@FETCH_STATUS = 0
    BEGIN
        BEGIN TRY
            EXEC @procedureName
        END TRY
        BEGIN CATCH
            PRINT 'Error executing ' + @procedureName
        END CATCH

        FETCH NEXT FROM versionProcedures INTO @procedureName
    END

    CLOSE versionProcedures
    DEALLOCATE versionProcedures

    -- update current version
    UPDATE CurrentVersion
    SET versionId = @targetVersion
    WHERE versionId = @currentVersion
END


-- Add Versions
INSERT INTO Versions VALUES ('Default')
INSERT INTO Versions VALUES ('Money Instead Of Decimal')
INSERT INTO Versions VALUES('Player Age')
INSERT INTO Versions VALUES('Ability Table')

-- Add Version Changes
INSERT INTO VersionChanges VALUES (2, 'sp_ChangeSponsorshipMonetaryValueToMoney')
INSERT INTO VersionChanges VALUES (2, 'sp_RemoveBirthDateFromPlayers')
INSERT INTO VersionChanges VALUES (2, 'sp_RemoveAblilitiesTable')

INSERT INTO VersionChanges VALUES (3, 'sp_ChangeSponsorshipMonetaryValueToMoney')
INSERT INTO VersionChanges VALUES (3, 'sp_AddBirthDateToPlayers')
INSERT INTO VersionChanges VALUES (3, 'sp_RemoveAblilitiesTable')


INSERT INTO VersionChanges VALUES (1, 'sp_ChangeSponsorshipMonetaryValueToDecimal')
INSERT INTO VersionChanges VALUES (1, 'sp_RemoveBirthDateFromPlayers')
INSERT INTO VersionChanges VALUES (1, 'sp_RemoveAblilitiesTable')

INSERT INTO VersionChanges VALUES (4, 'sp_ChangeSponsorshipMonetaryValueToMoney')
INSERT INTO VersionChanges VALUES (4, 'sp_AddBirthDateToPlayers')
INSERT INTO VersionChanges VALUES(4, 'sp_CreateAbilitiesTable')

