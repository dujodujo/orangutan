BEGIN TRANSACTION;

DROP TABLE IF EXISTS x_world;

CREATE TABLE x_world(
  id integer default 0 NOT NULL,
  x integer default 0 NOT NULL,
  y integer default 0 NOT NULL,
  tid integer default 0 NOT NULL,
  vid integer default 0 NOT NULL,
  village varchar(100) default '' NOT NULL,
  pid integer default 0 NOT NULL,
  player varchar(100) default '' NOT NULL,
  aid integer default 0,
  alliance varchar(100) default '',
  population integer default 0 NOT NULL,
  PRIMARY KEY (id)
);
-- Insert
INSERT INTO x_world VALUES (99,-302,400,3,40187,'Isengard 02',11675,'Uruk Hai',0,'',249);
INSERT INTO x_world VALUES (385,-16,400,3,48614,'Wizard 06',3110,'Wizarder',947,'-=FB=-',298);
INSERT INTO x_world VALUES (399,-2,400,3,51021,'Wizard 08',3110,'Wizarder',947,'-=FB=-',202);
INSERT INTO x_world VALUES (400,-1,400,3,22823,'Wizard 01',3110,'Wizarder',947,'-=FB=-',1099);
INSERT INTO x_world VALUES (401,0,400,3,19903,'Rosea 01',8922,'grammostola rcf',1397,'WOLVES®',641);
INSERT INTO x_world VALUES (402,1,400,3,50826,'Wizard 07',3110,'Wizarder',947,'-=FB=-',227);
INSERT INTO x_world VALUES (417,16,400,1,46003,'Sky',9220,'skyhawk',2943,'LoL',297);
INSERT INTO x_world VALUES (440,39,400,3,53769,'13 adiddas',1402,'lenart',154,'MGPA',39);
INSERT INTO x_world VALUES (441,40,400,3,24649,'11 Pedro',1402,'lenart',154,'MGPA',569);
INSERT INTO x_world VALUES (744,343,400,3,24075,'1.AAA 343/400',8833,'RESET.me',2458,'Pax™',911);
INSERT INTO x_world VALUES (796,395,400,3,40629,'[7] JoKER',3274,'zuzi',2458,'Pax™',308);
INSERT INTO x_world VALUES (808,-394,399,3,36210,'[6] JoKER',3274,'zuzi',2458,'Pax™',501);
INSERT INTO x_world VALUES (1201,-1,399,3,52737,'Wizard 10',3110,'Wizarder',947,'-=FB=-',74);
INSERT INTO x_world VALUES (1202,0,399,3,51257,'Wizard 09',3110,'Wizarder',947,'-=FB=-',197);
INSERT INTO x_world VALUES (1204,2,399,3,28674,'Wizard 02',3110,'Wizarder',947,'-=FB=-',978);
INSERT INTO x_world VALUES (1600,398,399,3,53793,'027',3399,'Dfender',51,'NYX',25);
INSERT INTO x_world VALUES (1607,-396,398,3,15768,'[1] JoKER',3274,'zuzi',2458,'Pax™',1025);
INSERT INTO x_world VALUES (1608,-395,398,3,33556,'[5] JoKER',3274,'zuzi',2458,'Pax™',580);
INSERT INTO x_world VALUES (2000,-3,398,2,46736,'jaker 4',13526,'jaker',2,'SS™',94);
INSERT INTO x_world VALUES (2001,-2,398,2,42413,'jaker 3',13526,'jaker',2,'SS™',226);
INSERT INTO x_world VALUES (2002,-1,398,2,35953,'jaker 2',13526,'jaker',2,'SS™',390);
INSERT INTO x_world VALUES (2409,-395,397,3,24152,'[3] JoKER',3274,'zuzi',2458,'Pax™',885);
INSERT INTO x_world VALUES (2410,-394,397,3,20135,'[2] JoKER',3274,'zuzi',2458,'Pax™',932);
INSERT INTO x_world VALUES (4750,344,395,3,34986,'3.A 4437',8833,'RESET.me',2458,'Pax™',608);
INSERT INTO x_world VALUES (5568,361,394,3,38286,'4.BBB 3OAZ4%+',8833,'RESET.me',2458,'Pax™',489);
INSERT INTO x_world VALUES (7723,113,391,3,36930,'Novo naselje',13975,'Luxorr',1240,'DRINK',74);
COMMIT;