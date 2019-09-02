# Generics 

#### _..allow **classes and interfaces** to be parameters when defining classes._ 

**Note:**  Java compiler applies strong type checking generic code and issues errors. Hence we can fix these errors at compile-time instead of fixing it at runtime.  

## It's simple! We already use it 

This sounds complicated, but we use generics in our code already. For example: 

```java
// Without Generics 
List list = new ArrayList();
list.add("hello");
String s = (String) list.get(0);

// With Generics
List<String> list = new ArrayList<String>();
list.add("hello");
String s = list.get(0);   // no cast
```
## It's simple pt 2 | Box Classes

When we use the angle brackets (<>), it denotes the specific _type_ parameters. We can have multiple to specify the types passed in. 

> `class name<T1, T2, ..., Tn> { /* ... */ }` 

Consider: 

```java
// Without Generics 
public class Box {
    private Object object;

    public void set(Object object) { this.object = object; }
    public Object get() { return object; }
}

// With Generics 
public class Box<T> {
    // T stands for "Type"
    private T t;

    public void set(T t) { this.t = t; }
    public T get() { return t; }
}

// To instantite an instance of Box 
// using generics you have to fill in 'T' 
Box<Integer> integerBox;
```