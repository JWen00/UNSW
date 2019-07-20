# Introduction to OO Programming 

POP-UP words: 
* Classes and objects (objects are instances of classes) 
* Abstraction 
* Encapsulation
* Inheritance

### Creating Classes and Object instances 

``` java
public class Account { 
    int accNo; 
    int bsb;
    float bal; 

    public static void main(String[] args) { 
        Account a1 = new Account(); 
        Account a2 = new Account(); 
    }
}
```
Each class does not necessarily require a **main** method. 

### UMLs - Unified Modelling Language 

Revision: UMLs is either **behavioural** or **structural** 

### Creating packages 

Packages are ways of grouping classes (kinda like import) 

```java 
package Shape; 
public class Circle { 

    static final double pi = 3.14159

    // If you don't initialise an int it initiliases to 0  
    int x, y, r; 

    /* 
        // To have encapsulation
        private x, y, r; 
    */
    public double circum() { 
        return 2 * pi * r; 
    }
}
/* NEW FILE */ 

package Shape; 
public class TestShapes { 

    public static void main(STring[] args) { 

        // Java gets the memory association which can point to x, y, r
        // Initially x, y, z = 0 
        Circle c1 = new Circle();
        
        // Not good to change the values directly 
        c1.x = 5; c1.y = 2; c1.r = 4;

        // When you don't give any values, any of the methods are available  
        System.out.println(c1.area())
    }

}
```

### Creating a constuctor 

```java
package Shape; 
public class Circle { 
    private int x, y, r; 

    public Circle (int x, int y, int r) { 
        this.x = x; 
        this.y = y; 
        this.r = r; 
        
        /* 
            ### There is a problem now.. 
            If you don't create a constructor, you cannot just create an instance with `new Circle();` 

            In that case, you can have a default constructor 
            >>> to be known 
        */
    }
}

```

### Class Variables ==> next 