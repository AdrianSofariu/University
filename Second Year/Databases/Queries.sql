-- 2 queries with the union operation using UNION [ALL] and OR

-- select all teams that have won a game
SELECT M.teamId1
FROM Matches M
WHERE M.scoreTeam1 > M.scoreTeam2
UNION
SELECT M.teamId2
FROM Matches M
WHERE M.scoreTeam2 > M.scoreTeam1


-- select the players that have played at least one game
SELECT DISTINCT P.playerId
FROM Picks P
WHERE P.wins > 0 OR P.losses > 0


-- 2 queries with the intersect operation using INTERSECT and IN

-- select teams that have won a tournament and participated in an event
SELECT T.winner
FROM Tournaments T
INTERSECT
SELECT P.teamId
FROM Participants P

-- select all regions that have both a team and a coach
SELECT DISTINCT P.regionId
FROM Players P
WHERE P.regionId IN (
    SELECT C.coachResidence
    FROM Coaches C)



-- 2 queries with the except operation using EXCEPT and NOT IN

-- select all teams that have not won a tournament
SELECT T.teamId
FROM Teams T
EXCEPT
SELECT T.winner
FROM Tournaments T

-- select all unplayed champions
SELECT C.championId
FROM Champions C
WHERE C.championId NOT IN (
    SELECT P.championId
    FROM Picks P)




-- 4 queries with INNER JOIN, RIGHT JOIN, LEFT JOIN, FULL JOIN  #DONE

-- select all players, their region and their teams
SELECT P.playerName, P.realName, R.regionName, T.teamName
FROM Players P LEFT JOIN Teams T 
ON P.teamId = T.teamId LEFT JOIN Regions R 
ON P.regionId = R.regionId

-- select all sponsorhips, include also sponsors with no active monetary sponsorships
SELECT *
FROM Sponsorships SH RIGHT JOIN Sponsors S 
ON SH.sponsorId = S.sponsorId

-- select all records of players with a champion, include unplayed champions and players that have yet to play 
SELECT C.championName, c.championRole, PL.playerName, PL.position, P.wins, P.losses
FROM Picks P FULL JOIN Champions C
ON P.championId = C.championId FULL JOIN Players PL
ON P.playerId = PL.playerId

-- select all teams that participated in a media event and their sponsors
SELECT E.eventName, E.eventDate, T.teamName, S.sponsorName
FROM Participants P INNER JOIN Events E
ON P.eventId = E.eventId INNER JOIN Teams T
ON P.teamId = T.teamId INNER JOIN Sponsorships SH
ON P.teamId = SH.teamId INNER JOIN Sponsors S
ON SH.sponsorId = S.sponsorId



-- 2 queries with the IN operator and a subquery in the WHERE clause;
-- in at least one case, the subquery must include a subquery in its own WHERE clause;

-- select all records of mage champions
SELECT *
FROM Picks P
WHERE P.championId IN (
    SELECT C.championId
    FROM Champions C
    WHERE C.championRole = 'Mage')

-- select all players that play in the european or north american league
SELECT *
FROM Players P
WHERE P.teamId IN (
    SELECT teamId
    FROM Teams T
    WHERE T.leagueId IN (
        SELECT leagueId
        FROM Leagues L
        WHERE L.abbreviation IN ('LEC', 'LCS')))



-- 2 queries with the EXISTS operator and a subquery in the WHERE clause;

-- select all players that have played a champion
SELECT DISTINCT *
FROM Players P
WHERE EXISTS (
    SELECT *
    FROM Picks PI
    WHERE PI.playerId = P.playerId)


-- select all the coaches that do not have a team
SELECT *
FROM Coaches C
WHERE NOT EXISTS (
    SELECT *
    FROM Teams T
    WHERE T.coachId = C.coachId)



-- 2 queries with a subquery in the FROM clause; 

-- compute the top 3 records (by winrate) of players that play mage or assassin champions
SELECT TOP 3 ROUND(R.wins * 1.0/(R.wins + R.losses) * 100, 2) AS winRatio, R.playerName, R.championName
FROM (
	SELECT PL.playerName, P.championId, P.wins, P.losses, C.championName
	FROM Picks P INNER JOIN Champions C 
	ON P.championId = C.championId INNER JOIN Players PL
	ON PL.playerId = P.playerId
	WHERE C.championRole = 'Mage' OR C.championRole = 'Assassin') AS R
ORDER BY winRatio DESC


