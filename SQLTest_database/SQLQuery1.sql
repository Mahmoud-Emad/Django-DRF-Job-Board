USE MASTER;
GO
/* DROP DATABASE "Target" */
/* create database */
CREATE DATABASE "Target"
on
(
name = target,
/* filename = 'target.mdf',*/
size = 10,
maxsize = 50,
filegrowth = 5
)
/* Create tables */
USE Target;
GO
/* Create Country Table */
CREATE TABLE Country
(
id INT IDENTITY(1,1),
title VARCHAR(30),

PRIMARY KEY (id),
)
/* Create City Table */
CREATE TABLE City
(
id INT IDENTITY(1,1),
title VARCHAR(30),

PRIMARY KEY (id),
)

/* Create Locations Table */
CREATE TABLE Locations
(
id INT IDENTITY(1,1),
country INT,
city INT

PRIMARY KEY (id),
FOREIGN KEY (country) REFERENCES Country(id),
FOREIGN KEY (city) REFERENCES City(id)
)

/* Create User Table */
CREATE TABLE "Users"
(
id INT IDENTITY(1,1),
first_name NCHAR(15) NOT NULL,
last_name NCHAR(15) NOT NULL,
email VARCHAR(30) NOT NULL,
password NCHAR(30) NOT NULL,
phone VARCHAR(15),
location INT,

PRIMARY KEY (id),
FOREIGN KEY (location) REFERENCES Locations(id)
)

/* Create Employer Table */
CREATE TABLE Employer
(
id INT IDENTITY(1,1),
first_name NCHAR(15) NOT NULL,
last_name NCHAR(15) NOT NULL,
company_name VARCHAR(30) NOT NULL,
company_size INT NOT NULL,
location INT,

PRIMARY KEY (id),
FOREIGN KEY (location) REFERENCES Locations(id)
)

/* Create User Jobs */
CREATE TABLE Jobs
(
id INT IDENTITY(1,1),
company INT,
location INT,
title VARCHAR(60) NOT NULL,
experience INT NOT NULL,
job_type VARCHAR(10) NOT NULL CHECK (job_type IN('part time', 'full time', 'freelance'))

PRIMARY KEY (id),
FOREIGN KEY (company) REFERENCES Employer(id),
FOREIGN KEY (location) REFERENCES Locations(id)
)