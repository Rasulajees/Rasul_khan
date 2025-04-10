--Define the database name:
USE Dummy

--Create table:  
CREATE TABLE Customer
(
    Customer_id VARCHAR(50),
    Customer_name VARCHAR(50),
    Customer_address VARCHAR(100),
    City VARCHAR(50),
    States VARCHAR (50),
    Pin_code INT
)

--Insert table values:
INSERT INTO Customer 
VALUES(20121201131,'Rasul khan','1/799, Pakkirimedu st, motchakulam',  'Villupuram', 'Tamil nadu',605105),
      (20121201132,'Ramesh','6900 Main street','San francisco','CA',94032),
      (20121201133,'Vignesh','2040 Riverside Rd','San diego','CA',92010),
      (20121201134,'Renesh','4010 speedway','Tucson','AZ',85719)

INSERT INTO Customer
VALUES(20121201135,'Kamu','329 Sunset Blvd','New York','NT',10059,'555-123-4567')

--ALTER TABLE Customer add -- Add a new column 'NewColumnName' to table 'TableName' in schema 'SchemaName'
    ALTER TABLE Customer
    ADD Mobile_number VARCHAR(10)

--update customer values:
UPDATE Customer
 SET Mobile_number = '6935824710'
 WHERE Customer_name= 'Renesh'

UPDATE Customer
 SET Mobile_number = '1234567890'
 WHERE Customer_name= 'Rasul khan'

UPDATE Customer
 SET Mobile_number = '0987456321'
 WHERE Customer_name= 'Ramesh'

UPDATE Customer
 SET Mobile_number = '0123456789'
 WHERE Customer_name= 'Vignesh'

UPDATE Customer
 SET States = 'Kerala'
 WHERE Customer_name = 'Renesh'

UPDATE Customer
 SET States = 'Goa'
 WHERE Customer_name = 'Vignesh'

UPDATE Customer
 SET States = 'Goa'
 WHERE Customer_name = 'Vignesh'

--Alter table column name:
SELECT Customer_id,Customer_name,Customer_address AS Address,City,States,Pin_code,Mobile_number
FROM Customer

--View table:
SELECT* FROM Customer

--Deleting table:
DROP TABLE Customer

--Deleting column:
ALTER TABLE Customer DROP COLUMN Mobile_number