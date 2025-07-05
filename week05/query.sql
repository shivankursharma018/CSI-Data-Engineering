-- task 1: export sql to csv, avro and parquet
-- creating sql db and table
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Age INT,
    Email NVARCHAR(100)
);

INSERT INTO Students (StudentID, FirstName, LastName, Age, Email)
VALUES 
(1, 'Ishaan', 'Verma', 20, 'ishaan.verma@edu.in'),
(2, 'Megha', 'Rathore', 22, 'megha.rathore123@gmail.com'),
(3, 'Rohit', 'Malik', 21, 'rohitmalik@outlook.com'),
(4, 'Tanvi', 'Desai', 19, 'tanvi.d@icloud.com'),
(5, 'Aarav', 'Jain', 23, 'aarav.jain.1999@yahoo.com'),
(6, 'Nikita', 'Paul', 20, 'nikita.paul@gmail.com'),
(7, 'Siddharth', 'Menon', 24, 'sid.menon@protonmail.com'),
(8, 'Pooja', 'Aggarwal', 22, 'pooja.aggarwal96@rediffmail.com'),
(9, 'Yash', 'Kapoor', 21, 'yash.kapoor@zoho.com'),
(10, 'Simran', 'Gupta', 20, 'simran.gupta24@gmail.com');

-- task 2: schedule based and event based trigger
-- schedule based trigger
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