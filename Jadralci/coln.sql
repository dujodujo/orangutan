BEGIN TRANSACTION;

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

COMMIT;