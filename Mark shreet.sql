--Database name:
USE Dummy

--Creating Table:
CREATE TABLE Mark_sheet
(
    Roll_no INT PRIMARY KEY IDENTITY(12001,1),
    Name VARCHAR(50),
    Class VARCHAR(10),
    Tamil INT,
    English INT,
    Maths INT,
    Science INT,
    Social_Science INT,
);

--View table:
SELECT* from Mark_sheet

--Inset values in the table:
INSERT INTO Mark_sheet
VALUES('Ajay','12th',54,38,73,87,69),
      ('Bala','12th',69,87,76,54,31),
      ('kadhir','12th',44,87,65,51,97),
      ('Yuvaraar','12th',)


SELECT SUM (Tamil) AS Total_mark
FROM Mark_sheet

--Delete table:
DROP TABLE Mark_sheet