-- update the picks table by adding a loss where the win ratio is above 50% or where there are 2 or less than 2 losses
UPDATE Picks
SET losses = losses + 1
WHERE wins < losses OR losses <= 2


-- rename the tournament MSI 2019 to Mid Season Invitational 2019
UPDATE Tournaments
SET tournamentName = 'Mid Season Invitational 2019'
WHERE tournamentName = 'MSI 2019'

-- set YamatoCannon as the coach of Fnatic if they dont already have a coach
UPDATE Teams
SET coachId = ( SELECT C.coachId FROM Coaches C WHERE C.coachName = 'YamatoCannon')
WHERE teamName = 'Fnatic' AND coachId IS NULL


-- double the capacity of LoL Park and LEC Studio
UPDATE Venues
SET capacity = capacity * 2
WHERE venueName IN ('LoL Park', 'LEC Studio')

-- increase the prizePool of all tournaments with prizePool over 2 mil that are not held in Seoul
UPDATE Tournaments
SET prizePool = prizePool + 8000
WHERE prizePool > 2000000 AND location <> 'Seoul'

-- add 10000 dollars from skin sales to the tournaments that already have winners
UPDATE Tournaments
SET prizePool = prizePool + 10000
WHERE winner IS NOT NULL

-- delete all Tournaments that began between January 2020 and January 2021
DELETE FROM Tournaments
WHERE startDate BETWEEN '2020-01-01' AND '2021-01-01'


-- delete all champions starting with the letter Y
DELETE FROM Champions
WHERE championName LIKE 'Y%'

-- delete all players from TES
DELETE FROM Players
WHERE teamId = (SELECT teamId FROM Teams WHERE teamName = 'TES')

-- make Noah teamless
UPDATE Players
SET teamId = NULL
WHERE playerName = 'Noah'