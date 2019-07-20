# SQL Injection

## What is it? 
SQL injection is on of the top 10 website application vulnerabilities.    

It is a common attack which dargets the backend database to access information that is not intended to be displayed. This could include sensitive company data and private customer information. 

## How is it done? 

Before we dig into how it is actually done, we need to understand how SQL queries work. 

* TODO: Make a site with a table of burger/Wraps/Mains (yay1531) Stay tuned for more info!

Consider our website. We can filter to find the product we want. When you click on a cateogory, the browser posts this information and the url would look something like this 

`https://my_website.come/products?category="Burgers"`    

This would create the SQL enquiery to retreive details from the databse: 

`SELECT * FROM products WHERE cetegory = 'Burgers' AND 'Available = 1'` 

The query would return all details regarding burgers which are available. 

## How to H*ck (no, not really)

1. Adding comments to the query (--)

Changing the link to `https://my_website.come/products?category="Burgers"--` would result in:   

`SELECT * FROM products WHERE cetegory = 'Burgers'-- AND 'Available = 1'`. This would deem the rest of the query as a comment which means the site would display non-available products as well. 

2. Returning true for everything

Changing the link to `https://my_website.come/products?category="Burgers"+OR1=1--"` would result in:  

`SELECT * FROM products WHERE cetegory = 'Burgers'-- AND 'Available = 1'`. This would return all items regardless of the categories since `1=1` is always true. 

3. UNION 

Union is a keyword which can be used to retrieve data from other tables within the database.   

E.g. `SELECT a, b, from TABLE1 UNION SELECT c, d from table2`  

For this to work, the queries must have the name number of columns and the data tyles must be compatible. 


## Doing your research 

It is useful to obtain information about the data base. For example:   

1. Version using `SELECT * FROM v$Version` 
2. All tables using `SELECT * FROM information_schema.tables` 

Owe my credits to this site here: https://portswigger.net/web-security/sql-injection 

Will update about how to prevent this soon! 