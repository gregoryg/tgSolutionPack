## creates schema for MOVIES (based on IMDB data) and loads sample data
##
## NOTE: script will DROP existing tables before creating new ones
##
## NOTE2: loading data from local csv is turned OFF by defult on mysql on mac
##
##   server Ide
##      SHOW GLOBAL VARIABLES LIKE 'local_infile';
##      SET GLOBAL local_infile=1;
##   client Ide
##      mysql --local-infile=1
##

CREATE DATABASE IF NOT EXISTS ldbc;
USE ldbc;

## allow cascading deletes
SET foreign_key_checks = 0;

DROP TABLE IF EXISTS comment;
CREATE TABLE comment (
     CommentId               INT NOT NULL,
     creationDate     DATE,
     locationIP     VARCHAR(25),
     browserUsed    VARCHAR(20),
     content        VARCHAR(250),
     length          INT,
     PRIMARY KEY (CommentId)
);

DROP TABLE IF EXISTS forum;
CREATE  TABLE forum (
     ForumId               INT NOT NULL,
     title     VARCHAR(25),
     creationDate    DATE,
     PRIMARY KEY (ForumId)
);

DROP TABLE IF EXISTS organization;
CREATE  TABLE organization (
     OrganisationId               INT NOT NULL,
     type     VARCHAR(25),
     name    VARCHAR(25),
     url        VARCHAR(100),
     PRIMARY KEY (OrganisationId)
);

DROP TABLE IF EXISTS person;
CREATE  TABLE person (
     PersonId               INT NOT NULL,
     firstName     VARCHAR(25),
     lastName     VARCHAR(25),
     gender     VARCHAR(25),
     birthday     VARCHAR(25),
     creationDate     VARCHAR(30),
     locationIP    VARCHAR(25),
     browserUsed        VARCHAR(25),
     PRIMARY KEY (PersonId)
);

DROP TABLE IF EXISTS place;
CREATE  TABLE place (
     PlaceId               INT NOT NULL,
     name    VARCHAR(25),
     url        VARCHAR(100),
     type     VARCHAR(25),
     PRIMARY KEY (PlaceId)
);

DROP TABLE IF EXISTS post;
CREATE  TABLE post (
     PostId               INT NOT NULL,
     imageFile     VARCHAR(40),
     creationDate     VARCHAR(25),
     locationIP     VARCHAR(25),
     browserUsed     VARCHAR(25),
     language    VARCHAR(25),
     content        VARCHAR(25),
     length        VARCHAR(25),
     PRIMARY KEY (PostId)
);

DROP TABLE IF EXISTS tag;
CREATE  TABLE tag (
     TagId               INT NOT NULL,
     name    VARCHAR(25),
     url        VARCHAR(100),
     PRIMARY KEY (TagId)
);

DROP TABLE IF EXISTS tagClass;
CREATE  TABLE tagClass (
     tagClassId               INT NOT NULL,
     name    VARCHAR(25),
     url        VARCHAR(100),
     PRIMARY KEY (tagClassId)
);

DROP TABLE IF EXISTS comment_hasCreator_person;
CREATE  TABLE comment_hasCreator_person (
     CommentId     INT  NOT NULL,
     PersonId     INT  NOT NULL,
     PRIMARY KEY (CommentId),
     FOREIGN KEY (PersonId) REFERENCES person(PersonId)
);

DROP TABLE IF EXISTS comment_hasTag_tag;
CREATE  TABLE comment_hasTag_tag (
     CommentId     INT  NOT NULL,
     TagId     INT  NOT NULL,
     PRIMARY KEY (CommentId),
     FOREIGN KEY (TagId) REFERENCES tag(TagId)
);

DROP TABLE IF EXISTS forum_hasMember_person;
CREATE  TABLE forum_hasMember_person (
     ForumId     INT  NOT NULL,
     PersonId     INT  NOT NULL,
     PRIMARY KEY (ForumId),
     FOREIGN KEY (PersonId) REFERENCES person(PersonId)
);

DROP TABLE IF EXISTS person_hasInterest_tag;
CREATE  TABLE person_hasInterest_tag (
     PersonId     INT  NOT NULL,
     TagId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (TagId) REFERENCES tag(TagId)
);

