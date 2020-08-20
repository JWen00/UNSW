# SQLi 

## 1) What's on the table already? 

Understanding what you're looking for is a good start 

## 2) Where is the query being sent to? 

Do we know if it's sanitised on client side? 

Do we know if an API call is being made? 

Is this completely blind SQLi? 

## 3) Break the input with [ `, ', ", """] 

Find out what the original query could possible look like. 

You can also try 9=9 or 4=4, not just 1=1

## 4) Find all the columns using `INFORMATION_SCHEMA.COLUMNS`

For a UNION query to work, two key requirements must be met:

* The individual queries must return the same number of columns.
* The data types in each column must be compatible between the individual queries.

See here for more indepth steps 

https://www.sqlinjection.net/union/
https://portswigger.net/web-security/sql-injection/union-attacks

## 5) Find the purpose of your injection

* Showing hidden content 
* Delete a ban record
* Modify the table 

## 6) Other 

```
SELECT CONCAT(login, password) FROM members
```