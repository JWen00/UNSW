Continuing on from last week.. Requirements engineering is a major feature of Software Engineering! 

## 2. Requirements Engineering 

> "A condition or capability needed by a user to solve a problem or achieve an objective” 

Requirements Engineering is:  

 * A **set of activities** to identify and communicate the purpose of a software systems
 * A **negotiation process** where we explore the requirements for what a user needs and wants
 * Accounting for the different stakeholders (End users, Customer, Design team etc.)
    
#### Functional and Non-functional requirements  

*Function requirements* define the funcationality of the "system to be". These include things such as:  

 * Inputs, Output
 * Behaviours of the system
 * NULL conditions, escape routes
   
*Non-functional requirements* describe the **quantity** attributes of the "system to be"   

 * Perfomance - Taking in the reponse time and network letency
 * Reliability - mean time between failures
 * Usability - training time, number of clicks
 * Portability - % of portable code

  

#### Phases of Requirements Engineering

![phases of requirements engineering](/images/phases_requirements.png)

1. Requirements Gathering - THE TALKING 

Very rarely do clients know exactly what they want, so we have to figure it out. Often we can miss requirements as the communication is not clear or we have limited access to clients. There could also be multiple stakeholders, which would create conflicting interests/priorities. 

2. Requirements Analysis   
    - Conclude a statement of requirements or a "Vision statement' 
    - Refine and reason about the requirements 
    - Scope the project 
    - Identify dependencies, conflics and risks 
    - Negotiate and determine the priority

    Popular techinques:  
    a) Case modelling - Build a set of use cases (User initiates an action, and the system respones with an action *f: X -> Y*)  
    b) User stories (AGILE Requirements)
    
3. Requirements Specifications 
    - Document the functional and non-functions requirements   
    - Using the AGILE documentation styles, we encode the design ideas   
4. Requirements Validation   
    Often times challenges can be that the client does not know what they want   

## Case Study: Home Access 

A home access conntrol system has several functions such as door lock control, lighting controll, intrusion detection.

#### Iteration 1 

Support basic door unlocking and locking functions.  

To solve this, we could have a simple authentication based on a valid key. Anyone with knowledge of key is permitted to enter.   

BUT, how do we handle failed attempts? 

Consider our new requirement: 

 
> The system shall keep the door looked at all times unless instructued otherwise by an authorised user. When the lock is diarmed, a countdown shall be initiaed at the end of which the lock shall be automatically armed (if still unarmed)


This is a long and complex requirement which can be split into two separate requirements. 


> 1. The system shall keep the doors locked at all times, unless commanded other by an authorised user
> 2. When the lock is diarmed, a countdown shall be initiaed at the end of which the lock shall be automatically armed (if still unarmed)

#### User Stories 

Use the RGB Model (Role Goal Benefit):
``` 
As a <user>, I want <goal> so that <benefit> 
```

OR, alternatively you could use the three C's model: *Card, conversation, comfirmation*

Note: 
Epic User Stories contain user stories   
User stories contain acceptance criterias 

#### Use-Case Modelling 

Models a set of use-cases which describe the tasks to be performed by the 'system-to-be' 

It signifies what the system needs to accomplish (AND NOT HOW) 

Things to use: 
```
1. <<initiaties>> Used when an actor initiates a request/functionality 
2. <<participates>> Used when an actor is only involved when called for
3. <<includes>> Used when a user-story includes another user-story 
4. <<extends>> Used to show an optional user-story

```
# Summary 
![mind-map-1](/images/mind_map_1.png)