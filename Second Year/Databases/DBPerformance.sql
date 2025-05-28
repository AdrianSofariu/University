GO
--procedure that deletes all data from a table
CREATE OR ALTER PROCEDURE sp_DeleteAllData
    @tableName VARCHAR(100)
AS
BEGIN
    DECLARE @deleteString NVARCHAR(MAX) = 'DELETE FROM ' + @tableName
    EXEC sp_executesql @deleteString
END

GO
-- procedure that inserts mock data in a given table
CREATE OR ALTER PROCEDURE sp_InsertMockData
    @tableName VARCHAR(100),
    @numberOfRows INT
AS
BEGIN

    -- insert mock data
    DECLARE @i INT = 0
    DECLARE @numberOfColumns INT

    -- get the data type of each column in the table
    DECLARE @columnNames TABLE (name VARCHAR(100), type VARCHAR(100))
    INSERT INTO @columnNames
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = @tableName

    -- declare a cursor to iterate through the columns
    DECLARE columnCursor CURSOR FOR
    SELECT name, type
    FROM @columnNames

    
    --create a string that will be used to insert the data
    DECLARE @insertString NVARCHAR(MAX) = 'INSERT INTO ' + @tableName + ' VALUES ('
    DECLARE @columnType VARCHAR(100)
    DECLARE @columnName VARCHAR(100)
    DECLARE @columnValueInt INT
    DECLARE @columnValueFloat FLOAT
    DECLARE @columnValueDate DATE
    DECLARE @columnValueString VARCHAR(100)
    DECLARE @columnValueBool BIT

    WHILE @i < @numberOfRows
    BEGIN
    --use a cursor to iterate through the columns
        OPEN columnCursor
        FETCH NEXT FROM columnCursor INTO @columnName, @columnType
        WHILE @@FETCH_STATUS = 0
        BEGIN
            IF @columnType = 'int'
            BEGIN
                SET @columnValueInt = @i
                SET @insertString = @insertString + CONVERT(varchar, @columnValueInt) + ','
            END
            ELSE IF @columnType = 'float'
            BEGIN
                SET @columnValueFloat = RAND() * 100
                SET @insertString = @insertString + @columnValueFloat + ','
            END
            ELSE IF @columnType = 'date'
            BEGIN
                SET @columnValueDate = GETDATE()
                SET @insertString = @insertString + ''''+ CONVERT(varchar, @columnValueDate) + ''','
            END
            ELSE IF @columnType = 'varchar'
            BEGIN
                SET @columnValueString = '''string'''
                SET @insertString = @insertString + @columnValueString + ','
            END
            FETCH NEXT FROM columnCursor INTO @columnName, @columnType
        END
        CLOSE columnCursor

        -- remove the last comma from the string
        SET @insertString = LEFT(@insertString, LEN(@insertString) - 1)
        SET @insertString = @insertString + ')'

        -- execute the insert statement
        EXEC sp_executesql @insertString

		--reset insert string
		SET @insertString = 'INSERT INTO ' + @tableName + ' VALUES ('

        -- increment the counter
        SET @i = @i + 1
    END
END
GO

-- run the procedure on the Participants table
EXEC sp_InsertMockData 'TestTable', 5
SELECT * FROM TestTable

--create a test table
CREATE TABLE TestTable
(
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    DateOfBirth DATE
)

DROP TABLE TestTable

SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'TestTable'


--procedure that calls the insert mock data procedure for all tables
--with the same test id's in the order given by position
CREATE OR ALTER PROCEDURE sp_testTables
    @testID INT,
    @testRunID INT
AS
BEGIN
    -- get all tables with the same test id from the TestTables table in a cursor
    DECLARE @tableId INT
    DECLARE @tableName VARCHAR(100)
    DECLARE @numberOfRows INT
    DECLARE @position INT

    -- declare a timer
    DECLARE @startTime DATETIME
    DECLARE @endTime DATETIME

    -- make cursor bidirectional
    DECLARE tableCursor CURSOR SCROLL FOR
    SELECT TableID, NoOfRows, Position
    FROM TestTables
    WHERE TestID = @testID
    ORDER BY Position

    -- delete all data from the tables
    OPEN tableCursor
    FETCH NEXT FROM tableCursor INTO @tableId, @numberOfRows, @position
    WHILE @@FETCH_STATUS = 0
    BEGIN
        --get the table name
        SELECT @tableName = Name
        FROM Tables
        WHERE TableID = @tableId

        -- call delete all data procedure for each table
        EXEC sp_DeleteAllData @tableName
        FETCH NEXT FROM tableCursor INTO @tableId, @numberOfRows, @position
    END

    -- insert data in reverse order
    FETCH LAST FROM tableCursor INTO @tableId, @numberOfRows, @position
    WHILE @@FETCH_STATUS = 0
    BEGIN
        --get the table name
        SELECT @tableName = Name
        FROM Tables
        WHERE TableID = @tableId

        -- start a timer
        SET @startTime = GETDATE()

        -- call the insert mock data procedure for each table
        EXEC sp_InsertMockData @tableName, @numberOfRows

        -- end the timer
        SET @endTime = GETDATE()

        -- insert the result into the TestRunTables table
        INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (@testRunID, @tableId, @startTime, @endTime)

        -- print the time it took to insert the data
        PRINT 'Inserted ' + CONVERT(VARCHAR, @numberOfRows) + ' rows into ' + @tableName + ' in ' + CONVERT(VARCHAR, DATEDIFF(MILLISECOND, @startTime, @endTime)) + ' milliseconds'
        
        -- get the next table
        FETCH PRIOR FROM tableCursor INTO @tableId, @numberOfRows, @position
    END
    CLOSE tableCursor
    DEALLOCATE tableCursor
