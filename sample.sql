CREATE TABLE Students (
    ID INT PRIMARY KEY IDENTITY(11201,1),
    Name VARCHAR(100),
    Age INT,
    Grade VARCHAR(5),
    
)
INSERT INTO Students
VALUES ('YUVA', 20, 'A')

SELECT*FROM Students

ALTER TABLE Students
ADD SALARY VARCHAR(10)

INSERT INTO Students (Name,Age,Grade)
VALUES ('Alice', 20, 'A',10000)

TRUNCATE TABLE Students

DROP TABLE Students