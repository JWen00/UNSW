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
        self._name = name 

    def get_name(self): 
        return self.name

print(person.get_name())
```

Similarly, if we want to set the name from outside of the class, we can create a **setter.** 

``` python 

class Person: 
    def __init__(self, name): 
        self._name = name 

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

#### Example of inheritance: 
```python
class Shape: 
    def __init__(self, colour): 
        self._colour = colour

class Circle(Shape): 
    def __init__(self, colour, radius): 
        self._colour = colour
        self._radius = radius
```

Here, you **cannot** instantiate a shape directly. However you **can** instantiate a circle. 

#### Example without using abstract method: 

If we want to have the same functions for the sub-classses as the parent class so I have written the functions many times :( 
    

```python
class Shape: 
    def __init__(self, colour): 
        self._colour = colour

    @property 
    def area(self): 
        pass

    # Note: the decorator `@property` means that
    # When we call the function we can call: 
    # shape.area rather than shape.area() 

class Circle(Shape): 
    def __init__(self, colour, radius): 
        self._colour = colour
        self._radius = radius

    def get_area(self): 
        return 3.142 * self._radius * self._radius

# This does NOT work
random_shape = Shape(white) 

# This also doesn't work 
print(random_shape.get_area()) 

# This, DOES work
c = Circle("white", 5) 
print(c.get_area())

```

#### Example using **super()**: 

```python

from abc import ABC, abstractmethod 

class Shape: 
    def __init__(self, colour): 
        self._colour = colour

    @abstractmethod 
    def get_area(self): 
        pass 

class Circle(Shape): 
    def __init__(self, colour, radius):
        super().__init__(colour) 
        self._colour = colour
        self._radius = radius

    get_area(self): 
        return return 3.142 * self._radius * self._radius

```

Two new things: 
1. super() calls and runs all the functions of the parent class 

2. @abstractmethod means you MUST implement the same functions within the sub-classes of the current class 

### Association Relationships in OOP 

**Aggregation** is when a child can exist independently from its parent. It is drawn in a UML by a white diamond. 

**Composition** is when a child cannot exist independently from its parent. It is drawn in a UML by a black diamond. 

`Refer to Engine example`

### Decorators 

Decorators refer to the '@' symbol above functions. They can wrap around a function and make it do a particular step before the function works. 

Some decorators which we have seen before include '@property' and '@setter.property' 

#### For example - Without using decorators 

```python 
def hello(): 
    msg = ("Hi Jennifer!")

    def greeter(): 
        print(msg) 
    
    return greeter

hello()
# Calling greeter() will return an error. 
```
This function would return "Hi Jennifer!" as you would expect.   

Something to notice is the function greeter within the function hello. 

"greeter" only has access to the local scope of the outer function "hello" 

#### For Example - Using decorators 

```python

```