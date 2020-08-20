# Tutorial 4

## Summary 
1) Overloading should be straightforward and intuitive. 
2) Determining whether we need `friend` keyword
3) `explicit operator {type}() const {}` 

`friend` when the operator doesn't take an instance of the class as the LHS argument.

Not `friend` when the operator does take an instance of the class as the LHS argument  
4) Operator `==, !=, <, >` take in lhs and rhs, they're all friends  
5) Const correctness for subscript overloaders  

## Tutorial Exercises

### Complete the istream operator overload to read in two points from command line.

```c++
std::istream& operator>>(std::istream& is, point& p) {
  return is >> p.x_ >> p.y_;
}

```

### Identify Constructions and Assignments

```cpp
std::vector<int> a(1, 2)   // Constructor (direct initilization). We prefer not to do this.

std::vector<int> a{1, 2}   // Constructor (uniform initilization)

std::vector<int> b = {1, 2} // Constructor (uniform initilization)

std::vector<int> c = a      // Constructor (copy construction)

c = b                       // Assignment (copy assignment)
```
### Make an non-explicit type overload for a double that returns the length from the origin to the point's current coordinates
```cpp
explicit operator double() const { 
  return sqrt(x_ * x_ + y_ * y_);
}
```

### Create a book class in [`book.h`] 

* Write the function definition for a constructor that takes values for name, author, isbn and price and uses a member initializer list to set the value of each data member.
* Write the overloaded == operator to compare if two book objects are identical
* Write the overloaded != operator that calls the already overloaded == operator to return true when two book objects are not identical. 
* Write the overloaded << operator to print out the name, author, isbn and price of a book using std::cout
* Write the overloaded type conversion operator to enable the conversion of the Book class to a std::string in the form of "author, name"
* Write the overloaded < operator to allow you to sort books by their isbn number.

```c++ 
class book { 

  struct member
  public:  
    book(std::string name, std::string author, int isbn, int price) 
    : name_{std::move(name)}, 
      author_{std::move(author)}, 
      isbn_{isbn}, 
      price_{price} {} 

    auto friend operator==(const& book n, const& book m) const -> bool { 
      return (m.name_ == n.name_ && 
              m.author_ == n.author_ && 
              m.isbn_ == n.isbn_ && 
              m.price_ == n.price_)
    } 

    auto friend operator!=(const& book n, const& book m) const -> bool { 
      return !(m == n); 
    }

    auto friend operator<<(std::ostream& out, const& book n) { 
      out << "Name: " << n.name_ << "\n";
      out << "Author: " << n.author_ << "\n";
      out << "ISBN: " << n.isbn_ << "\n";
      out << "Price: " << n.price_ << "\n";
    }

    auto friend operator<(const& book a, const& book b) -> bool { 
      return a.isbn_ < n.isbn_; 
    }

    explicit operator std::string(const& book n) { 
      std::stringstream ss; 
      ss << n.author_ << ", " << n.name_ << "\n";
      return ss.str();
    }

  private: 
    std::string name_; 
    std::string author_; 
    int isbn_; 
    int price_; 
}
```
### Creating overloads for subscript, ensuring CONST Correctness

```c++

// We need 2 overloads of the subscript operator:
	// one for non-const objects which allows them to modify the member, and
	// one for const objects that do NOT allow them to modify the member

	// non-const objects use this
	// const objects can NOT use this (since it returns a reference, which
	// allows the member to be changed)
	auto operator[](int i) -> int& {
		assert(i == 0 || i == 1);
		if (i == 0) {
			return this->x_;
		}
		return this->y_;
	}

	// const objects use this
	auto operator[](int i) const -> int {
		assert(i == 0 || i == 1);
		if (i == 0) {
			return this->x_;
		}
		return this->y_;
	}

```