END
GO

--procedure that runs all views for a given test run similar to the sp_testTables procedure
CREATE OR ALTER PROCEDURE sp_testViews
    @testRunID INT,
    @testID INT
AS
BEGIN
    -- get all views with the same test id from the TestViews table in a cursor
    DECLARE @viewId INT
    DECLARE @viewName VARCHAR(100)
    DECLARE @query NVARCHAR(MAX) -- query to run the view
    

    -- declare a timer
    DECLARE @startTime DATETIME
    DECLARE @endTime DATETIME

    DECLARE viewCursor CURSOR FOR
    SELECT ViewID
    FROM TestViews
    WHERE TestID = @testID

    OPEN viewCursor
    FETCH NEXT FROM viewCursor INTO @viewId
    WHILE @@FETCH_STATUS = 0
    BEGIN
        --get the view name
        SELECT @viewName = Name
        FROM Views
        WHERE ViewID = @viewId

        -- start a timer
        SET @startTime = GETDATE()

        -- call the view
        SET @query = 'SELECT * FROM ' + @viewName
        EXEC sp_executesql @query

        -- end the timer
        SET @endTime = GETDATE()

        -- insert the result into the TestRunViews table
        INSERT INTO TestRunViews (TestRunID, ViewID, StartAt, EndAt) VALUES (@testRunID, @viewId, @startTime, @endTime)

        -- print the time it took to run the view
        PRINT 'Ran ' + @viewName + ' in ' + CONVERT(VARCHAR, DATEDIFF(MILLISECOND, @startTime, @endTime)) + ' milliseconds'

        -- get the next view
        FETCH NEXT FROM viewCursor INTO @viewId
    END
    CLOSE viewCursor
    DEALLOCATE viewCursor
END
GO

-- create procedure to run a test
CREATE OR ALTER PROCEDURE sp_RunTest
    @testID INT
AS
BEGIN
    -- insert the test run into the TestRuns table and get the test run id
    DECLARE @testRunID INT
    DECLARE @description VARCHAR(100)

    -- declare a timer
    DECLARE @startTime DATETIME
    DECLARE @endTime DATETIME

    -- get test name
    DECLARE @testName VARCHAR(100)

    SELECT @testName = Name
    FROM Tests
    WHERE TestID = @testID

    -- set the description
    SELECT @description = 'Running test ' + @testName
    SET @startTime = GETDATE()

    INSERT INTO TestRuns (Description, StartAt) VALUES (@description, @startTime)

    -- get the test run id
    SELECT @testRunID = SCOPE_IDENTITY()

    -- run the test
    EXEC sp_testTables @testID, @testRunID
    EXEC sp_testViews @testRunID, @testID

    -- update the test run end time
    SET @endTime = GETDATE()
    UPDATE TestRuns
    SET EndAt = @endTime
    WHERE TestRunID = @testRunID

    -- print the time it took to run the test
    PRINT 'Test ' + @testName + ' completed in ' + CONVERT(VARCHAR, DATEDIFF(MILLISECOND, @startTime, @endTime)) + ' milliseconds'
END
GO


-- create a view on the TestTable
CREATE VIEW TestView AS
SELECT * FROM TestTable

-- test the sp_testTables procedure
--add a test
INSERT INTO Tests (Name) VALUES ('Test1')
SELECT * FROM Tests

--add the TestTable
INSERT INTO Tables (Name) VALUES ('TestTable')
SELECT * FROM Tables

--add the View
INSERT INTO Views (Name) VALUES ('TestView')
SELECT * FROM Views

--add the TestViews
INSERT INTO TestViews (TestID, ViewID) VALUES (1, 1)
SELECT * FROM TestViews


--add the TestTables
INSERT INTO TestTables (TestID, TableID, NumberOfRows, Position) VALUES (1, 1, 5, 1)
SELECT * FROM TestTables

-- execute the sp_testTables procedure
EXEC sp_testTables 1, 1

-- execute the sp_testViews procedure
EXEC sp_testViews 1, 1

-- run the test
EXEC sp_RunTest 1

-- remove winner foreign key
ALTER TABLE Matches
DROP CONSTRAINT FK_Matches_Winner
