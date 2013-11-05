BEGIN TRANSACTION;

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