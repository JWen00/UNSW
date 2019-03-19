# Requirements Engineering 

> "A condition or capability needed by a user to solve a problem or achieve an objective” 

Requirements Engineering is:  

 * A **set of activities** to identify and communicate the purpose of a software systems
 * A **negotiation process** where we explore the requirements for what a user needs and wants
 * Accounting for the different stakeholders (End users, Customer, Design team etc.)
    

### Functional and Non-functional requirements  
---

Function requirements define the funcationality of the "system to be." These include things such as:  

 * Inputs, Output
 * Behaviours of the system
 * NULL conditions, escape routes
   
Non-functional requirements describe the **quantity** attributes of the "system to be"   

 * Perfomance - Taking in the reponse time and network letency
 * Reliability - mean time between failures
 * Usability - training time, number of clicks
 * Portability - % of portable code

  

### Phases of Requirements Engineering
---

1. Requirements Gathering    
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


# User Stories 

I ndependent  
N egotiable  
V aluable  
E stimatable  
S mall  
T estable 

# USE-Cases

Use-case scenarios

Example: 
--- 
Use Case title: Pay for a job posting  

Primary Actor: Recuiter   

Level: Actor goal   

Pre-condition: The job information hsa been entered but is not viewable   

Minimal Guaranteers: None    

Success Guaranteers: Job is posted, recuiter's 
credit cars is changed    
