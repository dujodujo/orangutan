BEGIN TRANSACTION;

DROP TABLE IF EXISTS Jadralec;
DROP VIEW IF EXISTS mladina;

CREATE TABLE Jadralec ( jid INTEGER, ime VARCHAR(10), rating INTEGER, starost REAL,
                       PRIMARY KEY (jid),
                       CHECK ( rating >= 1 AND rating <= 10 ));

insert into Jadralec
       values( 22, 'Darko', 7, 45.0);
insert into Jadralec
       values( 29, 'Borut',  1, 33.0);
insert into Jadralec
       values( 31, 'Lojze',  8, 55.5);
insert into Jadralec
       values( 32, 'Andrej',  8, 25.5);
insert into Jadralec
       values( 58, 'Rajko',  10, 35.0);
insert into Jadralec
       values( 64, 'Henrik',  7, 35.0);
insert into Jadralec
       values( 71, 'Zdravko',  10, 16.0);
insert into Jadralec
       values( 74, 'Henrik',  9, 35.0);
insert into Jadralec
       values( 85, 'Anze', 3, 25.5);
insert into Jadralec
       values( 95, 'Bine', 3, 63.5);

DROP TABLE IF EXISTS Coln;

CREATE TABLE Coln ( cid INTEGER, ime VARCHAR(20), dolzina INTEGER, barva VARCHAR(10),
                    primary key (cid),
                    CHECK ( dolzina >= 1 AND dolzina <= 60 ));

insert into Coln
       values( 101, 'Elan', 34, 'modra');
insert into Coln
       values( 102, 'Elan', 34, 'rdeca');
insert into Coln
       values( 103, 'Sun Odyssey', 37, 'zelena');
insert into Coln
       values( 104, 'Bavaria', 50, 'rdeca');

DROP TABLE IF EXISTS Rezervacija;

CREATE TABLE Rezervacija ( jid INTEGER, cid INTEGER, dan DATE,
       PRIMARY KEY (jid, cid, dan),
       FOREIGN KEY (jid) REFERENCES Jadralec(jid),
       FOREIGN KEY (cid) REFERENCES Coln(cid));

insert into Rezervacija
       values ( 22, 101, DATE('2006-10-10'));
insert into Rezervacija
       values ( 22, 102, DATE('2006-10-10'));
insert into Rezervacija
       values ( 22, 103, DATE('2006-10-8'));
insert into Rezervacija
       values ( 22, 104, DATE('2006-10-7'));
insert into Rezervacija
       values ( 31, 102, DATE('2006-11-10'));
insert into Rezervacija
       values ( 31, 103, DATE('2006-11-6'));
insert into Rezervacija
       values ( 31, 104, DATE('2006-11-12'));
insert into Rezervacija
       values ( 64, 101, DATE('2006-9-5'));
insert into Rezervacija
       values ( 64, 102, DATE('2006-9-8'));
insert into Rezervacija
       values ( 74, 103, DATE('2006-9-8'));

COMMIT;
