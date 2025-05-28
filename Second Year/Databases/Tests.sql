-- create some mock tables identical to the ones in the database for testing

-- create a copy of the teams table with no foreign key constraints
CREATE TABLE TestTeams
(
    teamId INT PRIMARY KEY,
    teamName VARCHAR(100),
    regionId INT,
    acronym VARCHAR(10),
)

-- create a copy of the sponsors table with no foreign key constraints
CREATE TABLE TestSponsors
(
    sponsorId INT PRIMARY KEY,
    sponsorName VARCHAR(100),
    sponsorType VARCHAR(100),
)

-- create a copy of the sponsorships table with foreign keys on the testtables
CREATE TABLE TestSponsorships
(
    teamId INT,
    sponsorId INT,
    monetaryValue INT,
    PRIMARY KEY (teamId, sponsorId),
    FOREIGN KEY (teamId) REFERENCES TestTeams(teamId),
    FOREIGN KEY (sponsorId) REFERENCES TestSponsors(sponsorId)
)

-- create a basic view on testsponsorships
CREATE VIEW viewSponsorships
AS
SELECT *
FROM TestSponsorships SH



-- create a view to join all 3
CREATE VIEW viewTeamSpoonsorships
AS
SELECT TS.teamName, TS.sponsorName, TS.monetaryValue, T.teamName, S.sponsorName
FROM TestSponsorships TS INNER JOIN TestTeams T
ON TS.teamId = T.teamId INNER JOIN TestSponsors S
ON TS.sponsorId = S.sponsorId

-- create a view that uses joins and group by sponsor name
CREATE VIEW viewTeamSpoonsorshipsGrouped
AS
SELECT TS.sponsorId, S.sponsorName SUM(TS.monetaryValue) AS totalValue
FROM TestSponsorships TS INNER JOIN Sponsors S
ON TS.sponsorId = S.sponsorId
GROUP BY S.sponsorName

-- add all these 6 entities as a test
INSERT INTO Tables (Name) VALUES ('TestTeams')
INSERT INTO Tables (Name) VALUES ('TestSponsors')
INSERT INTO Tables (Name) VALUES ('TestSponsorships')
INSERT INTO Views (Name) VALUES ('viewSponsorships')
INSERT INTO Views (Name) VALUES ('viewTeamSpoonsorships')
INSERT INTO Views (Name) VALUES ('viewTeamSpoonsorshipsGrouped')

-- add test 2
INSERT INTO Tests (Name) VALUES ('Team-Sponsors Test')
DELETE FROM Tests WHERE TestID = 3

-- add testtables and testviews
INSERT INTO TestTables (TestID, TableID NoOfRows, Position) VALUES (2, 2, 100, 3)
INSERT INTO TestTables (TestID, TableID, NoOfRows, Position) VALUES (2, 3, 100, 2)
INSERT INTO TestTables (TestID, TableID, NoOfRows, Position) VALUES (2, 4, 100, 1)

INSERT INTO TestViews (TestID, ViewID) VALUES (2, 2)
INSERT INTO TestViews (TestID, ViewID) VALUES (2, 3)
INSERT INTO TestViews (TestID, ViewID) VALUES (2, 4)

-- run the test
EXEC sp_RunTest 2

