# Tutorial 7 

## Summary 
1) *rvalues* and *lvalues* 

These two words are the core to understand how c++ works as a whole. 

*rvalue* means that it's (usually) on the rhs and something that is to be assigned and cannot be a "stand-alone" _(E.g "hello")_

*lvalue* means that it contains a value and can be assigned values _(E.g variables)_ 

2) Templates 

*Note:* template definitions must be `.h` file because files using templates must be able to generate the code at compile time

3) Generics
4) Non-type parameter

This refers to the parameter for the template. _(E.g template<T, int size>)_ 

This is often bad since there will be an instantiaion for every single different sized class/function.

|Type| -
|:--:|:--:|  
|T& | Can be changed to const or T&& (rvalue) with std::move|
|T&& | Can only be converted int const T&
|const T&|  Const cannot change|
 
OR 

 |type|lvalue|const lvalue|rvalue|const rvalue|
 |----|------|------------|------|------------|
|template T&&|True|True|True|True|
 |T&|True|False|False|False|
 |const T&|True|True|True|True|
  |T&&|False|False|True|False|

## Tutorial Exercises

### Identify which of these will not work 
```c++ 
void c_lvalue(const std::string& lvalue);
void lvalue(std::string& lvalue);
void rvalue(std::string&& rvalue);
void value(std::string value);

// "hello" is a const rvalue (T&&)
c_lvalue("hello"); // T&& -> const T&
rvalue("hello");  // T&& -> T&&
value("hello"); 

// s is a lvalue (T&)
std::string s = "world";
rvalue(s); // WONT COMPILE T& -/>T&& (need std move)
value(s);

// lvalue can be passed as const lvalue
c_lvalue(s);            // T& -> const T&
lvalue(s);             // T& -> T&
lvalue("hello");      // WONT COMPILE // T&& -/> T& (only const T&)

c_lvalue(std::move(s)); // T&& -> const T&
rvalue(std::move(s)); // T&& -> T&&
lvalue(std::move(s));  // WONT COMPILE  T&& -/> T& (only const T&)
value(std::move(s)); 

// s2 is a char* but is RVALUE
auto s2 = "goodbye";
lvalue(s2); // WONT COMPILE T&& -/> T& (only const T&)
c_lvalue(s2); // T&& -> const T&
rvalue(s2);  // T&& -> T&&
value(s2);

```
### Convert the class to a templated/generic type
```c++
"stringqueue.h"
class stringqueue {
public:
	stringqueue(int size) 
    : size_curr_{0}, 
      size_max_{size}, 
      queue_{std::make_unique<std::string[]>(size)} {}

	auto enque(std::string s) -> void;
	auto deque() -> std::string;
	auto size() const -> int;
private:
	int size_curr_;
	int size_max_;
	std::unique_ptr<std::string[]> queue_;
}

"stringqueue.cpp"
template<typename T>
stringqueue::enque(std::string s) -> void { 
    if (this->size_curr_ == this->size_max_) { 
        return; 
    }

    this->queue_[size_curr_] = s;
    ++this->size_curr-;
    return;
}
template<typename T>
stringqueue::dequeue(std::string s) -> std::string { 
    if (this->size_curr_ == 0) { 
        throw std::logic_error{"Queue Empty"};
    }
    T item = queue_[0];
	for (auto i = 1; i <= size_curr_; ++i) {
		queue_[i - 1] = queue_[i];
	}
	size_curr_--;
	return item;


}
template<typename T>
stringqueue::size() const -> int { 
    return this->size_curr_;
}

```

