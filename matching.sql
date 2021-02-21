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
                answer VARCHAR(20) NOT NULL,
                person VARCHAR(20)	NOT NULL,
                PRIMARY KEY (questionNum, person),
                FOREIGN KEY (person) REFERENCES candidate (email)
                ON DELETE CASCADE ON UPDATE CASCADE);
                
INSERT INTO candidate (fname, lname, email) VALUES
			("richard", "wang",  "johndow@gmail.com");

INSERT INTO candidate (fname, lname, email) VALUES
			("qw", "ew",  "qw");

select * from candidate where email="abc";
select exists(select * from candidate where email="ab");


/*
INSERT INTO candidate (fname, lname, email) VALUES
            ("rick", "morty",  "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (1, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (2, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (3, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (4, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (5, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (6, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (7, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (8, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (9, "A", "dow@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (10, "A", "dow@gmail.com");

INSERT INTO candidate (fname, lname, email) VALUES
            ("wood", "wood",  "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (1, "A", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (2, "B", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (3, "C", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (4, "D", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (5, "A", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (6, "B", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (7, "C", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (8, "D", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (9, "A", "wood@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (10, "B", "wood@gmail.com");

INSERT INTO candidate (fname, lname, email) VALUES
            ("wood", "wood",  "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (1, "A", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (2, "A", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (3, "A", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (4, "A", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (5, "A", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (6, "B", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (7, "C", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (8, "D", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (9, "D", "person@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (10, "B", "person@gmail.com");
-- half A 2
INSERT INTO candidate (fname, lname, email) VALUES
            ("wood", "doow",  "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (1, "B", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (2, "B", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (3, "B", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (4, "B", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (5, "B", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (6, "B", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (7, "A", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (8, "A", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (9, "A", "gmail@gmail.com");
INSERT INTO question (questionNum, answer, person) VALUES
            (10, "A", "gmail@gmail.com");

*/
SELECT * FROM candidate