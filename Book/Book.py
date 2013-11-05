import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('books.db')
    db.execue_script('employees.sql')
    db.execue_script('classes.sql')

    print("Print the names and ages of each employee who works in both "
          "Sports and Travel department.")
    comm1 = "SELECT Emp.ename, Emp.age FROM Emp, Works w1, Works w2, Dept d1, Dept d2 "\
            "WHERE Emp.eid = w1.eid AND w1.did = d1.did AND d1.dname = 'Travels' AND " \
            "Emp.eid = w2.eid AND w2.did = d2.did AND d2.dname = 'Sports'"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT Emp.ename, Emp.age FROM Emp, Dept, Works "\
            "WHERE Works.eid = Emp.eid "\
            "AND Works.did = Dept.did " \
            "AND Dept.dname = 'Travels' " \
            "AND Emp.eid IN "\
            "(SELECT Emp.eid FROM Emp, Dept, Works "\
            "WHERE Works.eid = Emp.eid "\
            "AND Works.did = Dept.did " \
            "AND Dept.dname = 'Sports')"
    a = db.query(comm1)
    print(a)

    print("For each department with more than 1 full employees "
          "(where the part-time add up to at least "
          "that many fulltime employees),\n"
          "get Dept did, with the number of employees that "
          "work in that department")
    comm1 = "SELECT Works.did, COUNT(Works.eid) FROM Works "\
            "GROUP BY Works.did "\
            "HAVING 1 < (SELECT SUM(Works.pct_time) FROM Works W "\
            "WHERE W.did = Works.did AND " \
            "Works.pct_time != 1.00)"
    a = db.query(comm1)
    print(a)

    print("Print the name of each employee whose salary exceeds the "
          "budget of all of the departments that he or she works in")
    comm1 = "SELECT Emp.ename, Emp.salary FROM Emp "\
            "WHERE Emp.salary > "\
            "(SELECT Dept.budget FROM Dept, Works "\
            "WHERE Works.did = Dept.did "\
            "AND Works.eid = Emp.eid)"
    a = db.query(comm1)
    print(a)

    print("Select employee names who work in all departments")
    comm1 = "SELECT Emp.ename FROM Emp " \
            "WHERE NOT EXISTS " \
            "(SELECT * FROM Dept " \
            "WHERE NOT EXISTS " \
            "(SELECT * FROM Works " \
            "WHERE Works.did = Dept.did " \
            "AND Emp.eid = Works.eid))"
    a = db.query(comm1)
    print(a)

    print("Find the enames of managers who manage the departments "
          "with the largest budgets.")
    comm1 = "SELECT Emp.ename, Emp.eid, Dept.managerid FROM Emp, Dept " \
            "WHERE Dept.managerid = Emp.eid " \
            "AND Dept.budget = (SELECT MAX(Dept.budget) FROM Dept)"
    a = db.query(comm1)
    print(a)

    print("Find the names of aircraft such that all pilots certified "
          "to operate them earn more than 100.")
    comm1 = "SELECT DISTINCT Aircraft.aname FROM Aircraft, Certified, Employee " \
            "WHERE Aircraft.aid = Certified.aid " \
            "AND Employee.eid = Certified.eid " \
            "AND Employee.salary > 100"
    a = db.query(comm1)
    print(a)

    print("For each pilot who is certified for more than three aircraft,\n"
          "find the eid and the maximum cruisingrange of the aircraft "
          "for which he is certified.")
    comm1 = "SELECT Employee.eid, MAX(Aircraft.crusingrange) " \
            "FROM Employee, Aircraft, Certified " \
            "WHERE Certified.aid = Aircraft.aid " \
            "AND Certified.eid = Employee.eid " \
            "GROUP BY Employee.eid " \
            "HAVING Count(*) > 2"
    a = db.query(comm1)
    print(a)


    print("Find the names of pilots whose salary is less than the price "
          "of the cheapest route from Berlin to Bonn.")
    comm1 = "SELECT Employee.ename FROM Employee " \
            "WHERE Employee.salary < " \
            "(SELECT MIN(Flights.price) FROM Flights " \
            "WHERE Flights.departure = 'Berlin' " \
            "AND Flights.destination = 'Bonn')"
    a = db.query(comm1)
    print(a)

    print("Find the names of pilots certified for some R aircraft.")
    comm1 = "SELECT Employee.ename FROM Employee, Aircraft, Certified "\
            "WHERE Aircraft.aid = Certified.aid "\
            "AND Employee.eid = Certified.eid "\
            "AND Aircraft.aname LIKE 'E%'"
    a = db.query(comm1)
    print(a)

    print("For all aircraft with cruisingrange over 150 miles, "
          "find the name of the aircraft and the average salary of \n"
          "all pilots certified for this aircraft.")
    comm1 = "SELECT Aircraft.aid, Aircraft.aname, AVG(Employee.salary) FROM Employee " \
            "JOIN Certified USING(eid) " \
            "JOIN Aircraft USING(aid) " \
            "WHERE Aircraft.crusingrange > 100 " \
            "GROUP BY Aircraft.aid, Aircraft.aname"
    a = db.query(comm1)
    print(a)

    print("Find the Aircraft aids of all aircraft that can be "
          "used on routes from Los Angeles to Chicago.")
    comm1 = "SELECT Aircraft.aname FROM Aircraft "\
            "WHERE Aircraft.crusingrange > (SELECT distance FROM Flights "\
            "WHERE departure = 'Berlin' "\
            "AND destination = 'Bonn' ) "
    a = db.query(comm1)
    print(a)

    print("Identify the routes that can be piloted by "
          "every pilot who makes more than 100.")
    comm1 = "SELECT DISTINCT Flights.departure, Flights.destination FROM Flights "\
            "WHERE NOT EXISTS "\
            "(SELECT * FROM Employee "\
            "WHERE NOT EXISTS "\
            "(SELECT * FROM Aircraft, Certified "\
            "WHERE Aircraft.crusingrange > Flights.distance "\
            "AND Aircraft.aid = Certified.aid "\
            "AND Employee.eid = Certified.eid))"
    a = db.query(comm1)
    print(a)

    print("Compute the difference between the average salary"
          "of a pilot and the average salary of all pilots.")
    comm1 = "SELECT A.salary - B.avg FROM " \
            "(SELECT Employee.salary FROM Employee " \
            "WHERE Employee.eid IN (SELECT DISTINCT Certified.eid FROM Certified)) AS A, "\
            "(SELECT AVG(Employee.salary) AS avg FROM Employee " \
            "WHERE Employee.eid IN (SELECT DISTINCT Certified.eid FROM Certified)) AS B"
    a = db.query(comm1)
    print(a)

    print("Print the name and salary of every nonpilot "
          "whose salary is more than the average salary for pilots.")
    comm1 = "SELECT Employee.ename, Employee.salary FROM Employee "\
            "WHERE Employee.eid NOT IN (SELECT DISTINCT Certified.eid FROM Certified) "\
            "AND Employee.salary > "\
            "(SELECT AVG(Employee.salary) FROM Employee "\
            "WHERE Employee.eid IN (SELECT DISTINCT Certified.eid FROM Certified))"
    a = db.query(comm1)
    print(a)

    print("Print the names of employees who are certified only on aircrafts "
          "with cruising range longer than 1000 miles")
    comm1 = "SELECT Employee.ename FROM Employee, Certified, Aircraft "\
            "WHERE Certified.aid = Aircraft.aid "\
            "AND Employee.eid = Certified.eid "\
            "GROUP BY Employee.eid, Employee.ename "\
            "HAVING Aircraft.crusingRange > 100"
    a = db.query(comm1)
    print(a)

    print("Print the names of employees who are certified only on aircrafts "
          "with cruising range longer than 1000 miles,\n"
          "but on at least two such aircrafts.")
    comm1 = "SELECT Employee.ename FROM Employee, Certified, Aircraft "\
            "WHERE Certified.aid = Aircraft.aid "\
            "AND Employee.eid = Certified.eid "\
            "GROUP BY Employee.eid, Employee.ename "\
            "HAVING Aircraft.crusingRange > 100 " \
            "AND COUNT(*) > 1"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT * FROM Aircraft " \
            "WHERE NOT EXISTS " \
            "(SELECT * FROM Aircraft " \
            "WHERE Aircraft.aname = NULL)"
    a = db.query(comm1)
    print(a)


    tables = dict()
    tables['Book'] = "CREATE TABLE Book(BookId INTEGER default 0 NOT NULL,"\
                     "Title VARCHAR(50) default '' NOT NULL, "\
                     "PublisherName VARCHAR(50) default '' NOT NULL, "\
                     "PRIMARY KEY(BookId), "\
                     "FOREIGN KEY(PublisherName) REFERENCES Publisher(Name))"

    tables['Publisher'] = "CREATE TABLE Publisher(Name VARCHAR(50), "\
                          "Address VARCHAR(50) default '' NOT NULL, "\
                          "PRIMARY KEY(Name))"


    tables['BookAuthors'] = "CREATE Table BookAuthors (BookId INTEGER default 0 NOT NULL, " \
                            "AuthorName VARCHAR(50) default '' NOT NULL, " \
                            "FOREIGN KEY(BookId) REFERENCES Book(BookId))"

    tables['BookCopies'] = "CREATE Table BookCopies (BookId INTEGER, "\
                            "BranchId INTEGER default 0 NOT NULL, " \
                            "NumCopies INTEGER default 0 NOT NULL, " \
                            "FOREIGN KEY(BookId) REFERENCES Book(BookId), " \
                            "FOREIGN KEY(BranchId) REFERENCES LibraryBranch(BranchId))"

    tables['LibraryBranch'] = "CREATE Table LibraryBranch (BranchId INTEGER, " \
                              "BranchName VARCHAR(50), " \
                              "Adress VARCHAR(50) default '' NOT NULL, " \
                              "PRIMARY KEY(BranchId), " \
                              "FOREIGN KEY(BranchId) REFERENCES BookCopies(BranchId))"

    tables['BookLoans'] = "CREATE Table BookLoans (BookId INTEGER, " \
                          "BranchId INTEGER default 0 NOT NULL, " \
                          "CardNum INTEGER default 0 NOT NULL, " \
                          "DateOut DATE, " \
                          "DateIn DATE, " \
                          "FOREIGN KEY(CardNum) REFERENCES Borrower(CardNum) " \
                          "FOREIGN KEY(BranchId) REFERENCES LibraryBranch(BranchId) " \
                          "FOREIGN KEY(BookId) REFERENCES Book(BookId))"

    tables['Borrower'] = "CREATE Table Borrower (CardNum INTEGER, "\
                          "Name VARCHAR(50) default '' NOT NULL, "\
                          "Address VARCHAR(50) default '' NOT NULL, "\
                          "PRIMARY KEY(CardNum))"

    for skript in tables.values():
        db.execute(skript)

    """
    print("How many copies of the book titled The Lost Tribe "
          "are owned by the library branch whose name is 'Sharpstown'")
    comm1 = "SELECT BookCopies.NumCopies FROM BookCopies, LibraryBranch, Book " \
            "WHERE LibraryBranch.BranchId = BookCopies.BranchId " \
            "AND Book.BookId = BookCopies.BookId " \
            "AND LibraryBranch.BranchName = 'Sharpstown' "\
            "AND Book.Title = 'The Lost Tribe'"
    a = db.query(comm1)
    print(a)

    comm2 = "SELECT BookCopies.NumCopies FROM BookCopies "\
            "JOIN LibraryBranch ON USING(BranchId) "\
            "JOIN Book ON USING(BookId) "\
            "AND LibraryBranch.BranchName = 'Sharpstown' "\
            "AND Book.Title = 'The Lost Tribe'"
    a = db.query(comm1)
    print(a)

    print("How many copies of the book titled The Lost Tribe "
          "are owned by each library branch?")
    comm1 = "SELECT LibraryBranch.BranchName, BookCopies.NumCopies FROM BookCopies, LibraryBranch "\
            "WHERE LibraryBranch.BranchId = BookCopies.BranchId "\
            "AND Book.BookId = BookCopies.BookId "\
            "AND Book.Title = 'The Lost Tribe'"
    a = db.query(comm1)
    print(a)

    print("Retrieve the names of all borrowers who do not have any books checked out.")
    comm1 = "SELECT Borrower.Name FROM Borrower "\
            "WHERE NOT EXIST "\
            "(SELECT * FROM BookLoans "\
            "WHERE BookLoans.CardNum = Borrower.CardNum)"
    a = db.query(comm1)
    print(a)


    comm1 = "SELECT Borrower.Name FROM Borrower "\
            "WHERE Borrower.CardNum NOT IN "\
            "(SELECT BookLoans.CardNum FROM BookLoans)"
    a = db.query(comm1)
    print(a)


    print("For each book that is loaned out from the 'Sharpstown'"
          "branch and whose DueDate is today, retrieve the book title, "
          "the borrower's name, and the borrower's address.")
    comm1 = "SELECT Book.Title, Borrower.Name, Borrower.Address FROM " \
            "Borrower, BookLoans, LibrryBranch " \
            "WHERE BookLoans.CardNum = Borrower.CardNum " \
            "AND BookLoans.BookId = Book.BookId " \
            "AND BookLoans.BranchId = LibrryBranch.BrachId " \
            "AND LibraryBranch.BranchName = 'SharpsTown' " \
            "AND BookLoans.DateOut = 'Today'"
    a = db.query(comm1)
    print(a)

    print("For each library branch, retrieve the branch name"
          "and the total number of books loaned out from that branch.")
    comm1 = "SELECT LibraryBranch.BranchName, COUNT(*) FROM LibraryBranch, BookLoans" \
            "WHERE BookLoans.BranchId = LibraryBranch.BranchId " \
            "GROUP BY LibraryBranch.BranchName"
    a = db.query(comm1)
    print(a)

    print("Retrieve the names, addresses, and number of books checked out "
          "for all borrowers who have more than five books checked out.")
    comm1 = "SELECT Borrower.Name, Borrower.Address, COUNT(*) FROM Borrower, BookLoans" \
            "WHERE BookLoans.CardNum = Borrower.CardNum AND " \
            "GROUP BY Borrower.Name, Borrower.CardNum, Borrower.Address " \
            "HAVING COUNT(*) > 5"
    a = db.query(comm1)
    print(a)

    print("For each book authored (or co-authored) by 'Stephen King', retrieve the title "
          "and the number of copies owned by the library branch whose name is 'Central'")
    comm1 = "SELECT Book.Title, BookCopies.NumCopies FROM "\
            "Book, BookAuthors, LibraryBranch, BookCopies "\
            "WHERE Book.BookId = BookAuthors.BookId "\
            "AND LibraryBranch.BranchId = BookCopies.BranchId "\
            "AND BookAuthors.AuthorName = 'Stephen King'" \
            "AND LibraryBranch.BranchName = 'Central'"
    a = db.query(comm1)
    print(a)

    print("Retrieve the names of employees in department 5 "
          "who work more than 10 hours per week on the 'ProductX' project.")
    comm1 = "SELECT Employee.Name FROM Employee, WorksOn, Project" \
            "WHERE Employee.SSN = WorksOn.ESSN " \
            "AND WorksOn.PNO = Project.Pnumber " \
            "AND Employee.Dnumber = 5" \
            "AND Project.Pname = 'Project X' " \
            "AND WorksOn.Hours > 10"
    a = db.query(comm1)
    print(a)

    print("For each project, list the project name and the "
          "total hours per week (by all employees) spent on that project.")
    comm1 = "SELECT Project.Pname, SUM(HOURS) FROM Project, WorksOn" \
            "WHERE Project.Pnumber = WorksOn.PNO " \
            "GROUP BY Project.Pnumber, Project.Pname"
    a = db.query(comm1)
    print(a)

    print("Retrieve the names of employees who work on every project.")
    comm1 = "SELECT Employee.Name FROM Employee " \
            "WHERE NOT EXISTS " \
            "(SELECT Projects.Pnumber FROM Projects " \
            "WHERE Pnumber NOT IN " \
            "(SELECT PNO FROM WorksOn " \
            "WHERE WorksOn.ESSN = Employee.SSN))"

    comm1 = "SELECT Employee.Name FROM Employee "\
            "WHERE NOT EXISTS "\
            "(SELECT * FROM Projects "\
            "WHERE NOT EXISTS "\
            "(SELECT * FROM WorksOn "\
            "WHERE WorksOn.ESSN = Employee.SSN " \
            "AND Project.Pnumber = WorksOn.PNO))"
    a = db.query(comm1)
    print(a)

    print("Retrieve the names of employees who do not work on any project.")
    comm1 = "SELECT Employee.Name FROM Employee " \
            "WHERE Employee.SSN NOT IN " \
            "(SELECT WorksOn.ESSN FROM WorksOn"

    comm1 = "SELECT Employee.Name FROM Employee "\
            "WHERE NOT EXISTS "\
            "(SELECT WorksOn.ESSN FROM WorksOn" \
            "WHERE Employee.SSN = WorksOn.ESSN"
    a = db.query(comm1)
    print(a)

    print("Find the names and addresses of employees who work on at least one project "
          "located in Houston but whose department has no location in Houston.")
    comm1 = "SELECT Employee.Name, Employee.Address FROM " \
            "Employee, Project, WorksOn " \
            "WHERE Employee.SSN = WorksOn.ESSN " \
            "AND Project.Pnumber = WorksOn.PNO " \
            "AND Project.Plocation IN " \
            "(SELECT Project.Plocation From Project " \
            "WHERE Project.Plocation = 'Houston')" \
            "AND Employee.DNO NOT IN " \
            "(SELECT DepartmentLocation.Dnumber FROM DepartmentLocation " \
            "WHERE DepartmentLocation.Dnumber = <> 'Houston'"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT Employee.Name, Employee.Address FROM Employee"\
            "WHERE EXISTS " \
            "(SELECT * FROM Project, WorksOn " \
            "WHERE Employee.SSN = WorksOn.ESSN " \
            "AND Project.Pnumber = WorksOn.PNO AND " \
            "Project.Plocation = 'Houston') " \
            "AND NOT EXISTS " \
            "(SELECT * FROM DepartmentLocation " \
            "WHERE DepartmentLocation.Dnumber = Employee.DNO " \
            "AND DepartmentLocation.DLocation <> 'Houston')"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT Employee.Name, Employee.Address FROM Employee " \
            "WHERE NOT EXISTS" \
            "(SELCT * FROM Project, WorksOn, DepartmentLocation " \
            "WHERE Project.Pnumber = WorksOn.PNO " \
            "AND Project.Dnumber = DepartmentLocation.DNumber " \
            "AND DepartmentLocation.Location <> 'Houston')"
    a = db.query(comm1)
    print(a)

    print("List the last names of department managers who have no dependents.")
    comm1 = "SELECT Employee.Name FROM Employee, Department " \
            "WHERE Employee.SNN = Department.MGRSSN AND " \
            "Employee.SSN NOT IN " \
            "(SELECT ESSN FROM Dependant)"
    a = db.query(comm1)
    print(a)

    comm1 = "SELECT Employee.Name FROM Employee, Department "\
            "WHERE Employee.SNN = Department.MGRSSN AND "\
            "WHERE NOT EXISTS "\
            "(SELECT * FROM Dependant WHERE Dependant.ESSN = Employee.SSN)"
    a = db.query(comm1)
    print(a)

    print("Find details of those employees whose salary is > the average salary "
          "for all employees. Output salary in descending order.")
    comm1 = "SELECT * FROM Employee " \
            "WHERE Employee.Salary > (SELECT AVG(Employee.Salary) FROM Employee) " \
            "ORDER BY DESC"
    a = db.query(comm1)
    print(a)

    print("Find details of those employees whose salary is > the average salary"
          "for all employees in his/her department. Output salary in ascending order.")
    comm1 = "SELECT * FROM Employee E, " \
            "(SELECT DNO, AVG(SALARY) AS AVGS FROM Employee GROUP BY DNO) AS A "\
            "WHERE E.Salary > AVGS AND " \
            "E.DNO = A.DNO"
    a = db.query(comm1)
    print(a)
    """