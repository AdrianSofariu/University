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
	venueId INT UNIQUE IDENTITY(1,1),
	tournamentName VARCHAR(100) references Tournaments(tournamentName),
	courtName VARCHAR(100) references Courts(courtName),
	PRIMARY KEY(venueId, tournamentName, courtName)
)

DROP TABLE TournamentVenues

create table Players(
	playerName VARCHAR(100) PRIMARY KEY,
	prizeMoney INT,
	points INT
)

create table Matches(
	playerName1 VARCHAR(100) references Players(playerName),
	playerName2 VARCHAR(100) references Players(playerName),
	venueId INT references TournamentVenues(venueId),
	matchDate DATETIME,
	winner INT,
	points INT,
	prize INT
)

DROP TABLE Matches


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

insert into Matches values('Player1', 'Player2', 1, '2021-01-01 13:23:44', 1, 10, 100),
                         ('Player3', 'Player4', 3, '2021-02-01 15:45:21', 2, 20, 200),
                         ('Player1', 'Player3', 1, '2021-01-01 11:12:01', 2, 30, 300),
                         ('Player2', 'Player4', 4, '2021-02-01 14:56:59', 1, 40, 400)
						 ('Player1', 'Player4', 4, '2021-02-01 14:56:59', 1, 40, 400),
						 ('Player1', 'Player2', 3, '2021-02-03 16:00:00', 1, 40, 400),
						 ('Player1', 'Player3', 2, '2021-02-05 16:00:00', 1, 40, 400)

delete from matches where playerName1 = 'Player1' and playerName2 = 'Player3' and venueId = '1'

insert into Matches values ('Player1', 'Player3', 1, '2021-01-01 11:12:01', 2, 30, 300),
							('Player3', 'Player1', 2, '2021-02-05 16:00:00', 1, 40, 400)

go
create or alter procedure usp_addCourt @courtName VARCHAR(100), @tournamentName VARCHAR(100) as
begin
	declare @venue VARCHAR(100) = (select v.courtName from TournamentVenues v where v.tournamentName = @tournamentName and v.courtName = @courtName)

	if @venue is not null
	begin
		print 'Venue already exists'
	end
	else
		insert into TournamentVenues values (@tournamentName, @courtName)
end


select * from TournamentVenues
exec  usp_addCourt 'Court1', 'Tournament1'
exec  usp_addCourt 'Court1', 'Tournament2'
delete from TournamentVenues where tournamentName = 'Tournament2' and courtName = 'Court1' 



go
create or alter function usf_filteredTournaments(@c int)
returns table
as
return
select t.tournamentName
from Tournaments t
where t.tournamentName IN (
	select v.tournamentName
	from TournamentVenues v
	group by v.tournamentName
	having count(*) >= @c)

select * from usf_filteredTournaments(2)
select * from Tournaments


create or alter view ViewPlayers as
	select p.playerName
	from Players p inner join Matches m on p.playerName = m.playerName1 or p.playerName = m.playerName2
	inner join TournamentVenues v on m.venueId = v.venueId
	group by p.playerName
	having count(distinct v.courtName) = (select count(*) from courts)

select * from ViewPlayers
select * from Matches
select count(*) from courts


-- 1. d <28,3>
-- 2. e. None (8)
-- 3. a,c. 10 < 11 < 15

create table t(
	id int,
	a int,
	b int,
	c int,
	d int
	)

drop table t

insert into t values(20,1,20,5,1),
					(21,2,20,5,1),
					(22,3,20,5,1),
					(23,4,21,6,2),
					(24,5,21,6,2),
					(25,6,24,7,3),
					(26,7,24,7,3),
					(27,8,28,7,3),
					(28,9,28,8,3),
					(29,10,28,8,3)

select t1.b, sum(t1.d) as e
from t t1
group by t1.b
union all
select t2.b, count(t2.c) as e
from t t2
group by t2.b

go
create or alter trigger insert_trigger
on t
for insert
as
	declare @total int
	select @total = SUM(i.c - i.d)
	from inserted i

	print @total

insert into t values (30, 11, 28, 9, 3),
					(31, 12, 30, 9, 4)