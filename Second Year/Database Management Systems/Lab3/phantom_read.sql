-- Part 3: Phantom Read Example
-- Session A (Transaction 1) – Read all players with position 'Mid':
-- SET TRANSACTION ISOLATION LEVEL SERIALIZABLE; // This is the solution to avoid phantom reads
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
SELECT * FROM Players WHERE position = 'Mid';

-- Session B (Transaction 2) – Insert New Row:
BEGIN TRANSACTION;
INSERT INTO Players (playerName, realName, position)
VALUES ('NewPlayer', 'Jackies', 'Mid');
COMMIT; 

-- Session A (Transaction 1) – Re-read data (Phantom Read):
SELECT * FROM Players WHERE position = 'Mid';  -- You will see the new row inserted by Session B
COMMIT;
