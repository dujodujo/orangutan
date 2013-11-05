import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('classes.db')
    db.execue_script('classes.sql')

    print("Find all students who took a class in California "
          "from an instructor not in the student's major department and "
          "got a score over 80. Return the student name, university, and score.")
    comm1 = "SELECT DISTINCT Student.name, Class.univ, Took.score " \
            "FROM Student, Class, Took, Instructor " \
            "WHERE Student.studID = Took.studID " \
            "AND Instructor.instID = Took.instID " \
            "AND Class.classID = Took.classID " \
            "AND Student.major != Instructor.dept " \
            "AND Took.score >= 80 " \
            "AND Class.region = 'CA'"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT DISTINCT Student.name, Class.univ, Took.score FROM Student "\
            "JOIN Took ON Student.studID = Took.studID "\
            "JOIN Instructor ON Instructor.instID = Took.instID "\
            "JOIN Class ON Class.classID = Took.classID "\
            "WHERE Student.major != Instructor.dept "\
            "AND Took.score >= 80 "\
            "AND Class.region = 'CA'"
    a = db.query(comm1)
    print(a)

    print("Find average scores grouped by student and instructor "
          "for courses taught in Quebec.")
    comm1 = "SELECT Instructor.instID, Student.studID, AVG(Took.score) " \
            "FROM Student "\
            "JOIN Took ON Student.studID = Took.studID "\
            "JOIN Instructor ON Instructor.instID = Took.instID "\
            "JOIN Class ON Class.classID = Took.classID "\
            "WHERE Class.region = 'Quebec' "\
            "GROUP BY Instructor.instID, Student.studID " \
            "ORDER BY Student.studID"
    a = db.query(comm1)
    print(a)

    print("Find average scores grouped by student and instructor "
          "for courses taught in Quebec.")
    comm1 = "SELECT Instructor.instID, AVG(Took.score) "\
            "FROM Student "\
            "JOIN Took ON Student.studID = Took.studID "\
            "JOIN Instructor ON Instructor.instID = Took.instID "\
            "JOIN Class ON Class.classID = Took.classID "\
            "WHERE Class.region = 'Quebec' "\
            "GROUP BY Instructor.instID "\
            "ORDER BY Instructor.instID"
    a = db.query(comm1)
    print(a)

    print("Find average scores grouped by student major.")
    comm1 = "SELECT Student.major, AVG(Took.score) FROM Student "\
            "JOIN Took ON Student.studID = Took.studID "\
            "JOIN Instructor ON Instructor.instID = Took.instID "\
            "JOIN Class ON Class.classID = Took.classID "\
            "GROUP BY Student.major"
    a = db.query(comm1)
    print(a)

    print("Drill down on your result from problem 4 so it's grouping by "
          "instructor's department as well as student's major.")
    print("Find average scores grouped by student major.")
    comm1 = "SELECT Instructor.dept, Student.major, AVG(Took.score) FROM Student "\
            "JOIN Took ON Student.studID = Took.studID "\
            "JOIN Instructor ON Instructor.instID = Took.instID "\
            "JOIN Class ON Class.classID = Took.classID "\
            "GROUP BY Instructor.dept, Student.major"
    a = db.query(comm1)
    print(a)