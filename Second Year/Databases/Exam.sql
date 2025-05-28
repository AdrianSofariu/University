create table Tournaments(
	tournamentName VARCHAR(100) PRIMARY KEY,
	startDate DATE,
	endDate DATE,
)


create table Courts(
	courtName VARCHAR(100) PRIMARY KEY,
	capacity INT
)

create table TournamentVenues(
	tournamentName VARCHAR(100) references Tournaments(tournamentName),
	courtName VARCHAR(100) references Courts(courtName),
	PRIMARY KEY(tournamentName, courtName)
)

create table Players(
	playerName VARCHAR(100) PRIMARY KEY,
	prizeMoney INT,
	points INT
)

create table Matches(
	playerName1 VARCHAR(100) references Players(playerName),
	playerName2 VARCHAR(100) references Players(playerName),
	tournamentName VARCHAR(100) references Tournaments(tournamentName),
	matchDate DATETIME,
	winner INT,
	points INT,
	prize INT
)

insert into Tournaments values('Tournament1', '2021-01-01', '2021-01-02'),
                               ('Tournament2', '2021-02-01', '2021-02-02'),
                                 ('Tournament3', '2021-03-01', '2021-03-02')
                                 


insert into Courts values('Court1', 100),
            ('Court2', 200),
            ('Court3', 300),
            ('Court4', 400)

insert into TournamentVenues values('Tournament1', 'Court1'),
                                  ('Tournament1', 'Court2'),
                                  ('Tournament2', 'Court3'),
                                  ('Tournament2', 'Court4')

insert into Players values('Player1', 1000, 0),
                         ('Player2', 2000, 0),
                         ('Player3', 3000, 0),
                         ('Player4', 4000, 0)

insert into Matches values('Player1', 'Player2', 'Tournament1', '2021-01-01 13:23:44', 1, 10, 100),
                         ('Player3', 'Player4', 'Tournament2', '2021-02-01 15:45:21', 2, 20, 200),
                         ('Player1', 'Player3', 'Tournament1', '2021-01-01 11:12:01', 2, 30, 300),
                         ('Player2', 'Player4', 'Tournament2', '2021-02-01 14:56:59', 1, 40, 400)