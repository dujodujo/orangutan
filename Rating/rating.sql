/* Delete the tables if they already exist */
drop table if exists Movie;
drop table if exists Reviewer;
drop table if exists Rating;

drop view if exists NoRating;
drop view if exists HighlyRated;
drop view if exists LateRating;

/* Create the schema for our tables */
create table Movie(mID int, title text, year int, director text);
create table Reviewer(rID int, name text);
create table Rating(rID int, mID int, stars int, ratingDate date);

/* Populate the tables with our data */
insert into Movie values(101, 'Gone with the Wind', 1939, 'Victor Fleming');
insert into Movie values(102, 'Star Wars', 1977, 'George Lucas');
insert into Movie values(103, 'The Sound of Music', 1965, 'Robert Wise');
insert into Movie values(104, 'E.T.', 1982, 'Steven Spielberg');
insert into Movie values(105, 'Titanic', 1997, 'James Cameron');
insert into Movie values(106, 'Snow White', 1937, null);
insert into Movie values(107, 'Avatar', 2009, 'James Cameron');
insert into Movie values(108, 'Raiders of the Lost Ark', 1981, 'Steven Spielberg');

insert into Reviewer values(201, 'Sarah Martinez');
insert into Reviewer values(202, 'Daniel Lewis');
insert into Reviewer values(203, 'Brittany Harris');
insert into Reviewer values(204, 'Mike Anderson');
insert into Reviewer values(205, 'Chris Jackson');
insert into Reviewer values(206, 'Elizabeth Thomas');
insert into Reviewer values(207, 'James Cameron');
insert into Reviewer values(208, 'Ashley White');

insert into Rating values(201, 101, 2, '2011-01-22');
insert into Rating values(201, 101, 4, '2011-01-27');
insert into Rating values(202, 106, 4, null);
insert into Rating values(203, 103, 2, '2011-01-20');
insert into Rating values(203, 108, 4, '2011-01-12');
insert into Rating values(203, 108, 2, '2011-01-30');
insert into Rating values(204, 101, 3, '2011-01-09');
insert into Rating values(205, 103, 3, '2011-01-27');
insert into Rating values(205, 104, 2, '2011-01-22');
insert into Rating values(205, 108, 4, null);
insert into Rating values(206, 107, 3, '2011-01-15');
insert into Rating values(206, 106, 5, '2011-01-19');
insert into Rating values(207, 107, 5, '2011-01-20');
insert into Rating values(208, 104, 3, '2011-01-02');

create view LateRating as
  select distinct R.mID, title, stars, ratingDate
  from Rating R, Movie M
  where R.mID = M.mID
  and ratingDate > '2011-01-20';

create view HighlyRated as
  select mID, title
  from Movie
  where mID in (select mID from Rating where stars > 3);

create view NoRating as
  select mID, title
  from Movie
  where mID not in (select mID from Rating);

/**
Write an instead-of trigger that enables updates
to the title attribute of view LateRating.
Policy: Updates to attribute title in LateRating should update
Movie.title for the corresponding movie.
*/
CREATE TRIGGER UpdateTitle
INSTEAD OF UPDATE OF title ON LateRating
FOR EACH ROW
BEGIN
  UPDATE MOVIE
  SET title = New.title
  WHERE mID = New.mID;
END;

/**
Write an instead-of trigger that enables updates to the mID
attribute of view LateRating.
*/
CREATE TRIGGER UpdateStars
INSTEAD OF UPDATE OF stars ON LateRating
FOR EACH ROW
BEGIN
  UPDATE Rating
  SET stars = New.stars
  WHERE mID = New.mID
  AND ratingDate = New.ratingDate;
END;

CREATE TRIGGER UpdateMID
INSTEAD OF UPDATE OF mID ON LateRating
FOR EACH ROW
BEGIN
  UPDATE Movie SET mID = New.mID WHERE mID = Old.mID;
  UPDATE Rating SET mID = New.mID WHERE mID = Old.mID;
