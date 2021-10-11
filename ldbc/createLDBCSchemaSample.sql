## creates schema for MOVIES (based on IMDB data) and loads sample data
##
## NOTE: script will DROP existing tables before creating new ones
##
## NOTE2: loading data from local csv is turned OFF by defult on mysql on mac
##
##   server side
##      SHOW GLOBAL VARIABLES LIKE 'local_infile';
##      SET GLOBAL local_infile=1;
##   client side
##      mysql --local-infile=1
##

SET @datadir := '/Users/roberthardaway/tg/projects/tgSolutionPack/ldbc/data/';

CREATE DATABASE IF NOT EXISTS ldbc;
USE ldbc;

DROP TABLE IF EXISTS comment;
CREATE  TABLE comment (
     id               DOUBLE,
     creationDate     DATE,
     locationIP     VARCHAR(25),
     browserUsed    VARCHAR(20),
     content        VARCHAR(250),
     length          INT
);

DROP TABLE IF EXISTS forum;
CREATE  TABLE forum (
     id               INT,
     title     VARCHAR(25),
     creationDate    DATE
);

DROP TABLE IF EXISTS organization;
CREATE  TABLE organization (
     id               INT,
     type     VARCHAR(25),
     name    VARCHAR(25),
     url        VARCHAR(100)
);

DROP TABLE IF EXISTS person;
CREATE  TABLE person (
     id               INT,
     firstName     VARCHAR(25),
     lastName     VARCHAR(25),
     gender     VARCHAR(25),
     birthday     VARCHAR(25),
     creationDate     VARCHAR(30),
     locationIP    VARCHAR(25),
     browserUsed        VARCHAR(25)
);

DROP TABLE IF EXISTS place;
CREATE  TABLE place (
     id               INT,
     name    VARCHAR(25),
     url        VARCHAR(100),
     type     VARCHAR(25)
);

DROP TABLE IF EXISTS post;
CREATE  TABLE post (
     id               INT,
     imageFile     VARCHAR(40),
     creationDate     VARCHAR(25),
     locationIP     VARCHAR(25),
     browserUsed     VARCHAR(25),
     language    VARCHAR(25),
     content        VARCHAR(25),
     length        VARCHAR(25)
);

DROP TABLE IF EXISTS tag;
CREATE  TABLE tag (
     id               INT,
     name    VARCHAR(25),
     url        VARCHAR(100)
);

DROP TABLE IF EXISTS tagClass;
CREATE  TABLE tagClass (
     id               INT,
     name    VARCHAR(25),
     url        VARCHAR(100)
);

## Load from csv
LOAD DATA LOCAL INFILE './data/comment_sample.csv' INTO TABLE comment FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,creationDate,locationIP,browserUsed,content,length);
LOAD DATA LOCAL INFILE './data/forum_0_0.csv' INTO TABLE forum FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,title,creationDate);
LOAD DATA LOCAL INFILE './data/organisation_0_0.csv' INTO TABLE organization FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,type,name,url);
LOAD DATA LOCAL INFILE './data/person_0_0.csv' INTO TABLE person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,firstName,lastName,gender,birthday,creationDate,locationIP,browserUsed);
LOAD DATA LOCAL INFILE './data/place_0_0.csv' INTO TABLE place FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url,type);
LOAD DATA LOCAL INFILE './data/post_sample.csv' INTO TABLE post FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,imageFile,creationDate,locationIP,browserUsed,language,content,length);
LOAD DATA LOCAL INFILE './data/tag_0_0.csv' INTO TABLE tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url);
LOAD DATA LOCAL INFILE './data/tagclass_0_0.csv' INTO TABLE tagClass FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (id,name,url);


