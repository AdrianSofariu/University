CREATE TABLE Champions(
	championId INT PRIMARY KEY IDENTITY(1,1),
	championName VARCHAR(50) NOT NULL UNIQUE,
	championRole VARCHAR(50) NOT NULL,
)

CREATE TABLE Regions(
	regionId INT PRIMARY KEY IDENTITY(1,1),
	regionName VARCHAR(50) NOT NULL UNIQUE,
)


CREATE TABLE Coaches(
	coachId INT PRIMARY KEY IDENTITY(1,1),
	coachName VARCHAR(50) NOT NULL UNIQUE,
	coachResidence INT,
	coachRealName VARCHAR(50) NOT NULL UNIQUE,
	FOREIGN KEY (coachResidence) REFERENCES Regions(regionId) ON DELETE SET NULL,
)

CREATE Table Leagues(
	leagueId INT PRIMARY KEY IDENTITY(1,1),
	leagueName VARCHAR(100) NOT NULL UNIQUE,
	abbreviation VARCHAR(5) NOT NULL UNIQUE,
	maximumNrOfTeams INT NOT NULL,
	regionId INT,
	FOREIGN KEY (regionId) REFERENCES Regions(regionId) ON DELETE SET NULL,
)

CREATE Table Teams(
	teamId INT PRIMARY KEY IDENTITY(1,1),
	teamName VARCHAR(100) NOT NULL UNIQUE,
	acronym VARCHAR(3) NOT NULL UNIQUE,
	leagueId INT,
	coachId INT UNIQUE,
	FOREIGN KEY (leagueId) REFERENCES Leagues(leagueId) ON DELETE SET NULL,
	FOREIGN KEY (coachId) REFERENCES Coaches(coachId) ON DELETE SET NULL,
)

CREATE TABLE Players(
	playerId INT PRIMARY KEY IDENTITY(1,1),
	playerName VARCHAR(50) NOT NULL UNIQUE,
	realName VARCHAR(50) NOT NULL UNIQUE,
	position VARCHAR(3) NOT NULL,
	teamId INT,
	regionId INT,
	FOREIGN KEY (teamId) REFERENCES Teams(teamId) ON DELETE SET NULL,
	FOREIGN KEY (regionId) REFERENCES Regions(regionId) ON DELETE SET NULL,
)

CREATE TABLE Picks(
	playerId INT NOT NULL,
	championId INT NOT NULL,
	wins INT DEFAULT 0,
	losses INT DEFAULT 0,
	PRIMARY KEY (playerId, championId),
	FOREIGN KEY (playerId) REFERENCES Players(playerId) ON DELETE CASCADE,
	FOREIGN KEY (championId) REFERENCES Champions(championId) ON DELETE CASCADE,
)

CREATE TABLE Sponsors(
	sponsorId INT PRIMARY KEY IDENTITY(1,1),
	sponsorName VARCHAR(100) NOT NULL UNIQUE,
	domainOfActivity VARCHAR(100) NOT NULL,
)

CREATE TABLE Sponsorships(
	teamId INT NOT NULL,
	sponsorId INT NOT NULL,
	monetaryValue DECIMAL(15,2) DEFAULT 0,
	PRIMARY KEY (teamId, sponsorId),
	FOREIGN KEY (teamId) REFERENCES Teams(teamId) ON DELETE CASCADE,
	FOREIGN KEY (sponsorId) REFERENCES Sponsors(sponsorId) ON DELETE CASCADE,
)

CREATE TABLE Venues(
	venueId INT PRIMARY KEY IDENTITY(1,1),
	venueName VARCHAR(100) NOT NULL UNIQUE,
	location VARCHAR(100) NOT NULL,
	capacity INT NOT NULL,
)


CREATE TABLE Matches(
	teamId1 INT NOT NULL,
	teamId2 INT NOT NULL,
	date DATE NOT NULL,
	tournamentId INT NOT NULL,
	venueId INT NOT NULL,
	scoreTeam1 INT,
	scoreTeam2 INT,
	PRIMARY KEY(teamId1, teamId2, date),
	FOREIGN KEY (teamId1) REFERENCES Teams(teamId),
	FOREIGN KEY (teamId2) REFERENCES Teams(teamId),
	FOREIGN KEY (tournamentId) REFERENCES Tournaments(tournamentId),
	FOREIGN KEY (venueId) REFERENCES Venues(venueId),
)


CREATE TABLE Tournaments(
	tournamentId INT PRIMARY KEY IDENTITY(1,1),
	tournamentName VARCHAR(100) NOT NULL UNIQUE,
	location VARCHAR(100) NOT NULL,
	startDate DATE,
	endDate DATE,
	prizePool DECIMAL(15,2) DEFAULT 0,
	winner INT,
	FOREIGN KEY (winner) REFERENCES Teams(teamId),
)

CREATE TABLE Events(
	eventId INT PRIMARY KEY IDENTITY(1,1),
	eventName VARCHAR(100) NOT NULL UNIQUE,
	eventDate DATE NOT NULL,
)

CREATE TABLE Partitcipants(
	eventId INT NOT NULL,
	teamId INT NOT NULL,
	PRIMARY KEY(eventId, teamId),
	FOREIGN KEY (eventId) REFERENCES Events(eventId),
	FOREIGN KEY (teamId) REFERENCES Teams(teamId),
)
	


DROP TABLE Champions
DROP TABLE Regions
DROP TABLE Players
DROP TABLE Coaches
DROP TABLE Leagues
DROP TABLE Teams
DROP TABLE Picks
DROP TABLE Sponsors
DROP TABLE Sponsorships
DROP TABLE Venues
DROP TABLE Tournaments
DROP TABLE Matches