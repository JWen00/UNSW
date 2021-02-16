`# Databases and ER Models


### What is Data? 
Data is facts which can be recorded and have implcit meaning. 

We need a database because data by itself is not very useful. 

`DATA -> INFORMATION -> DECISION`

Data needs to be: 
1. Stored
2. Manipulated
3. Shared 
4. Transmitted 

### What are databases 

A **database** represents a logically coherent collection of related data.

A *database management system (**DBMS**)* is a softaware application: 

It allows users to: 
* Create and maintain a database (**DDL**) 
* Define queries to retrieve data from the databse 
* Perform transaction that cause some data to be written or deleted from the database (**DML**) 
* Provide concurrency, integrity and security 

NOTE: A database and DBMS is colelctively referred to as a database system 



#### Challenges in building Databases 

* Efficiency 
* Security 
* Scalability 
* Maintainability 
* Availability
* Integration
* Accounting for new media types 

### Data Models 

Data models can be characterised into **logical models** and **physical models** 

Logical is like the ER or OO model - higher-level 

Physical is like the relational model - physically show tables 

* Relational Model - Stores data as tubles or records in tables (E.g. SQL Server, Sybase, Oracle) 

* Document model - Sored in hierarchical (e.g. XML) 

* Object-oriented Model - Stored as a collection of objects 
* Object-Relational model - Hybrid of both 

> **Database schema** adheres to a data model and provides a logical view of the database


### Entity Relationship Conceptual Data-Modelling 

ER Models contain: 

* Entity 
* Attribute 
* Entity-set
* Primary Key 

> Entity :is-like: Object Instance 
> Entity Set :is-like: Class 


#### Types of attributes 
* Simple 
* Composite 
* Multi-valued 
`