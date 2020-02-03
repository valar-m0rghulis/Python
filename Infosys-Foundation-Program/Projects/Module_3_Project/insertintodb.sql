--uesers table

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(1,'asmith','smitha@gmail.com','asmith','angella','smith');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(2,'skumar','skumar@gmail.com','skumar','shiv','kumar');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(3,'smily','smily@yahoo.com','smily','sweta','singh');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(4,'royal','royal@gmail.com','royal','jack','smith');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(5,'harryp','hpotter@yahoo.com','potter','harry','potter');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(6,'reven','revenc@gmail.com','creven','reven','claw');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(7,'jsnow','jsnow@yahoo.com','jhon','jhon','snow');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(8,'sarya','aryas@gmail.com','aryaas','arya','stark');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(9,'ned','neds@gmail.com','nedme','ned ','stark');

INSERT INTO users(userid,username,email,password,first_name,last_name)
VALUES
(10,'walkers','walkers@yahoo.com','whitewalk','white','walker');


--photos table

INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(1,1,'D\:\posts\1.jpg',to_date('4-5-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(2,1,'D\:\posts\2.jpg',to_date('20-10-2017','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(9,1,'C\:\posts\9.jpg',to_date('29-11-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(4,2,'C\:\posts\4.jpg',to_date('14-3-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(7,2,'C\:\posts\7.jpg',to_date('4-7-2016','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(3,3,'D\:\posts\3.jpg',to_date('4-5-2017','dd-mm-yyyy'));

INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(5,3,'C\:\posts\5.jpg',to_date('20-1-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(6,3,'C\:\posts\6.png',to_date('4-5-2011','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(10,3,'C\:\posts\10.jpg',to_date('31-12-2016','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(8,4,'C\:\posts\8.jpg',to_date('24-6-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(12,4,'D\:\posts\12.jpg',to_date('12-12-2017','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(11,5,'C\:\posts\11.jpg',to_date('24-6-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(20,5,'D\:\posts\20.jpg',to_date('11-8-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(18,6,'D\:\posts\18.jpg',to_date('4-4-2017','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(15,6,'C\:\posts\15.jpg',to_date('25-12-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(13,7,'D\:\posts\13.jpg',to_date('21-5-2016','dd-mm-yyyy'));

INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(16,7,'D\:\posts\16.jpg',to_date('7-7-2017','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(19,7,'D\:\posts\19.jpg',to_date('11-10-2017','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(14,8,'D\:\posts\14.jpg',to_date('24-6-2016','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(17,8,'D\:\posts\17.jpg',to_date('20-8-2018','dd-mm-yyyy'));



INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(21,9,'D\:\posts\21.jpg',to_date('7-4-2017','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(23,9,'C\:\posts\23.jpg',to_date('29-3-2018','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(22,10,'C\:\posts\22.jpg',to_date('12-9-2016','dd-mm-yyyy'));


INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(25,10,'C\:\posts\25.jpg',to_date('4-5-2018','dd-mm-yyyy'));

INSERT INTO photos(photoid,userid,image_path,post_date)
VALUES
(24,10,'C\:\posts\24.jpg',to_date('24-7-2017','dd-mm-yyyy'));



--photo_caption table


INSERT INTO photo_caption(photoid,caption)
VALUES(1,'Perfect pic');


INSERT INTO photo_caption(photoid,caption)
VALUES(2,'Natures call');


INSERT INTO photo_caption(photoid,caption)
VALUES(3,'My holiday');


INSERT INTO photo_caption(photoid,caption)
VALUES(4,'Nature att its best');


INSERT INTO photo_caption(photoid,caption)
VALUES(5,'Nice Travelling');


INSERT INTO photo_caption(photoid,caption)
VALUES(6,'Feeling happy');


INSERT INTO photo_caption(photoid,caption)
VALUES(7,NULL);


INSERT INTO photo_caption(photoid,caption)
VALUES(8,'New tech');


INSERT INTO photo_caption(photoid,caption)
VALUES(9,'cooool');


INSERT INTO photo_caption(photoid,caption)
VALUES(10,'London trip');


INSERT INTO photo_caption(photoid,caption)
VALUES(11,'Artistic');


INSERT INTO photo_caption(photoid,caption)
VALUES(12,'Beautiful..isnt is?');


INSERT INTO photo_caption(photoid,caption)
VALUES(13,'Nice picture');


INSERT INTO photo_caption(photoid,caption)
VALUES(14,'Looking forward');


INSERT INTO photo_caption(photoid,caption)
VALUES(15,'Just feel');


INSERT INTO photo_caption(photoid,caption)
VALUES(16,'Peaceful');


INSERT INTO photo_caption(photoid,caption)
VALUES(17,'No words');


INSERT INTO photo_caption(photoid,caption)
VALUES(18,NULL);


INSERT INTO photo_caption(photoid,caption)
VALUES(19,'Speaking pics');


INSERT INTO photo_caption(photoid,caption)
VALUES(20,'Lovely nature');

INSERT INTO photo_caption(photoid,caption)
VALUES(21,'Tech Miracle');

INSERT INTO photo_caption(photoid,caption)
VALUES(22,'Self Descriptive');

INSERT INTO photo_caption(photoid,caption)
VALUES(23,'Beautiful..isnt is?');

INSERT INTO photo_caption(photoid,caption)
VALUES(24,'No words');

INSERT INTO photo_caption(photoid,caption)
VALUES(25,'Just enjoyy');

--tags table

INSERT INTO tags(tagid,tag)
VALUES(1,'Art');

INSERT INTO tags(tagid,tag)
VALUES(2,'Engineering');

INSERT INTO tags(tagid,tag)
VALUES(3,'Science');

INSERT INTO tags(tagid,tag)
VALUES(4,'Nature');

INSERT INTO tags(tagid,tag)
VALUES(5,'Travel');

INSERT INTO tags(tagid,tag)
VALUES(6,'World');

INSERT INTO tags(tagid,tag)
VALUES(7,'Music');


INSERT INTO tags(tagid,tag)
VALUES(8,'History');


INSERT INTO tags(tagid,tag)
VALUES(9,'Ancient');

INSERT INTO tags(tagid,tag)
VALUES(10,'Mystries');

INSERT INTO tags(tagid,tag)
VALUES(11,'Stories');

INSERT INTO tags(tagid,tag)
VALUES(13,'Old');

--photo_tag table

INSERT INTO photo_tag(photoid,tagid)
VALUES(1,3);

INSERT INTO photo_tag(photoid,tagid)
VALUES(1,5);

INSERT INTO photo_tag(photoid,tagid)
VALUES(2,7);

INSERT INTO photo_tag(photoid,tagid)
VALUES(3,3);

INSERT INTO photo_tag(photoid,tagid)
VALUES(4,1);

INSERT INTO photo_tag(photoid,tagid)
VALUES(5,8);

INSERT INTO photo_tag(photoid,tagid)
VALUES(5,10);

INSERT INTO photo_tag(photoid,tagid)
VALUES(6,4);

INSERT INTO photo_tag(photoid,tagid)
VALUES(7,1);

INSERT INTO photo_tag(photoid,tagid)
VALUES(7,9);

INSERT INTO photo_tag(photoid,tagid)
VALUES(8,11);

INSERT INTO photo_tag(photoid,tagid)
VALUES(8,6);

INSERT INTO photo_tag(photoid,tagid)
VALUES(9,4);

INSERT INTO photo_tag(photoid,tagid)
VALUES(10,7);

INSERT INTO photo_tag(photoid,tagid)
VALUES(11,5);

INSERT INTO photo_tag(photoid,tagid)
VALUES(12,1);

INSERT INTO photo_tag(photoid,tagid)
VALUES(12,3);

INSERT INTO photo_tag(photoid,tagid)
VALUES(13,2);

INSERT INTO photo_tag(photoid,tagid)
VALUES(14,4);

INSERT INTO photo_tag(photoid,tagid)
VALUES(15,5);

INSERT INTO photo_tag(photoid,tagid)
VALUES(16,6);

INSERT INTO photo_tag(photoid,tagid)
VALUES(17,6);

INSERT INTO photo_tag(photoid,tagid)
VALUES(18,7);

INSERT INTO photo_tag(photoid,tagid)
VALUES(19,8);

INSERT INTO photo_tag(photoid,tagid)
VALUES(20,9);

INSERT INTO photo_tag(photoid,tagid)
VALUES(21,10);

INSERT INTO photo_tag(photoid,tagid)
VALUES(22,11);

INSERT INTO photo_tag(photoid,tagid)
VALUES(23,6);

INSERT INTO photo_tag(photoid,tagid)
VALUES(24,8);

INSERT INTO photo_tag(photoid,tagid)
VALUES(25,9);

--Likes table

INSERT INTO likes(userid,photoid)VALUES(1,4);
INSERT INTO likes(userid,photoid)VALUES(1,9);
INSERT INTO likes(userid,photoid)VALUES(1,20);
INSERT INTO likes(userid,photoid)VALUES(2,4);
INSERT INTO likes(userid,photoid)VALUES(2,6);
INSERT INTO likes(userid,photoid)VALUES(2,9);
INSERT INTO likes(userid,photoid)VALUES(2,2);
INSERT INTO likes(userid,photoid)VALUES(1,23);
INSERT INTO likes(userid,photoid)VALUES(3,3);
INSERT INTO likes(userid,photoid)VALUES(3,7);
INSERT INTO likes(userid,photoid)VALUES(3,6);
INSERT INTO likes(userid,photoid)VALUES(3,10);
INSERT INTO likes(userid,photoid)VALUES(3,22);
INSERT INTO likes(userid,photoid)VALUES(3,25);
INSERT INTO likes(userid,photoid)VALUES(4,7);
INSERT INTO likes(userid,photoid)VALUES(4,5);
INSERT INTO likes(userid,photoid)VALUES(4,9);
INSERT INTO likes(userid,photoid)VALUES(4,15);
INSERT INTO likes(userid,photoid)VALUES(5,17);
INSERT INTO likes(userid,photoid)VALUES(5,18);
INSERT INTO likes(userid,photoid)VALUES(5,6);
INSERT INTO likes(userid,photoid)VALUES(6,2);
INSERT INTO likes(userid,photoid)VALUES(6,4);
INSERT INTO likes(userid,photoid)VALUES(6,8);
INSERT INTO likes(userid,photoid)VALUES(6,15);
INSERT INTO likes(userid,photoid)VALUES(7,1);
INSERT INTO likes(userid,photoid)VALUES(7,3);
INSERT INTO likes(userid,photoid)VALUES(7,8);
INSERT INTO likes(userid,photoid)VALUES(7,9);
INSERT INTO likes(userid,photoid)VALUES(8,19);
INSERT INTO likes(userid,photoid)VALUES(8,13);
INSERT INTO likes(userid,photoid)VALUES(8,23);
INSERT INTO likes(userid,photoid)VALUES(9,1);
INSERT INTO likes(userid,photoid)VALUES(9,7);
INSERT INTO likes(userid,photoid)VALUES(10,4);
INSERT INTO likes(userid,photoid)VALUES(10,23);
INSERT INTO likes(userid,photoid)VALUES(10,6);
INSERT INTO likes(userid,photoid)VALUES(10,9);
INSERT INTO likes(userid,photoid)VALUES(10,17);


