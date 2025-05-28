-- Enable Snapshot isolation on the database (if not enabled)

--ALTER DATABASE ESports SET READ_COMMITTED_SNAPSHOT ON WITH ROLLBACK IMMEDIATE;
--ALTER DATABASE ESports SET ALLOW_SNAPSHOT_ISOLATION ON;
--SET TRANSACTION ISOLATION LEVEL SNAPSHOT;

ALTER DATABASE ESports SET READ_COMMITTED_SNAPSHOT OFF WITH ROLLBACK IMMEDIATE;
ALTER DATABASE ESports SET ALLOW_SNAPSHOT_ISOLATION OFF;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;


-- Transaction 1: Open in one window
BEGIN TRANSACTION;

-- Read the data (optimistic locking behavior)
SELECT * FROM Champions WHERE ChampionID = 1;

-- Simulate a delay to allow Transaction 2 to start
WAITFOR DELAY '00:00:05';

-- Update the Champion role (this is what Transaction 1 wants to change)
UPDATE Champions
SET ChampionRole = 'Tank'
WHERE ChampionID = 1;

-- Commit the transaction
COMMIT TRANSACTION;



-- Transaction 2: Open in another window
BEGIN TRANSACTION;

-- Read the same data (optimistic locking behavior)
SELECT * FROM Champions WHERE ChampionID = 1;

-- Simulate a delay to overlap with Transaction 1's update
WAITFOR DELAY '00:00:03';

-- Attempt to update the same Champion record (this will cause a conflict)
UPDATE Champions
SET ChampionRole = 'Assasssin'
WHERE ChampionID = 1;

-- Try to commit the transaction
COMMIT TRANSACTION;




