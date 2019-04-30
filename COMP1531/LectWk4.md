# Actual Python Programming (yay)

## Creating Classes 
A class is a blueprint to instantiating (many) instances of objects. 

It is a skeleton which can be used over and over again. 

A class contains *attributes* and *methods*.
``` python 
class ClassName: 
    def __init__(self, attribute): 
        self._attribute = attribute 

    def hello_method(self): 
        print(f'Hello {{attributes}}) 
```
In the example, we have created a simple class which contains one attribute and one method.   

 `__init__` is a *constructor* which essentially sets up the object with the given parameters. 

 All attributes have an underscore to show that it is **private** should not be touched by functions outside of the class. 

> **Note:** Classes usually begin with a capital ONLY as a convention


## Encapsulation 

> *"We want to preserve the state of our object"*

This basically means that we don't want the values within the class to be directly accessible. 

We can encasupate our code using **getters and setters.** 
``` python 
class ClassName: 
    def __init__(self, attribute): 
        self._attribute = attribute 

    @property # The getter 
    def attribute(self): 
        return self._attribute 

    def attribute(self): # NOT a getter
        return self._attribute 
```
In the example, we create a getter using the decorator `@property`.   

This decorator allows us to access the attribute of the object, knowing that it is an attribute, rather than a function.   

Consider: 

```python 
example = ClassName(has_attribute) 

# Using the getter 
print(example.attribute) 
# Returns "has_attribute" 

# Without the getter 
print(example.attribute()) 
# Also returns "has_attribute" but is inefficient

```

The setter operates in a similar manner
``` python 
class ClassName: 
    def __init__(self, attribute): 
        self._attribute = attribute 

    @attribute.setter # The setter
    def attribute(self, new_attribute): 
        self._attribute = new_attribute 
```
## Inheritance and Abstract Classes 

#### Inheritance 

**Inheritance** is a programming principle that allows to define parent and child relationships between classes. 

```python
class Shape: 
    def __init__(self, colour): 
        self._colour = colour

class Circle(Shape): 
    def __init__(self, colour, radius):
        super().__init__(colour) 
        self._radius = radius
```
In the example, we have created a parent class called *Shape* and a child class called *Circle*. 

Here, *Circle* inherits all of *Shape*'s properties (*colour*).

These properties are created using the parent class' constructor through the function `super()` 
> The function is called super as the parent class is also referred t

*Circle* also contains unique properties which do not exist within *Shape* (*radius*) 

In this example, you can instantiate an instance of *Shape* as well as an instance of *Circle*. 

If we wish to only be able instantiate instances of *Circle*, then we need to use Abstraction. 

#### Abtraction
```python
from abc import ABC

class Shape(ABC): 
    def __init__(self, colour): 
        self._colour = colour

    @abstractmethod
    def area(self): 
        pass

class Circle(Shape): 
    def __init__(self, colour, radius): 
        self._colour = colour
        self._radius = radius

    def area(self): 
        return 3.142 * self._radius * self._radius

```
Abstaction requires `from abc import ABC`. 

To make *Shape* an abstract class we specify: `class Shape(ABC)` 

This means we can no longer instantiate objects of type *Shape* 

The decorator `@abstractmethod` means that in each instance of a child class, there MUST be a function called `area`. 

## Exception Handling 

> Covered in week 5 but included it here to better suit the content 

An Exception is an 'error' which occurs during the execution of a program 

Exception handling enables us to handle these type of situations with grace and avoids putting the entire program to a halt. 

#### Syntax of `<try-except-else>` block
```python
try: 
    # Perform operation 
except Exception1:
    # If exception1 occurs, execute.. 
except Exception2: 
    # If exception2 occurs, execute.. 
else: 
    # If there are no exception, execute.. 
finally: 
    # Always execute.. 
```

Common (built-in) exception
* IOError 
* Import Error 
* ValueError
* EOFError 
* ZeroDivisionError
* AssertionError

## Asserts in python 

DO NOTs: 
1. Don't use asserts for data validation or data procressing 
2. Ye that's it..xd