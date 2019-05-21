# Revision Questions 

### Describe the importance of software engineering to software development 

* Software engineering aims to develop value to the customer by ensuring a good understanding of the problem domain.  

* Software engineering creates a creative forumulation of ideas to solve the problem based on the problem domain 

* Software engineering breaks down the software development process through its clearly defined requirements engineering phase. 

* Software engineering ensures that software is good, that is, it is not only functional but easily maintable. 

* Software engineering allows for clear structured code. (Software architecture) 
### What are 3 differences betweeen waterfall and agile? 

1. Once code has been submitted for an iteration, in a waterfall methodology, it cannot be touched again. However, in AGILE methodology, it can be changed/refactored 

> Waterfall model follows linear sequential model (requirements/analysis/design/implementation/resting). Each phase must be completed before starting on the next. However, in an AGILE model, all the phases are traversed through within each iteration. 

2. Agile goes through the process of life cycles (analysis/requirements/design/implementation/testing) within each iteration while waterfall focuses on each stage at a time. 

> Kinda the same as 1. 

Another one would be: 
> Waterfall model: Rigid, not open to change in requirements 
> Agile: Flexible and can adjust to change in requirements between iterations 

3. Waterfall does not seek customer feedback while agile methods seek customer feedback to further improve/change design requirements 

* AGILE: Continous client involvement throughout the life-cycle 
Waterfall: Customer is involved only in the beginning and end 

### In O-O Design, explan the meaning of encapsulation and state its benefits 

Encapsulation is hiding the state of an object. 

In Python, this means having private functions/attributes and public attributes. This way, object values cannot be changed directly and must go through an internal process. 

This allows: 
* security 
* less unpredictability of an oject  

### What are the benefits of creating a CRC? 

CRC referrs to Class Responsibility Cards. These cards help us build our UML-Class diagrams as they allow us to brainstorm which classes interact and the methods they require. 

This way we can check that the system accurately represents our solution to the problem domain 

> LOL IT'S Class Responsibility Collallaborator CARDS 

### What is refactoring
 
Refactoring is changing the structure of the code while ensuring that the input and output are still the same. This way we can ensure our code has less design smells when we come back to test/extent/modify our code. 

> Applying transformation to a software's internal workings to make the code sipler and easier understand without 

### How is refactoring important in XP 

Core principals of XP include unpredictability.  

In order to account for changes and maintain a fast paced coding, XP emphasises on continous refactoring. 

XP: 
* Focus on stories within the iteration 
* Simple design 
* Continous refactoring
* Pair programming 
* Daily stand-up meetings

### Describe pipe and filter and outline 2 benefits 

Pipe and filter is a Software Architecture model. 

It filters through data in a linear stream in such a way that the information, after being filtered, is passed on to the next filter. 

All filters work concurrently 

Benefits: 
* Easily maintained by looking at each individual filter 
* Decouples data processing steps 

### Benefits of encapsulation 

* Keeping the attributes private provides a clear definition of the role of the object and increases usability 
* Abstracts the internal workings so that an unpredicted change does not cause a rippling effect (keeps a layer of protection) 

### UML Diagrams 

1. Structural (ie. Class Diagrams) 
2. Behaviour (ie. Use-case Diagrams) 