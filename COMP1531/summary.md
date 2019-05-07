# Softawre Engineering 

A software engineer orchestrates what a programmer should code. 

They aim to understand, develop and deliver what client is after. 

This is done through **Software Development Life Cycles** 

Requirements/Analysis->Design->Implementation->Testing->Evolution 


# Software Development Methodologies 

* Waterfall model (linear streamline) 
* Incremental and Iterative Model (Code as you go) 

# Requirements Engineering 

* Functional and None-functional requirements 
* Phases: 
    1. Requirements Gathering - understand the problem from the client's point of view 
    2. Requirements analysis - understand and scope the projects, identifying major parts and the 'vision'
    3. Requirements specification - document the functional and non-functional parts 
    4. Requirements validation - Validate that our information is correct 
    

# Software Architecture 

* n-tier (Layered) 

One client and several servers 

3 main layers 
1. Presentation
2. Business
(2.5. Persistance) 
3. database

* Client Server 

Client and Server talk to each other 

* Pipe and Filter 

When data is passed through a single 'pipe' and filtered through different requirements. 

* Publish-subscribe (Event-driven) 

The system responds to something happening. 

Similar to api.listen(...)

* Peer-to-peer 

Each computer functions as a client and server 
But now we don't know who owns the data 
Easy to setup and simple 



# SOLID 

* SRP - Single Responsibility Principal 
* OCP - Open for Extension, Closed for modification 
* LSP - Liskov Substitutoin principal 

Objects can be replaced with their sub-classes without affecting the program 

* DIP - Dependency Inversion principal 

High-level modules should be independant of Low-level modules (low coupling) 

## Design Smells 

* Rigidity 
* Fragility 
* immobility
* too complex 
*  revision 


# INVEST 

# CCC  (User Stories) 