DROP TABLE IF EXISTS person_isLocatedIn_place;
CREATE  TABLE person_isLocatedIn_place (
     PersonId     INT  NOT NULL,
     PlaceId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (PlaceId) REFERENCES place(PlaceId)
);

DROP TABLE IF EXISTS person_knows_person;
CREATE  TABLE person_knows_person (
     PersonId     INT  NOT NULL,
     FriendId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (FriendId) REFERENCES person(PersonId)
);

DROP TABLE IF EXISTS person_likes_post;
CREATE  TABLE person_likes_post (
     PersonId     INT  NOT NULL,
     PostId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (PostId) REFERENCES post(PostId)
);

DROP TABLE IF EXISTS person_workAt_organisation;
CREATE  TABLE person_workAt_organisation (
     PersonId     INT  NOT NULL,
     OrganisationId     INT  NOT NULL,
     PRIMARY KEY (PersonId),
     FOREIGN KEY (OrganisationId) REFERENCES organisation(OrganisationId)
);

DROP TABLE IF EXISTS post_hasCreator_person;
CREATE  TABLE post_hasCreator_person (
     PostId     INT  NOT NULL,
     PersonId     INT  NOT NULL,
     PRIMARY KEY (PostId),
     FOREIGN KEY (PersonId) REFERENCES person(PersonId)
);

DROP TABLE IF EXISTS tag_hasType_tagclass;
CREATE  TABLE tag_hasType_tagclass (
     TagId     INT  NOT NULL,
     TagClassId     INT  NOT NULL,
     PRIMARY KEY (TagId),
     FOREIGN KEY (TagClassId) REFERENCES tagClass(TagClassId)
);


## Load from csv
LOAD DATA LOCAL INFILE './data/comment_sample.csv' INTO TABLE comment FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (CommentId,creationDate,locationIP,browserUsed,content,length);
LOAD DATA LOCAL INFILE './data/forum_0_0.csv' INTO TABLE forum FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (ForumId,title,creationDate);
LOAD DATA LOCAL INFILE './data/organisation_0_0.csv' INTO TABLE organization FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (OrganisationId,type,name,url);
LOAD DATA LOCAL INFILE './data/person_0_0.csv' INTO TABLE person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,firstName,lastName,gender,birthday,creationDate,locationIP,browserUsed);
LOAD DATA LOCAL INFILE './data/place_0_0.csv' INTO TABLE place FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PlaceId,name,url,type);
LOAD DATA LOCAL INFILE './data/post_sample.csv' INTO TABLE post FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PostId,imageFile,creationDate,locationIP,browserUsed,language,content,length);
LOAD DATA LOCAL INFILE './data/tag_0_0.csv' INTO TABLE tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (TagId,name,url);
LOAD DATA LOCAL INFILE './data/tagclass_0_0.csv' INTO TABLE tagClass FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (TagClassId,name,url);

LOAD DATA LOCAL INFILE './data/tag_hasType_tagclass_0_0.csv' INTO TABLE tag_hasType_tagclass FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (TagId,TagClassId);
LOAD DATA LOCAL INFILE './data/post_hasCreator_person_sample.csv' INTO TABLE post_hasCreator_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PostId,PersonId);
LOAD DATA LOCAL INFILE './data/person_workAt_organisation_0_0.csv' INTO TABLE person_workAt_organisation FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,OrganisationId);
LOAD DATA LOCAL INFILE './data/person_likes_post_sample.csv' INTO TABLE person_likes_post FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,PostId);
LOAD DATA LOCAL INFILE './data/person_knows_person_sample.csv' INTO TABLE person_knows_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,FriendId);
LOAD DATA LOCAL INFILE './data/person_isLocatedIn_place_0_0.csv' INTO TABLE person_isLocatedIn_place FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,PlaceId);
LOAD DATA LOCAL INFILE './data/person_hasInterest_tag_0_0.csv' INTO TABLE person_hasInterest_tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (PersonId,TagId);
LOAD DATA LOCAL INFILE './data/forum_hasMember_person_sample.csv' INTO TABLE forum_hasMember_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (ForumId,PersonId);
LOAD DATA LOCAL INFILE './data/comment_hasTag_tag_sample.csv' INTO TABLE comment_hasTag_tag FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (CommentId,TagId);
LOAD DATA LOCAL INFILE './data/comment_hasCreator_person_sample.csv' INTO TABLE comment_hasCreator_person FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (CommentId,PersonId);
