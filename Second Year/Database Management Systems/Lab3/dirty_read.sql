-- Part 1: Dirty Read Example
-- Session A (Transaction 1) – Update without committing:
BEGIN TRANSACTION;
UPDATE Players
SET position = 'ADC'
WHERE playerName = 'Faker';
-- Do NOT commit here, just leave the transaction open

-- Session B (Transaction 2) – Read with READ UNCOMMITTED:
-- SET TRANSACTION ISOLATION LEVEL READ COMMITTED; // This is the solution to avoid dirty reads
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM Players WHERE playerName = 'Faker';
-- You will see the uncommitted update from Session A (Dirty Read)
