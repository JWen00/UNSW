# Tutorial 5

## Summary 
1) Const correctness for subscripts (again)
2) Pre vs Post increment/decrement 

* Prefix is preferred as it does not make a copy. Copies are bad!
* Postfix returns a copy of the object's current state prior to the increment/decrement occuring, useful if you're changing the things you're incrementing/decrementing.

3) Smart Pointers 

Smart pointers allow us not forget about memory leaks! More specifically, the move and copy semantics are handled for us, we do not need to allocate or free memory.

4) Shared Ptr vs Unique Ptr 

Shared pointeres are used when
* There is shared ownership
* There is a single owner, but the observers may stick around longer than the owner (Consider ass3)

5) Stack Unwinding 

Stack unwinding is the process of exiting stack frams until there is an exception handler for the function. 

Destructors are called on relevant objects and any exceptions througn whilst calling a destructor will cause `std::terminate` to be called.

6) Exception Safety levels 

1) No-throw (failure transparency) operations are guaranteed to succeed.
2) Strong exception safety, operations may fail but have no side effects 
3) 
## Tutorial Exercises 

### Make this code const-correct so it can compile and run sucessfully

```c++
    [[nodiscard]] operator[](int i) -> int& {
      assert(i == 0 || i == 1);
      if (i == 0) return this->x_;
      else return this->y_;
    }

     [[nodiscard]] operator[](int i) const -> int {
      assert(i == 0 || i == 1);
      if (i == 0) return this->x_;
      else return this->y_;
    }

```


### Make this code rethrow another error to the client

This program currently catches the exception fine within the make_connection function. However, we want the client (the main function) to also log it's own error message "Could not establish connection". How can we use rethrow to achieve this?

> By making another try catch loop around `make_connection`.

```c++ 
auto make_connection(const std::string &uname, const std::string &pword) -> DBConn {
    DBConn db;
    try {
        db.try_connect(uname, pword);
        return db;
    } catch (const std::string &e) {
        std::cout << e << std::endl;
    }
}

int main() {
    Logger l;
    try { 
      make_connection("hsmith", "swagger/10");
    } catch (const std::string &e) { 
      std::cout << e << "Could not establish connection\n";
    }
}

```
### Define your own exception 

This can be done using inheritance with exception classes 
```c++ 
// Domain error is for mathematical functions
// Argument is not part of domain
// We want the same properties as the domain_error but
// to give it a different name for the purposes of distinction
// e.g. sqrt(-1)
using domain_error = std::domain_error;

class inverse_domain_error : public domain_error {};
```