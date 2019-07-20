# Stategy Pattern

* Favour composition over inheritance 
* program to a supertype 
* encapsulate what varies
* Video Example: DuckSIM - Varying quacks 

# State Diagram 

* FSM (Finite State Machine) 
* Fits to OCP 
* Video Example: Gumball Machine 

Define a new class for each state and an action as a method of the state 

State transition is more exiplicit 
Delegate depending on the state 
![State Patter](/images/state_pattern.png) 

State control is different from strategy control. Context is in control of its own behaviour and is internalised. 

# The Template Method Pattern

Encapsulate steps of an algorithm with inheritance 

For example: 

* MakeCoffee() {} 
* MakeTea(){} 

In line with the HOLLYWOOD principle. Don't call us, we'll call you. 

It is a one directional implementation

# Iterator Pattern 

 Difference between Array and ArrayList 


 We can encapsulate what varies
  
  Encapsulate HOW we step through items 
 
Create a class called iterator to encapsulate this.

# Composite Pattern 

Represent part-whole heirarchies 
Abstract whether we're using a single or collection of something
Good for recursive algorithms 

# Decorator Pattern 
Coffee with milk 
Adds on
but is still the same base component 

# Observer Pattern  

* one to many 
* Add and remove observers easily from the observable
* Maintains loose couplings between the two 

# Builder Pattern 

* provide multiple contructors for a user
* Don't really udnerstand the sematics of a userBuilder 

# Factory Pattern 

Need to recise this.. Don't really understand. Delegate the task to someone else? 
 