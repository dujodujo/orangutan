BEGIN TRANSACTION;

DROP TABLE IF EXISTS Jadralec;

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

COMMIT;
