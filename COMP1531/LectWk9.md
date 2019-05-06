
# ER Model 

### Entites 
Weak entities exits only because of an association with strong entites 
It is shown by a double box.
### Attributes 
Simple attributes have only one value 
Composite attributes have several values 
Multivalued attributes 
Derived attriutes 
### Relations 
Relationship type 
Strong relationship shown by double line or thick line 
Relationship-set
> Degree
> Cardinality
Carindality shows how many entity instances in a relationship
### participation 
Total participation is shown by a double line 
Partial participation is shown by a naormla line 

### Subclasses andinheritance in ER Diagrams 
Has all the attributes in the parent plus its own 
Properties: 
> Overlapping (represented by O)
Means that they can the parent can be both children at once. 
ie person can be a doctor and patient at once 
> Disjoint (Represented by d)
Means that the parent can only be once of the child 
ie. a employee can only be a permanent or contract employee

### Design considerations: Object -> attribute or entity? 
    For example: 
    1) Customer -- Addresss -- Suburb/City/Postcode 
    2) Customer -- hasAddresss -- Address -- Suburb/Cuty/Postcode

    Example 1 only works if the customer has ONLY one address 
        > associated with once instance of the addresss 
    Example 2 works if the customer has multiple addresses


# Relational Data Model 
popular in the last decade 
based on the theory of sets
strutures the model as rows and columns 
 the goal of a relational model: 
 > simple general data 
 > maps easily to file structures 

## Constraints 
Prevent invalid data to be inserted into the table 


 ### The referential integrity contraint 
 Master table is linked to the child table through a foreign key ensures that a row can be added to the master table only when the foreign key has only when the child row has been made

 ### Domain Contraint 
Has to suit the type of data 
ie age has to be int 
address has to exist/valid

 ### Primary key contraint   
  It can never take in a null value  
    key has to be unique 
    
 ### Key contraint 
 key has to be unique   
     RULE: values have to be unique but NULL values are still permissable 

## Descripting relationship chemas 
 SQL probides the fomralism to express relational schemas 
SQL provides a Data Definition Language (DDL) 

## ER to Relational Mapping 
