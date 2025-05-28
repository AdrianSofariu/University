-- Part 2: Non-repeatable Read Example
-- Session A (Transaction 1) – First Read:
-- SET TRANSACTION ISOLATION LEVEL REPEATABLE READ; // This is the solution to avoid non-repeatable reads
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
SELECT * FROM Players WHERE playerName = 'Faker';

-- Session B (Transaction 2) – Update Data:
BEGIN TRANSACTION;
UPDATE Players
SET position = 'Top'
WHERE playerName = 'Faker';
COMMIT;

-- Session A (Transaction 1) – Re-read Data:
SELECT * FROM Players WHERE playerName = 'Faker';  -- The data will be different (Non-repeatable Read)
COMMIT;
