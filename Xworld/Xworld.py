import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('yworld.db')
    db.execue_script('yworld.sql')
    db.execue_script('wdrop.sql')

    tribes = ["Romans", "Teutons", "Gauls", "Natures", "Natars"]

    tables = dict()
    tables['Tribe'] = "CREATE TABLE Tribe(tid integer default 0 NOT NULL)"

    tables['Alliance'] = "CREATE TABLE Alliance(aid integer default 0 NOT NULL, "\
                        "alliance varchar(100) default '')"

    tables['Player'] = "CREATE TABLE Player(pid integer default 0 NOT NULL, "\
                        "player varchar(100) default '', "\
                        "tid integer default 0 NOT NULL, "\
                        "aid integer default 0 NOT NULL, " \
                        "PRIMARY KEY(pid), "\
                        "FOREIGN KEY(tid) REFERENCES Tribe(tid), "\
                        "FOREIGN KEY(aid) REFERENCES Alliance(aid))"

    tables['Village'] = "CREATE TABLE Village(id integer default 0 NOT NULL, "\
                        "x integer default 0 NOT NULL, "\
                        "y integer default 0 NOT NULL, "\
                        "vid integer default 0 NOT NULL, "\
                        "village varchar(100) default '' NOT NULL, "\
                        "population integer default 0 NOT NULL, "\
                        "pid integer default 0 NOT NULL, "\
                        "PRIMARY KEY(id), "\
                        "FOREIGN KEY(pid) REFERENCES Player(pid))"

    for skript in tables.values():
        db.execute(skript)


    comm1 = "INSERT INTO Tribe(tid) SELECT tid FROM x_world"
    comm2 = "INSERT INTO Alliance(aid, alliance) SELECT " \
            "DISTINCT aid, alliance FROM x_world"
    comm3 = "INSERT INTO Player(pid, player, tid, aid) SELECT " \
            "DISTINCT pid, player, tid, aid FROM x_world"
    comm4 = "INSERT INTO Village(id, x, y, vid, village, population, pid) SELECT " \
            "id, x, y, vid, village, population, pid FROM x_world"

    inserts = [comm1, comm2, comm3, comm4]
    for comm in inserts:
        db.query(comm)

    print("Kateri igralec ima najvecje naselje?")
    comm = "SELECT DISTINCT p.player, v.population FROM Player p " \
           "JOIN Village v USING(pid) " \
           "WHERE v.population = (SELECT MAX(population) FROM Village)"
    a = db.query(comm)
    print(a)

    print("Nadpovprecno veliko naselje")
    comm = "SELECT AVG(population) FROM Village v"
    a = db.query(comm)
    print(a)

    print("Velikost naselj")
    comm = "SELECT p.player, v.village, v.population FROM Player p "\
           "JOIN Village v USING(pid)"
    a = db.query(comm)
    print(a)

    print("Izpisite podatke o vseh naseljih igralcev brez alianse, "
          "urejeno padajoce po x in nato y koordinati.")
    comm = "SELECT DISTINCT v.village, v.x, v.y FROM Village v " \
           "JOIN Player p ON v.pid = p.pid " \
           "JOIN Alliance a ON p.aid = a.aid " \
           "WHERE a.alliance = '' " \
           "ORDER BY v.x DESC"
    a = db.query(comm)
    print a

    print("Katera plemena so najstevilcnejsa glede na populacijo padajaoce?")
    comm = "SELECT p.tid, SUM(v.population) FROM Village v " \
           "JOIN Player p USING(pid) " \
           "GROUP BY p.tid " \
           "ORDER BY v.population ASC"
    a = db.query(comm)
    print a

    print("Katere alinse so najstevilcnejsa glede na populacijo padajaoce?")
    comm = "SELECT a.aid, a.alliance, SUM(v.population) FROM Village v "\
           "JOIN Player p USING(pid) " \
           "JOIN Alliance a USING(aid) " \
           "WHERE a.alliance != '' "\
           "GROUP BY p.aid "\
           "ORDER BY v.population ASC"
    a = db.query(comm)
    print a

    print("Kater igralci so najstevilcnejsi glede na populacijo padajaoce?")
    comm = "SELECT p.pid, p.player, SUM(v.population) FROM Village v "\
           "JOIN Player p USING(pid) "\
           "GROUP BY p.pid "\
           "ORDER BY v.population ASC"
    a = db.query(comm)
    print a

    print("Izpisite imena igralcev, ki imajo vsa svoja naselja na obmocju x, "
          "ki je med 100 in 200 in y, ki je med 0 in 100")
    comm = "SELECT DISTINCT p.player FROM Village v "\
           "JOIN Player p USING(pid) " \
           "WHERE p.player IN " \
           "(SELECT p.player FROM Village v " \
           "JOIN Player p USING(pid) " \
           "WHERE (100 < x < 200) AND (0 < y < 100))"
    a = db.query(comm)
    print a

    print("Kateri igralci imajo nadpovprecno veliko naselje")
    comm = "SELECT p.player FROM Player p "\
           "JOIN Village v USING(pid) "\
           "GROUP BY p.player "\
           "HAVING v.population > (SELECT AVG(population) FROM Village v)"
    a = db.query(comm)
    print(a)

    print("Koliko igralcev ima nadpovprecno veliko naselje")
    comm = "SELECT COUNT(*) FROM "\
           "(SELECT p.player FROM Player p "\
           "JOIN Village v USING(pid) "\
           "GROUP BY p.player "\
           "HAVING v.population > (SELECT AVG(population) FROM Village v))"
    a = db.query(comm)
    print(a)

    print("Kateri igralci imajo samo nadpovprecno velika naselja")
    comm = "SELECT DISTINCT player FROM Player "\
           "JOIN Village v USING (pid) "\
           "WHERE player NOT IN "\
           "(SELECT player FROM Player pp "\
           "JOIN Village vv USING(pid) "\
           "WHERE vv.population < (SELECT AVG(population) FROM Village))"
    a = db.query(comm)
    print(a)

    print("x min, y min, x max, y max")
    comm = "SELECT MIN(x), MAX(x), MIN(y), MAX(y) FROM Village"
    minimumx = db.query(comm)
    print(minimumx)

    comm = "CREATE VIEW XView AS " \
           "SELECT v.id, v.x, v.y, t.tid, v.vid, v.village, p.pid, p.player, a.aid, a.alliance, v.population "\
           "FROM Village v, Player p, Alliance a, Tribe t"
    k = db.query(comm)

    print("presek, unija, count")
    comm = "SELECT * FROM x_world WHERE NOT EXISTS (SELECT * FROM XView)"
    k = db.query(comm)
    print(k)

    print("unija")
    comm = "SELECT * FROM x_world WHERE EXISTS (SELECT * FROM XView)"
    k = db.query(comm)
    print(k)

    comm = "SELECT COUNT(*) FROM (SELECT * FROM x_world WHERE EXISTS (SELECT * FROM XView))"
    k = db.query(comm)
    print(k)

    print("populacija igralca, stevilo naselij igralca")
    comm = "SELECT player, v.population FROM Player p " \
           "JOIN Village v USING(pid) " \
           "WHERE v.population > " \
           "(SELECT AVG(v.population)/100 FROM Player p "\
           "JOIN Village v USING(pid) "\
           "GROUP BY p.pid)"
    k = db.query(comm)
    print(k)