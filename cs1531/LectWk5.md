# Software Testing 

A **BUG** is an arroneous hardware or software elemtn of a system that can cause the system to fail. 

> "Testing shows the presence, not the absence of bugs." - Edsger W. Dijktra 

### Types of testing 
1. Black Box Testing 

Test a running program with a set of inputs without looking at the implementation. 

AKA asserting the expected outputs.

2. White Box Testing 

Testing the test data with knowledge of the implementation. 

3. Regression testing 

Verifying software outputs even after the implemtation or design has been refactored. 

### Test coverage 

Test coverate measure the degree to which the specification or code has been exercised by tests. 

### Code coverage 

Code coverage measures the decress which the source code has been tested. 

Code coverage includes: 

#### Equivalence Testing 

Equivalence testing is a black-box testing method. 

It divides the space of all possible outputs into equivalence groups such that the program "behaves the same" on each group. 

> (Wow is is this.. discrete) 

#### Boundary Testing 

Boundary testing is a special case of equivalence testing that focuses on the boundary values of input parameters. 

#### Control-flow Testing
* Statement coverage - execute each statement at least once 
* Edge coverage - Every branch of the control flow is traversed 
* Condition coverage - every condition has TRUE or FALSE outcomes 
* Path coverage - Finds the number of distince paths through the program to be traversed at least once 

> (Wow more discrete ;-;) 
![control-flow-image](/images/control_flow_testing.png) 

#### State-based Testing (Unit Tests) 

* Test fixture - preparation tasks 
* Test case - smallest unit of testing 
* Test suite - collection of test cases
* Test runner - orchestrates the execution of tests 

## Test Driven Development (TDD)

Apparently you should start your software design with writing tests.. 

> Whoops? 

![tdd-diagram](/images/tdd.png)

> More refactoring and reason to refactor covered in week 7

# Summary 
![mind_map_5](/images/mind_map_5.png) 