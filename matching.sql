ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
flush privileges;
DROP DATABASE IF EXISTS Matching;
CREATE DATABASE IF NOT EXISTS Matching;
USE Matching;
CREATE TABLE IF NOT EXISTS candidate (
			fname VARCHAR(20) NOT NULL, 
            lname VARCHAR(20) NOT NULL,
            email VARCHAR(40) PRIMARY KEY NOT NULL);
            
CREATE TABLE IF NOT EXISTS question (
				questionNum INT NOT NULL,
                answer VARCHAR(1) NOT NULL,
                person VARCHAR(20)	NOT NULL,
                PRIMARY KEY (questionNum, person),
                FOREIGN KEY (person) REFERENCES candidate (email)
                ON DELETE CASCADE ON UPDATE CASCADE);
                
INSERT INTO candidate (fname, lname, email) VALUES
			("richard", "wang",  "johndow@gmail.com");