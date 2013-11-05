import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('test.db')
    db.execue_script('xjadralci.sql')
    comm = "SELECT ime, rating FROM Jadralec j WHERE rating%2=0"
    k = db.query(comm)
    print(k)

    comm = "SELECT c1.ime, c1.cid FROM Coln c1, Coln c2 WHERE c1.ime = c2.ime AND c1.cid != c2.cid"
    k = db.query(comm)
    print(k)

    comm = "SELECT c.ime, c.dolzina, j.starost FROM Coln c " \
           "JOIN Rezervacija r USING(cid) " \
           "JOIN Jadralec j USING(jid) " \
           "WHERE c.dolzina > 35 " \
           "AND j.starost > 35"
    k = db.query(comm)
    print(k)

    comm = "SELECT c.ime, c.dolzina, j.starost FROM Coln c, Rezervacija r, Jadralec j " \
           "WHERE c.cid = r.cid " \
           "AND r.jid = j.jid " \
           "AND c.dolzina > 35 "\
           "AND j.starost > 35"
    k = db.query(comm)
    print(k)

    comm = "SELECT DISTINCT j.ime, r.dan FROM Jadralec j LEFT JOIN Rezervacija r"
    k = db.query(comm)
    print(k)

    comm = "SELECT j.ime, r.dan FROM Jadralec j INNER JOIN Rezervacija r " \
           "WHERE j.jid = r.jid"
    k = db.query(comm)
    print(k)

    comm = "SELECT j1.ime FROM Jadralec j1 " \
           "JOIN Jadralec j2 ON j1.ime = j2.ime "\
           "WHERE j1.jid != j2.jid"
    k = db.query(comm)
    print(k)

    comm = "SELECT c1.ime FROM Coln c1 "\
           "WHERE c1.ime IN " \
           "(SELECT c2.ime FROM Coln c2 " \
           "WHERE c2.cid != c1.cid)"
    k = db.query(comm)
    print(k)

    comm = "SELECT c1.ime FROM Coln c1 "\
           "WHERE c1.ime IN "\
           "(SELECT c2.ime FROM Jadralec j JOIN Rezervacija r ON j.jid = r.jid " \
           "JOIN Coln c2 ON r.cid = c2.cid "\
           "WHERE c2.dolzina > 35 AND j.starost > 35) " \
           "ORDER BY c1.ime DESC"
    k = db.query(comm)
    print(k)

    comm = "SELECT DISTINCT c.ime FROM Coln c " \
           "JOIN Rezervacija r USING(cid) " \
           "WHERE c.dolzina > 35 AND r.jid IN " \
           "(SELECT j.jid FROM Rezervacija r " \
           "JOIN Jadralec j USING(jid) " \
           "WHERE j.starost > 35) " \
           "ORDER BY c.ime DESC"
    k = db.query(comm)
    print(k)

    comm = "SELECT DISTINCT c.ime FROM Coln c " \
           "JOIN Rezervacija r ON r.cid = c.cid " \
           "JOIN Jadralec j ON r.jid = j.jid " \
           "WHERE j.starost > 35 " \
           "AND c.dolzina > 35 " \
           "ORDER BY c.ime DESC"
    k = db.query(comm)
    print(k)

    comm = "SELECT j.*, r.jid, r.dan FROM Rezervacija r " \
           "INNER JOIN Jadralec j ON j.jid = r.jid " \
           "ORDER BY j.jid"
    k = db.query(comm)
    print(k)

    comm = "SELECT * FROM (" \
           "SELECT * FROM Jadralec " \
           "JOIN Rezervacija USING(jid) " \
           "UNION " \
           "SELECT j.*, NULL, NULL " \
           "FROM Jadralec j " \
           "WHERE j.jid NOT IN " \
           "(SELECT jid from jadralec join rezervacija USING(jid)))" \
           "unija order by unija.jid"
    k = db.query(comm)
    print(k)

    comm = "SELECT c.cid, c.ime, COUNT(*) AS stRez FROM Coln c " \
           "JOIN Rezervacija r ON c.cid = r.cid " \
           "GROUP BY c.cid, c.ime " \
           "ORDER BY stRez ASC"
    k = db.query(comm)
    print(k)

    comm = "SELECT c.ime, COUNT(*) AS stRez FROM Coln c "\
           "JOIN Rezervacija r ON c.cid = r.cid "\
           "GROUP BY c.ime "\
           "ORDER BY stRez ASC"
    k = db.query(comm)
    print(k)

    comm = "SELECT j.ime, j.jid, COUNT(r.cid) AS stRez FROM Jadralec j " \
           "LEFT JOIN Rezervacija r ON r.jid = j.jid " \
           "GROUP BY j.jid, j.ime " \
           "ORDER BY stRez DESC"
    k = db.query(comm)
    print(k)

    print("_---------------------------")
    comm = "SELECT j.jid, j.ime, COUNT(r.cid) AS StRez FROM Jadralec j " \
           "LEFT JOIN Rezervacija r USING(jid) " \
           "GROUP BY j.jid, j.ime " \
           "HAVING StRez > " \
           "(SELECT AVG(stRez) " \
           "FROM (SELECT j.jid, j.ime, COUNT(r.cid) AS stRez " \
           "FROM Jadralec j " \
           "LEFT JOIN Rezervacija r USING(jid) " \
           "GROUP BY j.jid, j.ime))"
    k = db.query(comm)
    print(k)

    comm = "SELECT AVG(stRez) FROM (SELECT COUNT(r.cid) AS stRez " \
           "FROM Jadralec j LEFT JOIN Rezervacija r ON r.jid = j.jid " \
           "GROUP BY j.ime, j.jid)"
    k = db.query(comm)
    print(k)

    comm = "SELECT * FROM JADRALEC j WHERE j.starost < 18"
    k = db.query(comm)
    print(k)

    comm = "SELECT c.cid, c.ime, c.dolzina, COUNT(r.cid) AS stRez, COUNT(r.jid) AS stJadralcev, " \
           "AVG(j.rating) " \
           "FROM Coln c " \
           "JOIN Rezervacija r USING(cid) " \
           "JOIN Jadralec j USING(jid)" \
           "GROUP BY r.cid"
    k = db.query(comm)
    print(k)

    a = "(SELECT c.barva FROM Rezervacija r JOIN Coln c ON r.cid = c.cid " \
        "WHERE r.jid = j.jid "\
        "GROUP BY c.barva "\
        "ORDER BY COUNT(*) DESC LIMIT 1) AS Barva"

    comm = "SELECT j.jid, j.ime, COUNT(*), AVG(c.dolzina), " + a + " " \
           "FROM Jadralec j JOIN Rezervacija r USING(jid) JOIN Coln c USING(cid) " \
           "GROUP BY j.jid"
    k = db.query(comm)
    print(k)

    comm = "SELECT DISTINCT j1.ime, j2.ime, j1.rating FROM Jadralec j1, Jadralec j2 " \
           "WHERE j1.rating = j2.rating AND j1.jid < j2.jid " \
           "ORDER BY j1.rating DESC"
    k = db.query(comm)
    print(k)

    comm = "SELECT ime, starost FROM Jadralec WHERE starost = (SELECT MAX(starost) FROM Jadralec)"
    k = db.query(comm)
    print(k)

    comm = "SELECT ime, starost FROM Jadralec WHERE starost = (SELECT MAX(starost) FROM Jadralec)"
    k = db.query(comm)
    print(k)

    comm = "SELECT ime, SUM(starost) FROM Jadralec " \
           "GROUP BY ime"
    k = db.query(comm)
    print(k)

    comm = "SELECT * FROM mm "\
           "WHERE starost < 18"
    k = db.query(comm)
    print(k)


