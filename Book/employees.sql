BEGIN TRANSACTION;

DROP TABLE IF EXISTS Emp;
DROP TABLE IF EXISTS Works;
DROP TABLE IF EXISTS Dept;

DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Flights;
DROP TABLE IF EXISTS Certified;
DROP TABLE IF EXISTS Aircraft;

DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Publisher;
DROP TABLE IF EXISTS BookAuthors;
DROP TABLE IF EXISTS BookCopies;
DROP TABLE IF EXISTS LibraryBranch;
DROP TABLE IF EXISTS BookLoans;
DROP TABLE IF EXISTS Borrower;

CREATE TABLE Emp (
      eid INT NOT NULL,
      ename VARCHAR(255) NOT NULL,
      age INT NOT NULL,
      salary REAL NOT NULL,
      PRIMARY KEY (eid));

INSERT INTO Emp(eid, ename, age, salary) VALUES (1, 'John', 14, 10);
INSERT INTO Emp(eid, ename, age, salary) VALUES (2, 'Erik', 14, 10);
INSERT INTO Emp(eid, ename, age, salary) VALUES (3, 'Butters', 12, 10);
INSERT INTO Emp(eid, ename, age, salary) VALUES (4, 'Stan', 13, 4);
INSERT INTO Emp(eid, ename, age, salary) VALUES (5, 'Kyle', 13, 4);
INSERT INTO Emp(eid, ename, age, salary) VALUES (6, 'Token', 13, 4);
INSERT INTO Emp(eid, ename, age, salary) VALUES (7, 'Marsh', 13, 4);
INSERT INTO Emp(eid, ename, age, salary) VALUES (8, 'Larry', 13, 4);
INSERT INTO Emp(eid, ename, age, salary) VALUES (9, 'Marry', 13, 10);

CREATE TABLE Dept (
      did INT NOT NULL,
      dname VARCHAR(255) NOT NULL,
      budget REAL NOT NULL,
      managerid INT,
      PRIMARY KEY (did));

INSERT INTO Dept (did, dname, budget, managerid) VALUES (1, 'Sports', 5, 5);
INSERT INTO Dept (did, dname, budget, managerid) VALUES (2, 'Travels', 6, 1);
INSERT INTO Dept (did, dname, budget, managerid) VALUES (3, 'Foods', 6, 2);
INSERT INTO Dept (did, dname, budget, managerid) VALUES (4, 'Guns', 3, 1);
INSERT INTO Dept (did, dname, budget, managerid) VALUES (5, 'Clothes', 3, 5);

CREATE TABLE Works (
      eid INT NOT NULL,
      did INT NOT NULL,
      pct_time INT,
      PRIMARY KEY (eid, did),
      FOREIGN KEY (did) REFERENCES Dept(did),
      FOREIGN KEY (eid) REFERENCES Emp(eid));

INSERT INTO Works (eid, did, pct_time) VALUES (1, 1, 0.20);
INSERT INTO Works (eid, did, pct_time) VALUES (1, 2, 0.20);
INSERT INTO Works (eid, did, pct_time) VALUES (1, 3, 0.20);
INSERT INTO Works (eid, did, pct_time) VALUES (1, 4, 0.20);
INSERT INTO Works (eid, did, pct_time) VALUES (1, 5, 0.20);
INSERT INTO Works (eid, did, pct_time) VALUES (2, 1, 0.90);
INSERT INTO Works (eid, did, pct_time) VALUES (2, 2, 0.10);
INSERT INTO Works (eid, did, pct_time) VALUES (3, 1, 1.00);
INSERT INTO Works (eid, did, pct_time) VALUES (4, 1, 1.00);
INSERT INTO Works (eid, did, pct_time) VALUES (5, 3, 1.00);
INSERT INTO Works (eid, did, pct_time) VALUES (6, 3, 1.00);
INSERT INTO Works (eid, did, pct_time) VALUES (7, 3, 0.60);
INSERT INTO Works (eid, did, pct_time) VALUES (7, 1, 0.40);
INSERT INTO Works (eid, did, pct_time) VALUES (8, 3, 0.60);
INSERT INTO Works (eid, did, pct_time) VALUES (8, 1, 0.40);
INSERT INTO Works (eid, did, pct_time) VALUES (9, 3, 0.70);
INSERT INTO Works (eid, did, pct_time) VALUES (9, 1, 0.30);

