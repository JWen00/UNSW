# Software Architecture 

Good Software architecture solves problems as software systems increase in **size and complexity**. 

Software **architecture** focuses on the non-functional requirements and decomposition of functional requirements. 

> Reminder: *Function requirements* are the user stories while *Non-functional requirements* refers more to design choice 

Software **design** focuses on the implementation of functional requirements 

Softwares are decomposed into systems to form a *heirarchical organisation*  
 
![Software heiarchy](/images/software_structure.png)

HOW we decompose the system is the **Architectural Style** 

HOW we document the system's software architecture is the **Architectural View** 

### Why do we decompose systems? 

1. It allows understanding and communication 

By separating systems into its various stake-holders, subsystems, classes/objects and methods, the system becomes easier to understand as a whole 

2. It tackles complexity 

Like how we have functions which only perform one functionality, decomposing systems allow people to work on individual pieces of the system which can later be integrated to form the final system. 

3. Allows for flexibiity 

When an extention is added onto the system, or future evolution occurs, it is easier to decouple unrelated parts 

4. Avoid repetition of code 
 
 Rather than "reinventing the wheel," a decomposed system allows focus on creative parts and ideitification of components which have high reusabilty.  

### Architectural Styles [Formal Definition] 
Architectural Styles is defined by its: 
1. Components - A collection of computational units or elements that do the work (Classes/Databases) 
2. Connectors - Event Callers which enable communciation between different components 
3, Constraints - Define how components can be combined to form the system

### Architectural Styles 

#### Client/Server 

> Also known as a 2-tier client-server architecture 

**Problem**:  
Need to share data between a client and service provider distributed geographically across different locations. 

**Solution**: 
Separate the Software Architecture into *two distinct componenets:*

1. **Server-Side** provides specific services like wait for and handling connection 

2. **Client-Side** initiates connections to request services provided by the server  

#### 3-Tier/ N-Tiered Architecture 
Example of a 3-Tier Architecture 
![3-tier-architecture](/images/3_tier_architecture.png) 

**Advantages**
* Effective use of network and distribution of data 
* Roles and responsibilities distributed 
* Easy to add new servers or upgrade existing servers 
* Easy to deploy modules and enhance security 

**Disadvantages** 
* Single point of failure - aka if the server is down, no requests can be made 
* Network congestion - lots of clients simultaneously making requests 
* Complex and expensive

#### Peer-to-peer 
**Problem** 
Need to resolve network congestion and single point of failure (which were weaknesses in the client-server architecture) 

Concepts: 
* You don't contact the host, you contact the node 
* You get the node through contacting the server 

Examples include: 
* Napster 
* Skype 
* Bitcoin 

**Advantages**
* Efficiency 
* Scalability, capacity increases with the number of clients 
* Robustness, data is replicated and immune to singlepoint of failure 

**Disadvantages** 
* Architectural complexity 
* Distrubuted recources are not always aailable 
* More demanding of peers


## TODO: DOn't reall understand peer to peer that weel? 

#### Pipe-and-filter 
#### Central Repository (database)
#### Layered



