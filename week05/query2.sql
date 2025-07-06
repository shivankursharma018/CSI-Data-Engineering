-- task 2: schedule based and event based trigger
-- schedule based trigger (at 5 minutes gap)
INSERT INTO Students (StudentID, FirstName, LastName, Age, Email)
VALUES 
(11, 'Ananya', 'Sharma', 22, 'ananya.sharma@edu.in'),
(12, 'Karan', 'Mehta', 23, 'karan.mehta1999@gmail.com'),
(13, 'Divya', 'Iyer', 21, 'divya.iyer@outlook.com'),
(14, 'Rajat', 'Bansal', 20, 'rajat.bansal@icloud.com'),
(15, 'Sneha', 'Patel', 24, 'sneha.patel@protonmail.com');

-- event based trigger (file arrival)
-- remove last 5 lines from input/csv/data2.csv
-- run event trigger, new changes made to input/parquet/data2.parquet