END;

/**
"Finally, write a single instead-of trigger that combines all "
"three of the previous triggers to enable simultaneous updates "
"to attributes mID, title, and/or stars in view LateRating. "
"Combine the view-update policies of the three previous problems, "
"with the exception that mID may now be updated. "
"Make sure the ratingDate attribute of view LateRating "
"has not also been updated -- "
"if it has been updated, don't make any changes."
*/
CREATE TRIGGER InsteadAllUpdate
INSTEAD OF UPDATE OF mID, stars, title ON LateRating
FOR EACH ROW
when New.ratingDate = Old.ratingDate
BEGIN
  UPDATE Movie SET title = New.title WHERE mID = Old.mID;
  UPDATE Rating SET stars = New.stars WHERE ratingDate = Old.ratingDate AND mID = Old.mID;
  UPDATE Movie SET title = New.title WHERE mID = Old.mID;
  UPDATE Rating SET mID = New.mID WHERE mID = Old.mID;
END;

/**
Write an instead-of trigger that enables deletions from view HighlyRated.
Deletions from view HighlyRated should delete all ratings for
the corresponding movie that have stars > 3.
*/
CREATE TRIGGER InsteadDeleteFromHigh
INSTEAD OF DELETE ON HighlyRated
FOR EACH ROW
BEGIN
  DELETE FROM Rating WHERE mID = Old.mID AND stars > 3;
END;

/**
Write an instead-of trigger that enables deletions from view HighlyRated.
Deletions from view HighlyRated should update all ratings for the
corresponding movie that have stars > 3 so they have stars = 3.
*/
CREATE TRIGGER InsteadDeleteFromHighly
INSTEAD OF DELETE ON HighlyRated
FOR EACH ROW
BEGIN
  UPDATE Rating SET stars = 3 WHERE mID = Old.mID AND stars > 3;
END;

/**
Write an instead-of trigger that enables insertions into view HighlyRated.
An insertion should be accepted only when the (mID,title) pair already exists
in the Movie table. (Otherwise, do nothing.) Insertions into view HighlyRated
should add a new rating for the inserted movie with rID = 201, stars = 5,
and NULL ratingDate.
*/
CREATE TRIGGER InsteadOfInsertHighly
INSTEAD OF INSERT ON HighlyRated
FOR EACH ROW
WHEN EXISTS (SELECT * FROM Movie WHERE mID = New.mID AND title = New.title)
BEGIN
  INSERT INTO Rating(rID, mID, title) values (201, New.mID, 5);
END;

/**
Write an instead-of trigger that enables insertions into view NoRating.
An insertion should be accepted only when the (mID,title) pair already
exists in the Movie table. (Otherwise, do nothing.)
Insertions into view NoRating should delete all ratings for the
corresponding movie.
*/
CREATE TRIGGER InsteadInsertNoRating
INSTEAD OF INSERT ON NoRating
FOR EACH ROW
WHEN EXISTS (SELECT * FROM Movie WHERE mID = New.mID AND title = New.title)
BEGIN
  DELETE FROM Rating WHERE mID = New.mID;
END;

/**
Write an instead-of trigger that enables deletions
from view NoRating. Deletions from view NoRating
should delete the corresponding movie from the Movie table.
*/
CREATE TRIGGER InsteadDeletionNoRating
INSTEAD OF DELETE ON NoRating
FOR EACH ROW
BEGIN
  DELETE FROM Movie WHERE mID = Old.mID;
END;

/**
Write an instead-of trigger that enables deletions from view NoRating.
Deletions from view NoRating should add a new rating for the deleted
movie with rID = 201, stars = 1, and NULL ratingDate.
*/
CREATE TRIGGER Inss
INSTEAD OF DELETE ON NoRating
FOR EACH ROW
BEGIN
  INSERT INTO Rating(rID, mID, stars) values(201, Old.mID, 1, NULL);
END;