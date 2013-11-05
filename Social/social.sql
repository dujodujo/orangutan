/* Delete the tables if they already exist */
drop table if exists Highschooler;
drop table if exists Friend;
drop table if exists Likes;

/* Create the schema for our tables */
create table Highschooler(ID int, name text, grade int);
create table Friend(ID1 int, ID2 int);
create table Likes(ID1 int, ID2 int);

/* Populate the tables with our data */
insert into Highschooler values (1510, 'Jordan', 9);
insert into Highschooler values (1689, 'Gabriel', 9);
insert into Highschooler values (1381, 'Tiffany', 9);
insert into Highschooler values (1709, 'Cassandra', 9);
insert into Highschooler values (1101, 'Haley', 10);
insert into Highschooler values (1782, 'Andrew', 10);
insert into Highschooler values (1468, 'Kris', 10);
insert into Highschooler values (1641, 'Brittany', 10);
insert into Highschooler values (1247, 'Alexis', 11);
insert into Highschooler values (1316, 'Austin', 11);
insert into Highschooler values (1911, 'Gabriel', 11);
insert into Highschooler values (1501, 'Jessica', 11);
insert into Highschooler values (1304, 'Jordan', 12);
insert into Highschooler values (1025, 'John', 12);
insert into Highschooler values (1934, 'Kyle', 12);
insert into Highschooler values (1661, 'Logan', 12);

insert into Friend values (1510, 1381);
insert into Friend values (1510, 1689);
insert into Friend values (1689, 1709);
insert into Friend values (1381, 1247);
insert into Friend values (1709, 1247);
insert into Friend values (1689, 1782);
insert into Friend values (1782, 1468);
insert into Friend values (1782, 1316);
insert into Friend values (1782, 1304);
insert into Friend values (1468, 1101);
insert into Friend values (1468, 1641);
insert into Friend values (1101, 1641);
insert into Friend values (1247, 1911);
insert into Friend values (1247, 1501);
insert into Friend values (1911, 1501);
insert into Friend values (1501, 1934);
insert into Friend values (1316, 1934);
insert into Friend values (1934, 1304);
insert into Friend values (1304, 1661);
insert into Friend values (1661, 1025);
insert into Friend select ID2, ID1 from Friend;

insert into Likes values(1689, 1709);
insert into Likes values(1709, 1689);
insert into Likes values(1782, 1709);
insert into Likes values(1911, 1247);
insert into Likes values(1247, 1468);
insert into Likes values(1641, 1468);
insert into Likes values(1316, 1304);
insert into Likes values(1501, 1934);
insert into Likes values(1934, 1501);
insert into Likes values(1025, 1101);

/**
Write a trigger that makes new students named 'Friendly'
automatically like everyone else in their grade.
That is, after the trigger runs, we should have
('Friendly', A) in the Likes table for every
other Highschooler A in the same grade as 'Friendly'.
*/
CREATE TRIGGER Friendly
AFTER INSERT ON Highschooler
FOR EACH ROW
WHEN (New.name = 'Friendly')
BEGIN
  INSERT INTO Likes SELECT New.ID, Highschooler.ID FROM Highschooler
  WHERE New.grade = Highschooler.grade
  AND New.ID <> Highschooler.ID;
END;

/**
Write one or more triggers to manage the grade attribute of new Highschoolers.
If the inserted tuple has a value less than 9 or greater than 12,
change the value to NULL. On the other hand, if the inserted tuple
has a null value for grade, change it to 9.
*/
CREATE TRIGGER Grading1
AFTER INSERT ON Highschooler
FOR EACH ROW
WHEN (9 < New.grade OR New.grade > 12)
BEGIN
  UPDATE Highschooler
  SET grade = NULL
  WHERE ID = New.ID;
END;

CREATE TRIGGER Grading2
AFTER INSERT ON Highschooler
FOR EACH ROW
WHEN (New.grade = NULL)
BEGIN
  UPDATE Highschooler
  SET grade = 9
  WHERE ID = New.ID;
END;

CREATE TRIGGER Symetry1
AFTER INSERT ON Friend
FOR EACH ROW
WHEN NOT EXISTS (SELECT * FROM Friend WHERE Friend.ID1 = New.ID2 AND Friend.ID2 = New.ID1)
BEGIN
  INSERT INTO Friend values (New.ID2, New.ID1);
END;

/**
Write one or more triggers to maintain symmetry
in friend relationships. Specifically, if (A,B)
is deleted from Friend, then (B,A) should be deleted too.
If (A,B) is inserted into Friend then (B,A)
should be inserted too. Don't worry
about updates to the Friend table.
*/
CREATE TRIGGER Symetry2
AFTER DELETE ON Friend
FOR EACH ROW
WHEN EXISTS (SELECT * FROM Friend WHERE Friend.ID1 = Old.ID2 AND Friend.ID2 = Old.ID1)
BEGIN
  DELETE FROM Friend WHERE Friend.ID1 = Old.ID2 AND Friend.ID2 = Old.ID1;
END;

/**
Write a trigger that automatically deletes
students when they graduate, i.e.,
when their grade is updated to exceed 12.
*/
CREATE TRIGGER Grading
AFTER UPDATE ON Highschooler
FOR EACH ROW
WHEN (New.grade >= 12)
BEGIN
  DELETE FROM Highschooler WHERE New.ID = ID;
END;

/**
Write a trigger that automatically deletes students when they
graduate, i.e., when their grade is updated to exceed
12 (same as Question 4). In addition, write a trigger so
when a student is moved ahead one grade,
then so are all of his or her friends.
*/
CREATE TRIGGER Graduation
AFTER UPDATE ON Highschooler
FOR EACH ROW
WHEN (New.grade = Old.grade + 1)
BEGIN
  UPDATE Highschooler
  SET grade = grade + 1
  WHERE ID IN (SELECT DISTINCT ID2 FROM Friend WHERE Friend.ID1 = New.ID);
END;

/**
Write a trigger to enforce the following behavior:
If A liked B but is updated to A liking C instead,
and B and C were friends, make B and C no longer friends.
Don't forget to delete the friendship in both directions,
and make sure the trigger only runs when the liked (ID2)
person is changed but the liking
(ID1) person is not changed.
*/
CREATE TRIGGER Friendship
AFTER UPDATE OF ID2 ON Likes
FOR EACH ROW
WHEN (Old.ID1 = New.ID1 AND EXISTS
(SELECT * FROM Friend WHERE ID1 = Old.ID2 AND ID2 = New.ID1))
BEGIN
  DELETE FROM Friend
  WHERE (ID1=Old.ID2 and ID2=New.ID2) or (ID1=New.ID2 and ID2=Old.ID2);
END;