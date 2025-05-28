-- populate the regions table
INSERT INTO Regions VALUES 
('EMEA'), 
('CN'), 
('NA'), 
('KR'), 
('BR'), 
('APAC'), 
('LAT'), 
('VN');

-- populate the Leagues table
INSERT INTO Leagues(leagueName, abbreviation, maximumNrOfTeams, regionId) VALUES 
('League of Legends EMEA Championship', 'LEC', 10, 1),
('League of Legends Champions Korea', 'LCK', 10, 4),
('League of Legends Pro League', 'LPL', 17, 2),
('League Championship Series', 'LCS', 8, 3),
('Vietnam Championship Series', 'VCS', 8, 9),
('Pacific Championship Series', 'PCS', 11, 6),
('Campeonato Brasileiro de League of Legends', 'CBLOL', 10, 5);

-- populate the Champions table
INSERT INTO Champions(championName, championRole) VALUES 
('Aatrox', 'Fighter'), 
('Ahri', 'Mage'), 
('Akali', 'Assassin'), 
('Alistar', 'Tank'), 
('Aphelios', 'Marksman'), 
('Azir', 'Mage'), 
('Camille', 'Fighter'), 
('Gnar', 'Fighter'), 
('Jarvan IV', 'Fighter'), 
('Jhin', 'Marksman'), 
('Jinx', 'Marksman'), 
('Kennen', 'Mage'), 
('K''sante', 'Tank'), 
('Kai''Sa', 'Marksman'), 
('Le Blanc', 'Assassin'), 
('Jax', 'Fighter'), 
('Leona', 'Tank'), 
('Maokai', 'Tank'), 
('Miss Fortune', 'Marksman'), 
('Nidalee', 'Assassin'), 
('Orianna', 'Mage'), 
('Rakan', 'Support'), 
('Rell', 'Tank'), 
('Renekton', 'Fighter'), 
('Sejuani', 'Tank'), 
('Senna', 'Support'), 
('Vi', 'Fighter'), 
('Viego', 'Fighter'), 
('Zeri', 'Marksman');

-- populate the Coaches table
INSERT INTO Coaches(coachName, coachRealName, coachResidence) VALUES 
('YamatoCannon', 'Jakob Mebdi', 1), 
('kkOma', 'Jeong-Gyun Kim', 4), 
('Dylan Falco', 'Dylan Falco', 3), 
('Nightshare', 'Tomas Knezinek', 1), 
('Nukeduck', 'Erlend Vatevik Holm', 3), 
('KIM', 'Kim Jeong-soo', 4), 
('DanDy', 'Choi In-kyu', 4), 
('Spawn', 'Jake Tiberi', 3), 
('BigWei', 'Fu Chien-Wei', 2), 
('Maokai', 'Yang Ji-Song', 2);

-- populate the Teams table
INSERT INTO Teams(teamName, acronym, leagueId, coachId) VALUES 
('G2 Esports', 'G2', 1, 3), 
('Fnatic', 'FNC', 1, 4), 
('FlyQuest', 'FLY', 4, 5), 
('T1', 'T1', 2, 2), 
('Gen.G', 'GEN', 2, 6), 
('Team Liquid', 'TL', 4, 8), 
('Hanwha Life Esports', 'HLE', 2, 7), 
('Bilibili Gaming', 'BLG', 3, 9), 
('Top Esports', 'TES', 3, 10);

