drop table users cascade constraints;
drop table photos cascade constraints;
drop table tags cascade constraints;
drop table photo_caption cascade constraints;
drop table photo_tag cascade constraints;
drop table likes cascade constraints;

CREATE TABLE users(
userid NUMBER NOT NULL PRIMARY KEY,
username VARCHAR(15) NOT NULL UNIQUE,
email VARCHAR(25) NOT NULL UNIQUE,
password VARCHAR(10),
first_name VARCHAR(10),
last_name VARCHAR(10));


CREATE TABLE photos(
photoid NUMBER NOT NULL PRIMARY KEY,
userid NUMBER REFERENCES users(userid)ON DELETE CASCADE,
image_path VARCHAR(255) UNIQUE,
post_date DATE);

CREATE TABLE photo_caption(
photoid NUMBER REFERENCES photos(photoid)ON DELETE CASCADE,
caption VARCHAR(255));

CREATE TABLE tags(
tagid NUMBER NOT NULL PRIMARY KEY,
tag VARCHAR(20));

CREATE TABLE photo_tag(
photoid NUMBER REFERENCES photos(photoid) ON DELETE CASCADE,
tagid NUMBER REFERENCES tags(tagid),
PRIMARY KEY(photoid,tagid));

CREATE TABLE likes(
userid NUMBER REFERENCES users(userid)ON DELETE CASCADE,
photoid NUMBER REFERENCES photos(photoid)ON DELETE CASCADE,
CONSTRAINT pk PRIMARY KEY(userid,photoid));

