DROP CREATE DATABASE RASUL
 USE Dummy

CREATE TABLE Company
(
    Employee_id varchar (50),
    Employee_name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
)

INSERT INTO Company
VALUES ('abc123','Arun','Python_developer',25000),
        ('abc456','Deva','Testing',35000),
        ('abc','Kalai','HR',40000)

ALTER TABLE Company
ADD In_hand INT

UPDATE Company
SET In_hand =39300
WHERE Employee_name= 'Kalai'


SELECT*FROM Company