-- populate the Players table
INSERT INTO Players(playerName, realName, position, teamId, regionId) VALUES 
('caps', 'Rasmus Winther', 'MID', 1, 1), 
('mikyx', 'Mihael Mehle', 'SUP', 1, 1), 
('Hans Samara', 'Steven Liv', 'ADC', 1, 1), 
('Broken Blade', 'Sergen Celik', 'TOP', 1, 1), 
('Skewmond', 'Rudy Semaan', 'JNG', 1, 1), 
('Massu', 'Fahad Abdulmalek', 'ADC', 3, 3), 
('Bwipo', 'Gabriel Rau', 'TOP', 3, 1), 
('Noah', 'Oh Hyeon-taek', 'ADC', 2, 4), 
('Chovy', 'Jeong Ji-hoon', 'MID', 5, 4), 
('Faker', 'Lee Sang-hyeok', 'MID', 4, 4), 
('Canyon', 'Kim Geon-bu', 'JNG', 5, 4), 
('Gumayusi', 'Jang Min-chul', 'ADC', 4, 4), 
('Yeon', 'Sean Sung', 'ADC', 6, 3), 
('CoreJJ', 'Jo Yong-in', 'SUP', 6, 4), 
('Zeka', 'Kim Geon-woo', 'MID', 7, 4), 
('Viper', 'Park Do-hyeon', 'ADC', 7, 4), 
('Bin', 'Chen Ze-Bin', 'TOP', 8, 2), 
('Knight', 'Zhuo Ding', 'MID', 8, 2), 
('JackeyLove', 'Yu Wen-Bo', 'ADC', 9, 2), 
('Tian', 'Gao Tian-Liang', 'JNG', 9, 2);

-- populate the Picks table
INSERT INTO Picks(playerId, championId, wins, losses) VALUES 
(18, 21, 4, 4), 
(19, 23, 2, 10), 
(24, 6, 5, 0), 
(23, 2, 1, 1), 
(29, 3, 10, 2), 
(31, 16, 7, 1), 
(33, 10, 2, 0);

-- populate the Tournaments table
INSERT INTO Tournaments(tournamentName, location, startDate, endDate, prizePool, winner) VALUES 
('LEC Spring 2021', 'Berlin', '2021-01-22', '2021-04-11', 200000, 28), 
('LCK Spring 2024', 'Seoul', '2024-01-13', '2024-04-10', 285200, 32), 
('MSI 2019', 'Taipei', '2019-05-01', '2019-05-19', 1000000, 28), 
('Worlds 2023', 'Seoul', '2023-09-13', '2023-11-19', 2225000, 31);

-- populate Venues table
INSERT INTO Venues(venueName, location, capacity) VALUES 
('LEC Studio', 'Berlin', 174), 
('LoL Park', 'Seoul', 450), 
('Gocheok Sky Dome', 'Seoul', 50000), 
('O2 Arena', 'London', 20000), 
('Beijing National Stadium', 'Beijing', 91000), 
('Chase Center', 'San Francisco', 18060);

-- populate the Matches table
INSERT INTO Matches(teamId1, teamId2, date, tournamentId, venueId,  scoreTeam1, scoreTeam2) VALUES 
(28, 29, '2021-04-11', 1, 1, 3, 2), 
(31, 32, '2024-04-10', 2, 2, 1, 3), 
(28, 31, '2019-05-18', 3, 3, 3, 2);

-- populate the Sponsors table
INSERT INTO Sponsors(sponsorName, domainOfActivity) VALUES 
('Red Bull', 'Energy Drinks'), 
('Mercedes-Benz', 'Automotive'), 
('Honda', 'Automotive'), 
('Samsung', 'Technology'), 
('Ralph Lauren', 'Fashion'), 
('Puma', 'Fashion'), 
('KIA', 'Automotive');

-- populate the Sponsorships table
INSERT INTO Sponsorships(teamId, sponsorId, monetaryValue) VALUES 
(28, 1, 100000), 
(31, 2, 50000), 
(32, 6, 75000), 
(33, 3, 100000), 
(31, 4, 50000), 
(28, 5, 75000), 
(31, 1, 100000);

-- populate the Events table
INSERT INTO Events(eventName, eventDate) VALUES 
('Paris Worlds 2024 Fan meeting', '2024-10-20'), 
('Berlin Red Bull League of its Own', '2021-04-11'), 
('Seoul Mercedes-Benz Invitational', '2024-04-10'), 
('Worlds 2023 Finals Opening Ceremony', '2023-11-19');

-- populate the Participants table
INSERT INTO Participants(eventId, teamId) VALUES 
(2, 28), 
(2, 31);

-- example of a failed insert
INSERT INTO Players(playerName, realName, position, teamId, regionId) VALUES 
('caps', 'Error', 'MID', 1, 1);
