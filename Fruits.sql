use Dummy
CREATE TABLE Fruits(
Name varchar(50),
Price int
)

INSERT INTO Fruits
VALUES('APPLE',150),
      ('BANANA',50),
      ('CHERRY',60),
      ('DROGEN FRUIT',100),
      ('EGG FRUIT',95)

UPDATE Fruits
 SET Price= 120
 WHERE Price= 150

UPDATE Fruits
 SET Name='MANGO'
 WHERE Name='BANANA'
 
SELECT*FROM Fruits