use world;
SELECT * FROM CITY;
USE SHOPDB;

-- DROP TABLE SHOPDB.MEMBERTBL;

CREATE TABLE SHOPDB.MEMBERTBL (
--     MEMBERID CHAR(8) NOT NULL,
--     MEMBERNAME CHAR(5) NOT NULL,
--     MEMBERADDRESS CHAR(20) NULL,
--     PRIMARY KEY (MEMBERID)
-- );

-- INSERT into membertbl values('Dang', '당탕이', '경기 부천시 중동');
-- INSERT into membertbl values('Jee', '지운이', '서울 은평구 증산동');
-- INSERT into membertbl values('Han', '한주연', '인천 남구 주안동');
-- INSERT into membertbl values('Sang', '상길이', '경기 성남시 분당구');

select * from membertbl;
-- delete from membertbl where memberid='Sang';

-- DROP TABLE SHOPDB.producttbl;

-- CREATE table shopdb.producttbl(
-- 	productname char(4) not null,
--     cost int not null,
--     makeDate date null,
--     company char(5) null,
--     amount int not null,
--     PRIMARY KEY (productname)
-- );

select * from producttbl;

-- insert into producttbl values('컴퓨터', 10, '2021-01-01', '삼성', 17);
-- insert into producttbl values('세탁기', 20, '2022-09-01', 'LG', 3);
-- insert into producttbl values('냉장고', 5, '2023-02-01', '대우', 22);

select * from producttbl;