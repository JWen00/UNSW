# Domain Models 

(Also known as "conceptual model" ) 

The domain model provides a visual representation of the problem, through decomposing the domain into key concepts

We want to map out the model into a conceptual model and see how each actor plays out with each other  

### Key Ideas
Domain Models allow us to

* consider what is the central problem (*core domain*) and it's relationship between sub-parts (*sub-domains*) 

* ensure that the system reflects a deep understanding of the problem domain as objects represent domain concepts

* foster unambiguous shared understanding of the problem domain 

## What are objects? 

Domain model are mostly based on the O-O design paradigm. 

But first, O-O Programming..?

 1. Objects are entities. 

 2. Objects have **attributes** and **methods** 

Atrributes are sth like their variables while methods are their functions 

3. Objects also encasulates some **state** 

The state refers to the currently assigned values and also gives an object its (unique) identity

4. Objects interact and communicate with each other through the **object interface** 

The interface is a set of the object's methods that can be invoked on the object 

5. A **class** is a blueprint defining the attributes and methods of an object.
  
AKA an object is an **instance** of a class 
AKA an object is **instantiated**  from a class

#### Key Terms 
* Attributes
* Methods 
* Object State
* Object Interface
* Class
* Instance
* Instantiate 

## Principles of O-O Design 

1.  Abstraction 

Abstractions means making a class/object generic and therefore being able to focus on the common properties and behaviours of objects

2.  Encapsulation 

Encapsulation means HIDING the object state so that the data is restricted. 

In this manner, only methods provide explicit access to the object. 

Then, in an object, there are **Private attributes** and **Public attributes** 

#### Benefits? 
* ensures that the object's state is consistent (**consistent state**)

* increases usability 
  
    Separating private and public data through an object's interface provides a clear view of the role of the object

* abstracts implementations 

    Encapsulations means that there are less dependencies so changes do not break the entire system 

## Relationships between Objects

1. Inheritance 

Inheritance models a relationship between classes in which once class represents a more general concept than another more specialised class.

AKA One class is a subset of another class. 

The subset *inherits* the attributes and methods from the other class. 

 ![inheritance example](/images/inheritance.png)

2. Association 

Association between two classes shows that they are linked to each other in some manner. 

## Back to Design Modelling - CRC Cards 

**C** lass   
**R** esponsibility   
**C** ollaboration   

For example
> A customer  
 deposits money into an **account**    

The creation of CRC models 
1. Read the description
2. Identity core classes 
3. Create a card per class
4. Add responsibilities 
5. Add collaborations
6. Add more classes as you discover them 
7. Refine by identifying inheritance 


A good method to see if it works is a **Scenario Walk-through** 

### Types of Association 
1. Association is a special type of relationship between two classes

> Shown as a line between two classes 

2. Aggregation is when a whole class contains another class 
 
> Shown as a white diamond, for example, [Car]<>--[Wheels] means a Car contains Wheels 

3. Composition is when a class cannot exist without another class 

> Shown as a black diamond, for example, [Book]<//>--[Pages] means a book cannot exist without pages 


# Summary 
![summary-week-4](/images/mind_map_4.png)







