import sqlite3
from Db import Db

if __name__ == '__main__':
    db = Db('test.db')
    db.execue_script('xjadralci.sql')

    comm = 'SELECT ime FROM Jadralec WHERE rating % 2 = 0'
    even = db.query(comm)
    print(even)

    comm = 'SELECT ime FROM Jadralec WHERE rating % 2 != 0'
    odd = db.query(comm)
    print(odd)

    comm = 'SELECT * FROM Coln c1, Coln c2 WHERE (c1.ime = c2.ime) AND (c1.cid != c2.cid)'
    equal_name = db.query(comm)
    print(equal_name)

    comm = 'SELECT * FROM Coln c JOIN Rezervacija r USING(cid) JOIN Jadralec j' \
           ' USING(jid) WHERE c.dolzina>35 and j.starost<35'
    boat_name = db.query(comm)
    print(boat_name)

    comm1 = 'SELECT DISTINCT j.ime, r.dan FROM Jadralec j LEFT JOIN Rezervacija r USING(jid)' \
           'WHERE r.dan NOT NULL'
    comm2 = 'SELECT DISTINCT j.ime, r.dan FROM Jadralec j LEFT JOIN Rezervacija r USING(jid)'
    reservations1 = db.query(comm1)
    reservations2 = db.query(comm2)
    print(reservations1)
    print(reservations2)

    comm = 'SELECT j1.ime FROM Jadralec j1 JOIN Jadralec j2 USING(ime) WHERE j1.jid!=j2.jid'
    sailor_equl_names = db.query(comm)
    print(sailor_equl_names)

    comm = "SELECT j.ime FROM Coln c JOIN Rezervacija r USING(cid)" \
           "JOIN Jadralec j USING(jid) WHERE c.ime like '%Sun%'"
    fixed = db.query(comm)
    print(fixed)

    comm = "SELECT * FROM Jadralec j WHERE EXISTS " \
           "(SELECT * FROM Rezervacija rr, Coln c " \
           "WHERE j.jid = rr.jid AND " \
           "rr.cid = c.cid " \
           "AND c.ime = 'Bavaria')"
    a = db.query(comm)
    print(a)

    comm = "SELECT c.cid FROM Coln c, Rezervacija r, Jadralec j " \
           "WHERE c.cid = r.cid AND r.jid = j.jid " \
           "AND j.ime = 'Darko' " \
           "INTERSECT " \
           "SELECT c.cid FROM Coln c, Rezervacija r, Jadralec j " \
           "WHERE c.cid = r.cid AND r.jid = j.jid " \
           "AND j.ime = 'Lojze' "
    a = db.query(comm)
    print(a)

    comm = "SELECT ime FROM Jadralec j WHERE jid NOT IN " \
           "(SELECT jid FROM Rezervacija WHERE cid IN " \
           "(SELECT cid FROM Coln WHERE barva = 'rdeca'))"
    a = db.query(comm)
    print(a)

    comm = "SELECT c1.ime FROM Coln c1 WHERE ime IN " \
           "(SELECT c2.ime FROM Coln c2 WHERE c1.cid != c2.cid)"
    a = db.query(comm)
    print(a)

    comm = "SELECT c.ime FROM coln c JOIN Rezervacija r USING(cid) " \
           "WHERE c.dolzina > 35 and r.jid IN " \
           "(SELECT j.jid FROM rezervacija r JOIN Jadralec j USING(jid) " \
           "WHERE j.starost < 40)"
    a = db.query(comm)
    print(a)

    comm = "SELECT * FROM JADRALEC LEFT JOIN REZERVACIJA r USING(jid) " \
           "WHERE r.dan NOT NULL ORDER BY jid"
    a = db.query(comm)
    print(a)


    comm3 = "SELECT * FROM Jadralec j LEFT JOIN Rezervacija USING(jid)"
    a = db.query(comm)
    print(a)


    coms = "SELECT * from (SELECT * FROM Jadralec JOIN Rezervacija USING(jid) " \
           "UNION SELECT j.*, NULL, NULL FROM Jadralec j WHERE j.jid NOT IN " \
           "(SELECT jid FROM Jadralec JOIN Rezervacija USING(jid))) " \
           "unija order by unija.jid"
    a = db.query(coms)
    print(a)

    comm = "SELECT c.cid, c.ime, count(*) AS stRez FROM Coln c JOIN Rezervacija r USING(cid) " \
           "GROUP BY c.cid, c.ime " \
           "ORDER BY stRez DESC"
    a = db.query(comm)
    print(a)

    comm = "SELECT j.jid, j.ime, count(r.cid) AS stRez FROM Jadralec j LEFT JOIN Rezervacija r USING(jid) "\
           "GROUP BY j.jid, j.ime "\
           "ORDER BY stRez DESC, j.ime ASC"
    a = db.query(comm)
    print(a)