import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('rating.db')
    db.execue_script('rating.sql')

    comm1 = "SELECT Movie.title FROM Movie WHERE director = 'Steven Spielberg'"
    a = db.query(comm1)
    print(a)

    print("2. Find all years that have a movie that received a rating of 4 or 5 "
          "and sort them in increasing order.")
    comm1 = "SELECT DISTINCT Movie.year FROM Movie, Rating " \
            "WHERE Movie.mID = Rating.mID " \
            "AND Rating.stars >= 4 " \
            "ORDER BY Movie.year ASC"
    a = db.query(comm1)
    print(a)

    print("3. Find the titles of all movies that have no ratings.")
    comm1 = "SELECT Movie.title FROM Movie " \
            "WHERE NOT EXISTS "\
            "(SELECT * FROM Rating "\
            "WHERE Movie.mID = Rating.mID)"
    a = db.query(comm1)
    print(a)

    print("4. Some reviewers didn't provide a date with their rating. "
          "Find the names of all reviewers who have "
          "ratings with a NULL value for the date.")
    comm1 = "SELECT DISTINCT Reviewer.name FROM Reviewer, Rating " \
            "WHERE Reviewer.rID = Rating.rID " \
            "AND Rating.rID IN "\
            "(SELECT Rating.rID FROM Rating "\
            "WHERE Rating.ratingDate IS NULL)"
    a = db.query(comm1)

    print(a)
    comm1 = "SELECT DISTINCT Reviewer.name FROM Reviewer "\
            "JOIN Rating ON Rating.rID = Reviewer.rID "\
            "WHERE Rating.rID " \
            "AND Rating.ratingDate IS NULL"
    a = db.query(comm1)
    print(a)

    print("5. Write a query to return the ratings data in "
          "a more readable format: reviewer name, movie title, stars, and ratingDate.\n"
          "Also, sort the data, first by reviewer name, "
          "then by movie title, and lastly by number of stars.")
    comm1 = "SELECT Reviewer.name, Movie.title, Rating.stars, Rating.ratingDate " \
            "FROM Movie " \
            "JOIN Rating USING(mID) " \
            "JOIN Reviewer USING(rID) " \
            "GROUP BY Reviewer.name, Movie.title, Rating.stars"
    a = db.query(comm1)
    print(a)

    print("6. For all cases where the same reviewer rated the same movie "
          "twice and gave it a higher rating the second time, \n"
          "return the reviewer's name and the title of the movie.")
    comm1 = "SELECT Reviewer.name, Movie.title " \
            "FROM Movie, Rating t1, Rating t2, Reviewer " \
            "WHERE Movie.mID = t1.mID " \
            "AND t1.rID = t2.rID " \
            "AND t1.mID = t2.mID " \
            "AND t1.rID = Reviewer.rID " \
            "AND t1.stars < t2.stars " \
            "AND t1.ratingDate < t2.ratingDate"
    a = db.query(comm1)
    print(a)

    print("7. For each movie that has at least one rating,"
          "find the highest number of stars that movie received. \n"
          "Return the movie title and number of stars. Sort by movie title.")
    comm1 = "SELECT Movie.title, MAX(Rating.stars) FROM Reviewer, Movie, Rating "\
            "WHERE Movie.mID = Rating.mID "\
            "AND Rating.rID = Reviewer.rID "\
            "GROUP BY Movie.mID "\
            "HAVING COUNT(*) > 1 " \
            "ORDER BY Movie.title"
    a = db.query(comm1)
    print(a)

    print("8. For each movie, return the title and the 'rating spread', "
          "that is, the difference between highest and lowest ratings given \n"
          "to that movie. Sort by rating spread from highest to lowest, "
          "then by movie title.")
    comm1 = "SELECT Movie.title, MAX(Rating.stars)-Min(Rating.stars) AS spread " \
            "FROM Reviewer, Movie, Rating "\
            "WHERE Movie.mID = Rating.mID "\
            "AND Rating.rID = Reviewer.rID "\
            "GROUP BY Movie.mID "\
            "HAVING COUNT(*) > 0 "\
            "ORDER BY spread DESC, Movie.title"
    a = db.query(comm1)
    print(a)

    print("9. Find the difference between the average rating of movies "
          "released before 1980 and the average rating of movies released after 1980. \n"
          "(Make sure to calculate the average rating for each movie, "
          "then the average of those averages for movies before 1980 and movies after.\n"
          "Don't just calculate the overall average rating before and after 1980.")

    comm1 = "SELECT AVG(B.bb)-AVG(A.aa) FROM " \
            "(SELECT AVG(Rating.stars) AS aa FROM Movie "\
            "JOIN Rating ON Rating.mID = Movie.mID "\
            "GROUP BY Movie.mID " \
            "HAVING Movie.year > 1980) A, " \
            "(SELECT AVG(Rating.stars) AS bb FROM Movie "\
            "JOIN Rating ON Rating.mID = Movie.mID "\
            "GROUP BY Movie.mID " \
            "HAVING Movie.year < 1980) B"
    a = db.query(comm1)
    print(a)

    print("2.1 Find the names of all reviewers who rated Gone with the Wind.")
    comm1 = "SELECT DISTINCT Reviewer.name FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) " \
            "WHERE Movie.title = 'Gone with the Wind'"
    a = db.query(comm1)
    print(a)

    print("2.2 For any rating where the reviewer is the same as the director of the movie, "
          "return the reviewer name, movie title, and number of stars.")
    comm1 = "SELECT DISTINCT Reviewer.name, Movie.title, Rating.stars FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "WHERE Movie.director = Reviewer.name"
    a = db.query(comm1)
    print(a)

    print("2.3 Return all reviewer names and movie names "
          "together in a single list, alphabetized.")
    comm1 = "SELECT Reviewer.name + Movie.title FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID)"
    a = db.query(comm1)
    print(a)

    print("2.4 Find the titles of all movies not reviewed by Chris Jackson.")
    comm1 = "SELECT Movie.title FROM Movie " \
            "EXCEPT " \
            "SELECT Movie.title FROM Movie " \
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) " \
            "WHERE Reviewer.name = 'Chris Jackson'"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT Movie.title FROM Movie "\
            "WHERE Movie.title NOT IN "\
            "(SELECT Movie.title FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "WHERE Reviewer.name = 'Chris Jackson')"
    a = db.query(comm1)
    print(a)

    print("2.5 For all pairs of reviewers such that both reviewers "
          "gave a rating to the same movie, return the names of both reviewers. \n"
          "Eliminate duplicates, don't pair reviewers with themselves, "
          "and include each pair only once. For each pair, return the names "
          "in the pair in alphabetical order.")
    comm1 = ""
    a = db.query(comm1)
    print(a)

    print("2.6 For each rating that is the lowest (fewest stars) currently in the database,"
          "return the reviewer name, movie title, and number of stars.")
    comm1 = "SELECT Reviewer.name, Movie.title, Rating.stars " \
            "FROM Reviewer, Movie, Rating "\
            "WHERE Movie.mID = Rating.mID "\
            "AND Rating.rID = Reviewer.rID " \
            "AND Rating.stars = (SELECT MIN(Rating.stars) FROM Rating)"\
            "GROUP BY Movie.mID " \
            "ORDER BY Movie.title"
    a = db.query(comm1)
    print(a)

    print("2.7 List movie titles and average ratings, "
          "from highest-rated to lowest-rated. "
          "If two or more movies have the same average rating, "
          "list them in alphabetical order.")
    comm1 = "SELECT Movie.title, AVG(Rating.stars) FROM Movie " \
            "JOIN Rating USING(mID) " \
            "GROUP BY Movie.mID " \
            "ORDER BY Avg(Rating.stars) DESC, Movie.title ASC"
    a = db.query(comm1)
    print(a)

    print("2.8 Find the names of all reviewers who have contributed "
          "three or more ratings.")
    comm1 = "SELECT Reviewer.name FROM Reviewer "\
            "JOIN Rating USING(rID) " \
            "JOIN Movie USING(mID) " \
            "GROUP BY Reviewer.rID " \
            "HAVING COUNT(*) > 2"
    a = db.query(comm1)
    print(a)

    print("2.9 Some directors directed more than one movie."
          "For all such directors, return the titles of all movies \n"
          "directed by them, along with the director name. "
          "Sort by director name, then movie title.")
    comm1 = "SELECT Movie.title, Movie.director FROM Movie "\
            "WHERE Movie.director IN "\
            "(SELECT M.director FROM Movie M "\
            "GROUP BY M.director " \
            "HAVING COUNT(*) > 1) " \
            "ORDER BY Movie.director DESC, Movie.title"
    a = db.query(comm1)
    print(a)

    print("2.10 Find the movie with the highest average rating. "
          "Return the movie title(s) and average rating.")
    comm1 = "SELECT Movie.title AS t, AVG(Rating.stars) AS ars FROM Movie " \
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "GROUP BY Movie.title " \
            "ORDER BY ars DESC LIMIT 1"
    a = db.query(comm1)
    print(a)


    print("2.11 Find the movie with the lowest average rating. "
          "Return the movie title(s) and average rating.")
    comm1 = "SELECT Movie.title, AVG(Rating.stars) FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "GROUP BY Movie.title "\
            "HAVING AVG(Rating.stars) = " \
            "(SELECT MAX(M.A) FROM " \
            "(SELECT AVG(Rating.stars) AS A FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "GROUP BY Movie.title) AS M)"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT Movie.title, AVG(Rating.stars) FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "GROUP BY Movie.title "\
            "HAVING AVG(Rating.stars) = "\
            "(SELECT MIN(M.A) FROM "\
            "(SELECT AVG(Rating.stars) AS A FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) "\
            "GROUP BY Movie.title) AS M)"
    a = db.query(comm1)
    print(a)

    print("2.12 For each director, return the director's name together with "
          "the title(s) of the movie(s) they directed that received the \n"
          "highest rating among all of their movies, and the value of that rating."
          "Ignore movies whose director is NULL.")
    comm1 = "SELECT Movie.director, Movie.title, MAX(Rating.stars) FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) " \
            "GROUP BY Movie.director " \
            "HAVING Movie.director IN "\
            "(SELECT Movie.director FROM Movie "\
            "JOIN Rating USING(mID) "\
            "JOIN Reviewer USING(rID) " \
            "WHERE Movie.director IS NOT NULL)"
    a = db.query(comm1)
    print(a)

    comm1 = "INSERT INTO Reviewer values(209, 'Roger Ebert')"
    a = db.query(comm1)

    comm1 = "INSERT INTO Rating (rID, mID, stars) " \
            "SELECT (SELECT rID FROM Reviewer WHERE name='James Cameron'), M.mID = 5, 5 " \
            "FROM Movie AS M"

    comm1 = "UPDATE Movie " \
            "SET year = year + 25 " \
            "WHERE Movie.mID IN " \
            "(SELECT Movie.mID FROM Movie, Rating " \
            "WHERE Movie.mID = Rating.mID " \
            "GROUP BY Movie.mID " \
            "HAVING AVG(Rating.stars) >= 4)"

    print("Remove all ratings where the movie's year is before "
          "1970 or after 2000, and the rating is fewer than 4 stars.")
    comm1 = "update movie " \
            "set " \
            "year = year + 25 " \
            "where mid in " \
            "(select M.mid from movie as M, rating as R " \
            "where M.mid = R.mid " \
            "group by M.mid " \
            "having avg(stars) >= 4)"