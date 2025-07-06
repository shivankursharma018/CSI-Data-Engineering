-- 
CREATE PROCEDURE dbo.GenerateAndCreateTable
    @TableName NVARCHAR(128)
AS
BEGIN
    DECLARE @SQL NVARCHAR(MAX) = ''

    SELECT @SQL = 'IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ''' + @TableName + ''')
    BEGIN
        CREATE TABLE [' + @TableName + '] ('

    SELECT @SQL = @SQL +
        COLUMN_NAME + ' ' +
        DATA_TYPE +
        CASE 
            WHEN CHARACTER_MAXIMUM_LENGTH IS NOT NULL AND DATA_TYPE IN ('nvarchar', 'varchar', 'char') THEN '(' + 
                CASE WHEN CHARACTER_MAXIMUM_LENGTH = -1 THEN 'MAX' ELSE CAST(CHARACTER_MAXIMUM_LENGTH AS VARCHAR) END + ')'
            WHEN DATA_TYPE IN ('decimal', 'numeric') THEN '(' + 
                CAST(NUMERIC_PRECISION AS VARCHAR) + ',' + CAST(NUMERIC_SCALE AS VARCHAR) + ')'
            ELSE ''
        END +
        CASE WHEN IS_NULLABLE = 'NO' THEN ' NOT NULL,' ELSE ',' END
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = @TableName

    -- Remove last comma, close the CREATE TABLE
    SET @SQL = LEFT(@SQL, LEN(@SQL) - 1) + ') END'

    EXEC sp_executesql @SQL
END

--
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Subject NVARCHAR(100),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(20),
    HireDate DATE
);
INSERT INTO Teachers (TeacherID, FirstName, LastName, Subject, Email, PhoneNumber, HireDate)
VALUES
(1, 'Amit', 'Sharma', 'Mathematics', 'amit.sharma@school.edu', '9876543210', '2018-06-15'),
(2, 'Neha', 'Patel', 'English', 'neha.patel@school.edu', '9876501234', '2019-07-20'),
(3, 'Raj', 'Kumar', 'Physics', 'raj.kumar@school.edu', '9876512345', '2017-03-10'),
(4, 'Divya', 'Joshi', 'Chemistry', 'divya.joshi@school.edu', '9876523456', '2020-11-01'),
(5, 'Suresh', 'Mehta', 'Biology', 'suresh.mehta@school.edu', '9876534567', '2021-02-25');

