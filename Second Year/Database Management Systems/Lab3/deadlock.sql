-- Part 4: Deadlock Example
-- Session A (Transaction 1) – Update Players, then Champions:
BEGIN TRANSACTION;
UPDATE Players SET position = 'Mid' WHERE playerName = 'Faker';
WAITFOR DELAY '00:00:05';  -- Simulate waiting
UPDATE Champions SET championRole = 'Assassin' WHERE championName = 'Ahri';
COMMIT;

-- Session B (Transaction 2) – Update Champions, then Players:
BEGIN TRANSACTION;
UPDATE Champions SET championRole = 'Mage' WHERE championName = 'Ahri';
WAITFOR DELAY '00:00:05';  -- Simulate waiting
UPDATE Players SET position = 'ADC' WHERE playerName = 'Faker';
COMMIT;
-- --- End of Deadlock Example ---

-- Solution to Deadlock Example
-- To resolve the deadlock, we can use a consistent order of operations in both transactions.
-- For example, always update Players first and then Champions in both transactions.
-- This way, we avoid the circular wait condition that leads to a deadlock.

-- Part 4: Deadlock Example
-- Session A (Transaction 1) – Update Players, then Champions:
BEGIN TRANSACTION;
UPDATE Players SET position = 'Mid' WHERE playerName = 'Faker';
WAITFOR DELAY '00:00:05';  -- Simulate waiting
UPDATE Champions SET championRole = 'Assassin' WHERE championName = 'Ahri';
COMMIT;

-- Session B (Transaction 2) – Update Champions, then Players:
BEGIN TRANSACTION;
UPDATE Players SET position = 'ADC' WHERE playerName = 'Faker';
WAITFOR DELAY '00:00:05';  -- Simulate waiting
UPDATE Champions SET championRole = 'Mage' WHERE championName = 'Ahri';
COMMIT;
-- --- End of Deadlock Example ---