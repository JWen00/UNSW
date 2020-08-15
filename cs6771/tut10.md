# Tutorial 10 

## Summary

More on OOP
1) Protected 

Things that can be used by child classes (derived classes) but not accessible to the public.

2) Virtual 
 
Functions which my be overwritten in child classes 

Setting a virtual function to `=0` makes it an abstract function (aka every child class must have it's own implentation of that function) 

3) Constructing and Deconstructing

Constructing constructs in order of superclass, private fields and then itself. 

Destructing is the reverse 

4) Out of scope deconstructing 

Deconstructs in order of appearance. 
