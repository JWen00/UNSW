# Tutorial 9 

## Summary
1) Specialised classes 

We do not specialise functions, only classes. This is because specialising functions can lead to unintended behaviour. It is better to just use overloading for functions. 

We specialise classes when we need to preserve a specific semantic for something that would not work otherwise. 

Or, make an optimisation for a specific type _(E.g `std::vector<bool>` utilises bit-shifting for optimisation)_

2) Type Traits 
```c++
template <typename T>
struct is_a_pointer {
	static auto constexpr value = false;
    // constexpr has value is resolved at compile time
};
```
3) Concepts 

You can add restrictions to both classes and functions 

```c++ 
template <typename T> 
requires (concepts::totally_ordered<T>)
class class_name {
```

```c++
auto fn() const -> T requires (std::is_arithmetic_v<T>) {} 
```

4) `std:forward` 

It 'forwards' the argument as the same type as it was given. 

Use when you pass in a rvalue (which may be converted and you don't want that)

## Tutorial Exercises

### Design your own type trait `is_a_pointer`
```c++
namespace traits {

template <typename T>
struct is_a_pointer {
	static auto constexpr value = false;
};

template <typename T>
struct is_a_pointer<T*> {
	static auto constexpr value = true;
};

} // namespace traits
```

### Use your own type traits to determine if real number of not
```c++
#include <stdexcept>
#include <type_traits>
namespace traits { 
    template<typename T>
    struct is_real_num { 
        static auto constexpr value = std::is_arithmetic<T>; 
    };
}
```

### Caluclate streaming_median
`streaming_median` currently allows the user to use any (ordered) type. This means that the general implementation of median doesn't work on even sized streams, as for many types, such as std::string, there isn't an obvious way to calculate the midpoint between two values.

1) Modify the existing streaming_median class to add a compile time check for whether the parameterized type is arithmetic, to provide an implementation of median() which works for evenly sized streams of arithmetic type.

```c++
template <typename T>
class streaming_median {
 public:
  auto add(T value) -> void { data_.insert(std::move(value)); }

  auto median() const -> T requires (not std::is_arithmetic_v<T> {
    if (data_.empty()) {
      throw std::runtime_error{"Cannot get median of empty stream."};
    }
    if (data_.size() % 2 == 0) { 
      throw std::runtime_error{"Cannot get median of an evenly sized stream"};
    }
  } 
  auto median() const -> T requires (std::is_arithmetic_v<T>) { 
    if (data_.empty()) {
      throw std::runtime_error{"Cannot get median of empty stream."};
    }
    if (data_.size() % 2 == 0) { 
        auto hi = std::next(data_.begin(), data_size() / 2);()
        auto lo = std::prev(hi); 
        return (*hi + *lo) / 2
    }
    return *std::next(data_.begin(), data_.size() / 2);
  }
 private:
  std::multiset<T> data_;
};
```
2) The current solution allows a user to instantiate a streaming_median<T> where T is a type which doesn't have a valid operator<, and thus cannot be ordered properly. Using a requires statement with the concept concepts::totally_ordered, prevent a user from mistakely instantiating a streaming_median with a type which is invalid.

Note: Also simplified median, this is a much better way.

```c++
template <typename T> 
requires (concepts::totally_ordered<T>)
class streaming_median {
 public:
  auto add(T value) -> void { data_.insert(std::move(value)); }

  auto median() const -> T requires (not std::is_arithmetic_v<T> {
    if (data_.empty()) {
      throw std::runtime_error{"Cannot get median of empty stream."};
    }
    if (data_.size() % 2 == 0) { 
      // Evaluate this at compile time.
      if constexpr (!std::is_arithmetic_v<T>) {
        throw std::runtime_error{"Cannot get median of an evenly sized stream."};
      }
      auto hi = std::next(data_.begin(), data_size() / 2);()
      auto lo = std::prev(hi); 
      return (*hi + *lo) / 2
    }
    return *std::next(data_.begin(), data_.size() / 2);
  }
 private:
  std::multiset<T> data_;
};
```

### Identify the interferred types 

```c++
auto main() -> int {
	int i = 5; // i is lvalue
	int& k = i; // k is reference to i, lvalue

	decltype(i) x; // int -> variable
	decltype(k) y; // int& -> lvalue
	decltype(std::move(i)) z; // int&& -> rvalue
	decltype(4.2); // double -> rvalue
}
```
### Fix this implementation of `make_unique`

This code currently doesn't work as the implementation for my_make_unique is incomplete. Complete it through the addition of using std::forward as well as variadic types. To compile with this code, you will need to use types.h which can be found [HERE](https://github.com/cs6771/comp6771/blob/master/lectures/week8/forwarding/types.h) in the github.

```c++
template <typename T>
auto my_make_unique(T item) {
  return std::unique_ptr<T>{new T{item}};
}
  |
  |
  V

// Takes advantage of reference collapsing
// Forward keeps args as rvalues instead of converting it into an lvalue whilst constructing
template <typename T, typename... Args>
auto my_make_unique(Args&&... args) {
  return std::unique_ptr<T>{new T{std::forward<Args>(args)...}};
}

```