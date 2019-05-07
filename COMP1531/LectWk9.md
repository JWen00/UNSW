# ER Model

ER diagrams (may) contain: 
* Entities (Strong or weak)
* Attributes (Composite, derived, multivalued, simple) 
![attributes-images](/images/er_attributes.png)  
* Cardinatlity 
![cardinality-image](/images/er_cardinality.png) 
* Participation (Partial and Total) 
![participation-image](/images/er_participation.png) 
* Subclasses/Inheritance (Overlapping, Disjoint)
![inheritance-image](/images/er_inheritance.png) 

For example: 
![relationship-example](/images/er_example1.png) 
1. A course has many lecturers. There must be a lecturer for a course. 
2. Courses must have a lecturer (or many) who teaches. A lecturere must have a course (or many). 
3. One lectuerer teaches one course. There must be a lectuerer for a couse. 

# Relational Data Model 

Relational Data model describes the world as a collection of inter-connected relations. 
* Simplifies general data  
* Maps easily to file structures 

Core Components to a **Relational Model** 

1. Attribute - a single data that forms part of a relation  

2. Tuple - collection of attribute values 

3. Domain - set of allowed values for an attribute 

4. Relational schema - gives the name for the relation (summary of object.) 

5. Relation - set of tubles based on the realtional schema 

6. Key - a single attribute that contains a distinct value for every tuple in the relation 

7. Foreign Key - single attribute in one relation that conta


## Constraints 
Prevent invalid data to be inserted into the table 

* Domain Constraints - values which an attribute should have 
* Referential integrity constraints - describe references between relations 

 Master table is linked to the child table through a foreign key ensures that a row can be added to the master table only when the foreign key has only when the child row has been made

 * Primary key contraint - It can't take in a null value (has to exist) key has to be unique
    
 * Key has to be unique   
     RULE: values have to be unique but NULL values are still permissable 

## ER to Relational model 

![image](/images/er_relational.png)



