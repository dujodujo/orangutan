import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('social.db')
    db.execue_script('social.sql')

    print("1 Find the names of all students who are friends with someone named Gabriel.")
    comm1 = "SELECT Highschooler.name FROM Highschooler " \
            "WHERE Highschooler.ID IN " \
            "(SELECT Friend.ID2 FROM Highschooler, Friend " \
            "WHERE Highschooler.ID = Friend.ID1 " \
            "AND Highschooler.name = 'Gabriel')"
    a = db.query(comm1)
    print(a)

    print("2. For every student who likes someone 2 or more "
          "grades younger than themselves, \n"
          "return that student's name and grade, \n"
          "and the name and grade of the student they like.")
    comm1 = "SELECT (SELECT name FROM HighSchooler, Likes "\
            "WHERE HighSchooler.ID = L.ID1), "\
            "(SELECT grade from HighSchooler, Likes "\
            "WHERE HighSchooler.ID = L.ID1), "\
            "name, grade "\
            "FROM HighSchooler H, Likes L "\
            "WHERE H.ID = L.ID2 and H.grade + 2 <= "\
            "(SELECT grade from HighSchooler  "\
            "WHERE HighSchooler.ID=L.ID1)"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT H1.name, H1.grade, H2.name, H2.grade "\
            "FROM Highschooler H1, Highschooler H2, Likes L " \
            "WHERE L.ID1 = H1.ID AND L.ID2 = H2.ID AND H1.grade >= H2.grade + 2"
    a = db.query(comm1)
    print(a)

    print("3 For every pair of students who both like each other,"
          "return the name and grade of both students. \n"
          "Include each pair only once, with the two names in alphabetical order.")
    comm1 = "SELECT H1.name, H1.grade, H2.name, H2.grade FROM " \
            "(SELECT L.ID1, L.ID2 FROM Likes AS L " \
            "WHERE EXISTS (SELECT * FROM Likes L1 WHERE L.ID1 = L1.ID1 AND L.ID2 = L1.ID2)) AS R, " \
            "Highschooler H1, " \
            "Highschooler H2 " \
            "WHERE H1.ID = R.ID1 " \
            "AND H2.ID = R.ID2 " \
            "AND H1.name > H2.name"
    a = db.query(comm1)
    print(a)

    print("4 Find all students who do not appear in the Likes table "
          "as a student who likes or is liked and return their \n"
          "names and grades. Sort by grade, then by name within each grade.")
    comm1 = "SELECT Highschooler.name, Highschooler.grade FROM Highschooler "\
            "WHERE Highschooler.ID NOT IN " \
            "(SELECT Likes.ID1 FROM Likes) " \
            "AND Highschooler.ID NOT IN " \
            "(SELECT Likes.ID2 FROM Likes) " \
            "ORDER BY Highschooler.grade, Highschooler.name"
    a = db.query(comm1)
    print(a)

    print("5. For every situation where student A likes student B,"
          "but we have no information about whom B likes \n"
          "(that is, B does not appear as an ID1 in the Likes table),"
          "return A and B's names and grades.")
    comm1 = "SELECT (SELECT name FROM HighSchooler, Likes "\
            "WHERE HighSchooler.ID = L.ID1), "\
            "(SELECT grade from HighSchooler, Likes "\
            "WHERE HighSchooler.ID = L.ID1), "\
            "name, grade "\
            "FROM HighSchooler H, Likes L "\
            "WHERE H.ID = L.ID2 " \
            "AND L.ID2 NOT IN " \
            "(SELECT L.ID1 FROM Likes L)"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT (SELECT name FROM HighSchooler, Likes "\
            "WHERE HighSchooler.ID = L.ID1), "\
            "(SELECT grade from HighSchooler, Likes "\
            "WHERE HighSchooler.ID = L.ID1), "\
            "name, grade "\
            "FROM HighSchooler H, Likes L "\
            "WHERE H.ID = L.ID2 "
    a = db.query(comm1)
    print(a)

    print("6 Find names and grades of students who only have "
          "friends in the same grade. Return the result "
          "sorted by grade, then by name within each grade.")
    comm1 = "SELECT DISTINCT H1.name, H1.grade " \
            "FROM Friend F, Highschooler H1, Highschooler H2 " \
            "WHERE H1.ID = F.ID1 " \
            "AND H2.ID = F.ID2 " \
            "AND H1.grade = H2.grade " \
            "AND NOT EXISTS (SELECT * FROM Friend F1 WHERE H1.ID = F1.ID1 " \
            "AND H1.grade <> (SELECT grade FROM Highschooler WHERE ID = F1.ID2)) " \
            "ORDER BY H1.name"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT DISTINCT H1.name, H1.grade "\
            "FROM Friend F, Highschooler H1, Highschooler H2 "\
            "WHERE NOT EXISTS (SELECT * FROM Friend F1 WHERE H1.ID = F1.ID1 "\
            "AND H1.grade <> (SELECT grade FROM Highschooler WHERE ID = F1.ID2)) "\
            "ORDER BY H1.name"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT DISTINCT H1.name, H1.grade FROM Highschooler H1 " \
            "WHERE NOT EXISTS " \
            "(SELECT * FROM Friend F1 WHERE H1.ID = F1.ID1 " \
            "AND H1.grade <> (SELECT grade FROM Highschooler H2 WHERE H2.ID = F1.ID2)) " \
            "ORDER BY H1.name"
    a = db.query(comm1)
    print(a)

    print("8. Find the difference between the number of students"
          "in the school and the number of different first names.")
    comm1 = "SELECT COUNT(*) - " \
            "(SELECT COUNT(*) FROM " \
            "(SELECT DISTINCT Highschooler.name " \
            "FROM Highschooler)) " \
            "FROM Highschooler "
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT DISTINCT " \
            "(SELECT COUNT(H.ID) FROM Highschooler H) " \
            " - "\
            "(SELECT COUNT(DISTINCT Highschooler.name) FROM Highschooler)"\
            "FROM Likes "
    a = db.query(comm1)
    print(a)

    print("9 Find the name and grade of all students "
          "who are liked by more than one other student")
    comm1 = "SELECT H.name, H.grade FROM " \
            "(SELECT L.ID2 FROM Likes AS L " \
            "GROUP BY L.ID2 " \
            "HAVING COUNT(L.ID1) > 1) R, Highschooler H " \
            "WHERE H.ID = R.ID2"
    a = db.query(comm1)
    print(a)