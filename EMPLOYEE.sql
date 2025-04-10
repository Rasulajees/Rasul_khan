--CREATING TABLE:
CREATE table Student
(
    Name VARCHAR(50),
    Age int,
    Department VARCHAR(50)
)

--DISPLAY TABLE:
SELECT*from Student

--INSERT TABLE VALUES:
INSERT INTO Student
VALUES ('VIJAY',27,'SOFTWARE DEVELOPER')

--UPDATE TABLE VALUSE:
UPDATE Student
SET Age = 25
WHERE Name = 'Mufasa'

--DELETING THE VALUES:
DELETE FROM Student
WHERE Age=15

--DROP DATAS:
drop TABLE Student
