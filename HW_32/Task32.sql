-- Active: 1713108237529@@127.0.0.1@3306@it_step_db
create DATABASE if NOT EXISTS it_step_db;

#დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE Table Author(
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT
)


#2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE Table Books(
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    BookName VARCHAR(50) NOT NULL,
    Foreign Key (AuthorID) REFERENCES Author(AuthorID)
)

#3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO author(`FirstName`,`LastName`)
VALUES
("Mikheil","Javaxishvili"),
("Shota","Rustaveli"),
("Iakob","Gogebashvili"),
("Ilia","Chavchavadze"),
("Vaja","Fshavela")

INSERT INTO books(`AuthorID`,`BookName`) 
VALUES
("1","Jayos Xiznebi") ,
("2","Vefxistyaosani"),
("3","Deda Ena"),
("4","Kacia Adamiani?"),
("5","Aluda Qetelauri")

#4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE books
SET `BookName` = "Otaraant Qvrivi"
Where `AuthorID` = 4;

#5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
DELETE TABLE AuthorID;
Delete TABLE BookName;
Delete TABLE FirstName;
Delete TABLE LastName;

#6. წაშალეთ Author და Books ცხრილები
DROP TABLE books,
DROP TABLE author;