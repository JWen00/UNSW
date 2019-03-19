# Actual Python Programming 

### Creation of Classes 

A class is similar to a blueprint. It is a skeleton which can be used over and over again. 

As we said, it contains attributes and methods. 
For exmaple: 

``` python 

class Person: 
    def __init__(self, name): 
        self._name = name 

    def walking_distance(self, distance): 
        print(self.name, "is walking", distance, "meters") 

person = Person(Jennifer)
person.distance(2000)

```

**Note:** Classes usually begin with capitals (cause y not)   
**Note:** \_\_init\_\_ is called a constructor   
**Note:** For the constructer, it should always be private to ensure encapsulation (as discussed below)

### Encapsulation

This basically means that we don't want the values within the class to be directly accessible. 

> *"We want to preserve the state of our object"*

We can encasupate our code using **getters and setters.** 

#### Getters and Setters 

To access the name from outside of the class, we can create a **getter.**

``` python 

class Person: 
    def __init__(self, name): 
        self.name = name 

    def get_name(self): 
        return self.name

print(person.get_name())
```

Similarly, if we want to set the name from outside of the class, we can create a **setter.** 

``` python 

class Person: 
    def __init__(self, name): 
        self.name = name 

    def get_name(self): 
        return self.name

    def set_name(self, new_name): 
        self.name = new_name

print(person.get_name())
person.set_name("Jenn")
```


### Abstraction and Inheritance

**Abstraction** is the method or organising objects into groups based on common attributes.

**Inheritance** is a programming principle that allows to define parent and child relationships between classes. 