CREATE TABLE Flights (
      flno INT NOT NULL,
      departure VARCHAR(255) NOT NULL,
      destination VARCHAR(255) NOT NULL,
      distance INT NOT NULL,
      departs INT NOT NULL,
      arrives INT NOT NULL,
      price INT NOT NULL,
      PRIMARY KEY (flno));

INSERT INTO Flights (flno, departure, destination,
distance, departs, arrives, price)
VALUES (1, 'Berlin', 'Bonn', 100, 10, 12, 200);
INSERT INTO Flights (flno, departure, destination,
distance, departs, arrives, price)
VALUES (2, 'Berlin', 'Bonn', 100, 10, 12, 300);
INSERT INTO Flights (flno, departure, destination,
distance, departs, arrives, price)
VALUES (3, 'Frankfurt', 'Bonn', 100, 12, 14, 250);
INSERT INTO Flights (flno, departure, destination,
distance, departs, arrives, price)
VALUES (4, 'London', 'Manchester', 100, 6, 10, 350);
INSERT INTO Flights (flno, departure, destination,
distance, departs, arrives, price)
VALUES (5, 'Amsterdam', 'Helsinki', 400, 8, 10, 150);

CREATE TABLE Aircraft (
      aid INT,
      aname VARCHAR(255) NOT NULL,
      crusingrange INT NOT NULL,
      PRIMARY KEY (aid));

INSERT INTO Aircraft (aid, aname, crusingrange) VALUES (1, 'Ryan Air', 200);
INSERT INTO Aircraft (aid, aname, crusingrange) VALUES (2, 'Easy Jet', 200);
INSERT INTO Aircraft (aid, aname, crusingrange) VALUES (3, 'Wizz Air', 350);
INSERT INTO Aircraft (aid, aname, crusingrange) VALUES (4, 'Wings', 250);

CREATE TABLE Employee (
      eid INT NOT NULL,
      ename VARCHAR(255) NOT NULL,
      salary INT NOT NULL,
      PRIMARY KEY (eid));

INSERT INTO Employee (eid, ename, salary) VALUES (1, 'Heinrich', 250);
INSERT INTO Employee (eid, ename, salary) VALUES (2, 'Thurim', 120);
INSERT INTO Employee (eid, ename, salary) VALUES (3, 'Otto', 210);
INSERT INTO Employee (eid, ename, salary) VALUES (4, 'Frank', 150);
INSERT INTO Employee (eid, ename, salary) VALUES (5, 'Siegfried', 300);
INSERT INTO Employee (eid, ename, salary) VALUES (6, 'Manfred', 340);
INSERT INTO Employee (eid, ename, salary) VALUES (7, 'Noll', 400);

CREATE TABLE Certified (
      eid INT NOT NULL,
      aid INT NOT NULL,
      FOREIGN KEY (aid) REFERENCES Aircraft(aid),
      FOREIGN KEY (eid) REFERENCES Employee(eid));

INSERT INTO Certified (eid, aid) VALUES (1, 1);
INSERT INTO Certified (eid, aid) VALUES (1, 2);
INSERT INTO Certified (eid, aid) VALUES (1, 3);
INSERT INTO Certified (eid, aid) VALUES (1, 4);
INSERT INTO Certified (eid, aid) VALUES (2, 1);
INSERT INTO Certified (eid, aid) VALUES (2, 2);
INSERT INTO Certified (eid, aid) VALUES (2, 3);
INSERT INTO Certified (eid, aid) VALUES (3, 1);
INSERT INTO Certified (eid, aid) VALUES (3, 2);
INSERT INTO Certified (eid, aid) VALUES (3, 3);
INSERT INTO Certified (eid, aid) VALUES (3, 4);
INSERT INTO Certified (eid, aid) VALUES (4, 1);
INSERT INTO Certified (eid, aid) VALUES (5, 1);

Commit;