-- find all sponsors that have better deals than the average deal
SELECT DISTINCT R.sponsorName
FROM (
    SELECT S.sponsorName, SH.monetaryValue
    FROM Sponsorships SH INNER JOIN Sponsors S
    ON SH.sponsorId = S.sponsorId) AS R
WHERE R.monetaryValue > (
    SELECT AVG(monetaryValue)
    FROM Sponsorships)


-- 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause;
-- 2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX;

-- find the top 3 teams with the most games played
SELECT TOP 3 T.teamName, COUNT(M.date) AS nrOfMatches
FROM Teams T INNER JOIN Matches M
ON T.teamId = M.teamId1 OR T.teamId = M.teamId2
GROUP BY T.teamName
ORDER BY nrOfMatches DESC


-- select the teams with 5 players
SELECT T.teamName
FROM Teams T INNER JOIN Players P
ON T.teamId = P.teamId
GROUP BY T.teamName
HAVING COUNT(P.playerId) = 5

-- compute the number of games per venue played in venues with less than 500 places
SELECT venueId, COUNT(*) gamesPlayed
FROM Matches M
GROUP BY M.venueId
HAVING venueId IN (SELECT venueId
				   FROM Venues V
				   WHERE V.capacity < 500)

-- find the sponsorships with the highest value for sponsors in the automotive or fashion domain
SELECT SH.sponsorId, MAX(SH.monetaryValue) as spnosorshipValue
FROM Sponsorships SH
GROUP BY SH.sponsorId
HAVING sponsorId IN (SELECT sponsorId
						FROM Sponsors S
						WHERE S.domainOfActivity IN ('Automotive', 'Fashion'))




-- 4 queries using ANY and ALL to introduce a subquery in the WHERE clause (2 queries per operator);
-- rewrite 2 of them with aggregation operators, and the other 2 with IN / [NOT] IN.

-- select all players that have played a champion with a winrate above 50%
SELECT *
FROM Players P
WHERE P.playerId = ANY (
    SELECT PI.playerId
    FROM Picks PI
    WHERE PI.wins * 1.0/(PI.wins + PI.losses) > 0.5)

-- rewrite the query with an in operator
SELECT *
FROM Players P
WHERE P.playerId IN (
    SELECT PI.playerId
    FROM Picks PI
    WHERE PI.wins * 1.0/(PI.wins + PI.losses) > 0.5)



-- compute an increased number of teams (by 2) for leagues with less than the maximum number of teams in any league
SELECT leagueName, abbreviation, maximumNrOfTeams + 2, regionId
FROM Leagues L
WHERE L.maximumNrOfTeams < ANY(
	SELECT DISTINCT maximumNrOfTeams
	FROM Leagues L)

-- rewrite the query with an aggregation operator
SELECT leagueName, abbreviation, maximumNrOfTeams + 2, regionId
FROM Leagues L
WHERE L.maximumNrOfTeams < (
    SELECT MAX(maximumNrOfTeams)
    FROM Leagues L)


-- select the sponsorships equal or higher with the maximum value of all T1 sponsorships
SELECT *
FROM Sponsorships SH
WHERE SH.monetaryValue >= ALL (
    SELECT SH1.monetaryValue
    FROM Sponsorships SH1
    WHERE SH1.teamId = (SELECT T.teamId
                        FROM Teams T
                        WHERE T.acronym = 'T1'))

-- rewrite the query with an aggregation operator
SELECT *
FROM Sponsorships SH
WHERE SH.monetaryValue >= (
    SELECT MAX(SH1.monetaryValue)
    FROM Sponsorships SH1
    WHERE SH1.teamId = (SELECT T.teamId
                        FROM Teams T
                        WHERE T.acronym = 'T1'))


-- compute a halved capacity for venues where no games have been played
SELECT V.venueName, V.location, V.capacity/2 as HalvedCap
FROM Venues V
WHERE V.venueId <> ALL( SELECT M.venueId
						FROM Matches M)

-- rewrite the query with an in operator
SELECT V.venueName, V.location, V.capacity/2 as HalvedCap
FROM Venues V
WHERE V.venueId NOT IN( SELECT M.venueId
                        FROM Matches M)


/*You must use:

arithmetic expressions in the SELECT clause in at least 3 queries; 3/3
conditions with AND, OR, NOT, and parentheses in the WHERE clause in at least 3 queries; 3/3
DISTINCT in at least 3 queries, ORDER BY in at least 2 queries, and TOP in at least 2 queries. 3/3, 2/2, 2/2

*/










