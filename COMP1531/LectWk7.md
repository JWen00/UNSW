# Effective Software Design
 A.K.A. Why we should write good code

### Design Smells 

Software developers like to simulate their lives in the real world so when their code becomes bad, it **rots** and **smells** 

This disease is not a results of the developer, but rather a **symptom of poor design** 

When this happens, it is caused by: 
* a violation of key **design principles** 
* lack of **refactoring** when required 

> Reminder: Refactoring is re-structuring the internal struture to make it easier to understand and modify without changing it's external observable behaviour 


1. Rigidity - Cannot make small changes without causing a cascade of changes 
2. Fragility - Tendency for code to break from small changes 
3. Immobility - Design is hard to reuse  
4. Viscosity - Filling in holes rather than preserving methods 
5. Opacity - Difficulty to understand the code (ie. bad variable names or function names) 
6. Needless complexity - Contains constructs not useful 
7. Needless repetition - repeated classes which could be unified 


### How to start writing better code (Good Design) 

#### Coupling 

Coupling is the interependence between components or classes 

**High coupling** means that one component A depends on another component B and is affected by the internal changes to B. 

To ensure good design we want to aim for **loosely coupled** classes.

#### Cohesion

Cohesion is the degree which all elementsof a component or class work together as a functional uni

**Highly cohesive modules** are much easier to maintain as functions are responsibile for one purpose and possess higher probability and reusability 


### Solid Principles 

#### **S**RP - Single Responsibility Principle    
Each responsibility can be tested in isolation
SRP allows readability, usability and testability 
 
#### **O**CP - Open Closed Principle        
**open** for extention so that we can add onto a component 
**closed** for modification so that extending the module does not require changing the orgiinal source  

OCP is achieved through **abstraction and dynamic binding**   

OCP reduces rigidity it is not easy and expensive but creates very good design through proving flexibility, reusability and maintainability in th long run


#### **L**SP - Liskov Substitution Principle    
#### **I**SP - Interface Segregation principle    
#### **D**IP - Dependency Inversion Principle    


