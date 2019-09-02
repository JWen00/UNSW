## Week 10 | User-Centric Design

10 Usability Heuristics for UI Design 

* Visiblity of status 
* Similar system and real world 
* User control and freedom 
* Consistency and holding standards
* Error Prevention 
* Recognition
* Flexibility (Customisation) 
* Aesthetic and minimalist 
* Recognise, diagnose errors 
* Help and documentation 

## Week 9 | Visitor Pattern 
* is a behavioural pattern
* a method for a particular behaviour to 'visit' a node and interact with it 
* lets you separate algorithms from the objects they operate on `node.accept(visitor)`
* PROs: OCP, SRP, can accumulate info while visitng 


## Week 8 | Smells, Refactoring Techniques & Template Pattern

### Code Smells 

**Code Smells**: Poorly written code that is difficult to understand   
**Design Smells**: Poorly written code that is difficult to maintain 
Occurs in structures within implementation including:  
* Bloaters (Classes/Methods which have grown too big in size) 
* OO Abusers (Incorrect application) 
* Change Preventers (Rigid Code) 
* Dispensables (Unnecessary Code) 
* High Coupling ([Feature Envy](https://waog.wordpress.com/2014/08/25/code-smell-feature-envy/), Demeter, [Msg Chains](https://refactoring.guru/smells/message-chains))
* Refused Bequest (Bad inheritance)
* [Divergent Change](https://refactoring.guru/smells/divergent-change) (many changes for one addition) 
* [Shotgun Surgery](https://refactoring.guru/smells/shotgun-surgery) (single responsbility over multiple classes) 

### Solutions 
* Push Down Field/Method
* Extract Class (extract repeated code)
* Inline Method (creating temp variable) 
* Replace temps with queries (so we dont store info)
* Replace method with method object 
* Renaming!!!! (V IMPORTANT) 
* Substitute algorithm
* Intro parameter objs (start-end => period) 
* [Preserve whole objects](https://refactoring.guru/preserve-whole-object) (as opposed to getting each individual and then calculating) 
* Form template method (Similar algorithm in two sublasses) 
* Replace inheritance with delegation 
* Replace conditional with Polymorphism 


## Week 7 | Decorator & Adaptor Patterns 
* Layer each attribute separately 

 > Using tut example: `ChestPlateDecorator(new King());`

* Each attribute all implement a base decorator 
* Layers can differ in order 


## Week 6 | Design by Contract

#### Questions! Which pattern to use for these problems?  
1. Sorting Collections of records in different orders 
> Strategy 
2. Modelling a file System 
> Composite (Directories are the same as files) 
3. Updating a UI component when the state of the program changes 
> Observer
4. Parsing and evluating arithmetic expressions 
> Composite
5. Adjusting brightness based on light sensor 
> State (jokes it's observer) but state works too right? changing state.. and then the observer notices that and changes.. JOKEs

### "_Require no more, promise no less_"

Main Features: 
1. Contract made of: 
    * _requirements_ upon caller made by class
    * _promises_ made by the class to caller 
2. Requirements made up of conditions on: 
    * argument 
    * order of execution 
    * conditions of execution 
    * Pre-conditions
    * Post-conditions
    * Invariants
3. Requirements enforced by throughing exceptions
4. A class's preconditions have to be the same or weaker than the post conditions (to conform the LSP)


## Week 5 | Interfaces, Abstract classes & inheritance

* **Polymorphism** is the ability of an object to take on many forms through inheritance 

* Polymorphism vs Strategy 
    * Inheritance is simpler to code 
    * Strategy is more flexible, allowing for dynamic changes 

## Week 4 | Design Principles 

### Law of Demeter denotes that classes should only talk to its friends so each class can only call:  
* arguments 
* local variables 
* instance variables 
* globals

**Breaking the Law of Demeter causes:**
* Tight Coupling 
* Low Cohesion
* Dependency on other code 

### LKS (LisKov Substitution) denotes that code should work without knowing the actual class (inheritance) 

> This was broken in my dungeon assignment as there were specific checks for classes D': 

**Solutions**
* **BAD**: Patching parent class with a checker 
* **BETTER**: Fixing the inheritance heirarchy 


## Week 3 | Access Modifiers & Fields 

### Access Modifiers 
1. Public
2. Protected
3. Default 
4. Private (Classes cannot be private)

### Fields 
* Final (Classes, Abstract Classes, Methods) 
* Abstract (Only obastract classes) 
* Static (Classes, Methods) 

