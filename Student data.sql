CREATE DATABASE Teacher
USE Teacher

CREATE TABLE Student(
Name VARCHAR(50),
Department VARCHAR(50),
Marks_scored int,
)
--SELECT * FROM Student
ALTER TABLE Student 
 ADD City VARCHAR(50)

ALTER TABLE Student
 DROP Department

SELECT*FROM Student