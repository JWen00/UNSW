# Tutorial 2 

## Summary 
1) Test Cases 
```c++
require "catch2" 
TEST_CASE("TEST_NAME") { 
    auto i = "Hello";
    SECTION("SECTION_NAME") {
        // Assert Preconditions
        REQUIRE("Hello" == "Hello"); 
        // Assert Post Conditions
        CHECK(i == "Hello");  
    }
}
```
2) Iterators act as the bridge between algorithms and ranges, separating   
    a) Memory-Efficient Data Strucures   
    b) Optimised Algorithms

3) Remember to `#include <algorithm>`. See more: [Algorithms](https://en.cppreference.com/w/cpp/algorithm)  
4) Remember to `#include <absl/container/flat_hash_map.h>` for flat hash maps, and use their implementation of find when required 
5) `std::getline(cin, input)` in a while loop will read until EOF (ctrl+D)
6) Pipelining with

```c++
#include <absl/strings/str_cat.h>
#include <fmt/format.h>
#include <range/v3/action.hpp>
#include <range/v3/range.hpp>
#include <range/v3/view.hpp>
namespace views = ranges::views;
    // Intermediate is a vector of strings
	auto const intermediate = ints
	                        | views::{do_sth}
	                        | views::transform({lamda_fn})
	                        | ranges::to<std::vector>; // Change to vector
    // views::join flattens it to a single string
	auto result = intermediate | views::join | ranges::to<std::string>;

```
7) Lamda Functions 
```c++
	auto fn = []({PARAMS}) {
		return {STH}
	};
```
# Tutorial Questions
### Identify the following algorithms 
```c++
// ranges::find
auto first(std::vector<int> const& v, int const needle) -> std::vector<int>::iterator {
  for (auto i = v.begin(); i != v.end(); ++i) {
    if (*i == needle) {
      return i;
    }
  }
  return v.end();
}

// ranges::rotate
auto second(std::vector<int>& v, std::vector<int>::iterator new_first) -> std::vector<int>::const_iterator {
  auto copy = std::vector<int>(v.begin(), new_first);
  v.erase(v.begin(), new_first);
  return v.insert(v.end(), copy.begin(), copy.end());
}

```

### Write `sort_descending` 
```c++
// Write a function that sorts a vector of strings in descending order.
auto sort_descending(std::vector<std::string> v) -> void { 
    // First sort into ascending order 
    std::sort(v); 
    // Then reverse the order
    std::reverse(v);

    /* Solution: ranges::sort(numbers, ranges::greater{}); */
}

// Note: don't need to return as the the actual vector is passed in

```
### Write `all_unique`
```c++
// Implement an algorithm to determine if a string has all unique characters. You should write two algorithms - first should use an additional data structure, second should not. 

auto all_unique(std::string s) -> bool { 
    auto pre_size = s.size(); 
    return ranges::unique(s) == pre_size; 
}

auto all_unique(std::string s) -> bool { 
    auto set = std::set<std::char>(); // We're supposed to use absl
    for (auto const c : s) { 
        set.insert(c); 
    }
    return s.size() == set.size();
}

// From solution
auto all_unique(std::string s) -> bool { 
    auto set = absl::flat_has_set<char>();
    if (not letters_seen.emplace(letter).second) {
			return false;
		}
    return true;
}

// From solution, adjacent find returns end() if it doesn't find a duplicate
auto all_unique(std::string s) -> bool { 
    ranges::sort(s); 
    return ranges::adjacent_find(s) == word.cend();
}

// From solution, uses pipelining for ranges
auto all_unique_in_place2(std::string word) -> bool {
	ranges::sort(word);
	namespace views = ranges::views;
	return ranges::distance(word | views::unique) == ranges::distance(word);
}

```
### Write `is_permutation`
```c++
// Given two strings, write a function to determine if one string is a permutation of the other
auto is_permutation(std::string a, std::string b) -> bool { 
    ranges::sort(a.begin(), a.end()); 
    ranges::sort(b.begin(), b.end()); 
    return a == b; 
} 

// Note: The good thing about solutions is that they can pass in a const& as opposed to an entire copy. 

// Solutions do something else 
#include <absl/container/flat_hash_map.h>
auto count_letters(std::string const& x) -> absl::flat_hash_map<char, int> {
   auto dictionary = absl::flat_hash_map<char, int>();

   for (auto const letter : x) {
      // `absl::flat_hash_map::find`
      // looks for a key, and returns an iterator to the key/value pair entry in the map. It's different to `ranges::find` --- and better suited --- since it is specialised for hash-table lookups, whereas `ranges::find` is suited for linear searches.

      // With a few exceptions, if there's a member function for a container and a `ranges::` function with the same name, the member function is usually better-suted than the `ranges::` function
      auto result = dictionary.find(letter);
      if (result == dictionary.cend()) {
         dictionary.emplace(letter, 1);
         continue;
      }

      // Here we increment the value part of our key/value pair. We're not allowed to modify the key
      ++result->second;
   }
   return dictionary;
}

auto is_permutation(std::string const& x, std::string const& y) -> bool {
   return count_letters(x) == count_letters(y);
}

```

### Write `int_to_string`
```c++
// Write a program that reads in integers from the character input, converts them to a string, and then writes them to the character output in a list style.
auto main() -> void { 
    auto s = std::string(); 
    auto c = std::int(); 
    while (std::getline(cin, c) && !cin.eof()) { 
        s.append(c); 
    }
    std::cout int_to_string(s);
}
#include <iostream>
#include <absl/strings/str_cat.h>
#include <fmt/format.h>
#include <range/v3/action.hpp>
#include <range/v3/range.hpp>
#include <range/v3/view.hpp>

#include "int_to_string.hpp"

// This is sort of a "grab bag" that exposes you to various content that you saw in Week 2 lectures.
auto int_to_string(std::vector<int> const& ints) -> std::string {
	if (ints.empty()) {
		return "[]";
	}

    // If this were a more complex string, we can do
    // fmt::format("{x}, {y}, {x}", fmt::arg("x", x), fmt::arg("y", y));
    // Note: x appears twice
	auto append_comma = [](int const x) {
		return fmt::format("{}, ", x);
	};

	// Here, we form a range pipeline. `intermediate` builds up a description of a computation we intend to have happen, but haven't actioned yet. This is called lazy computation

	// The "pipe" operator is used to pass information from one part of our description to the next, and allows us to "naturally" read the operation. 
    // This is called "reactive programming". 

    // If we were to adopt the more traditional functional approach, this is how we'd have to format the initialisation of intermediate:

	/* 
	    auto intermediate_part1 = views::common(views::transform(views::drop_last(ints, 1), append_comma));
	    auto const intermediate = std::vector<int>(intermediate_part1.begin(), intermediate_part1.end());
	*/

	// Note that while views are lazy, `ranges::to<std::vector>` (the thing that "constructs a vector out of the preceding range") is not. This is our _action_ "command".

	namespace views = ranges::views;
	auto const intermediate = ints
	                        | views::drop_last(1)
	                        | views::transform(append_comma)
	                        | ranges::to<std::vector>;

	// For very technical reasons, we can't use certain views like `views::join` on something that returns a temporary object. A temporary object is one that hasn't been given a name (i.e. isn't a variable or constant, but still exists in memory). 

	// In the above declaration, there are two lines that return temporaries. The first is `views::transform(append_comma)`, which returns a temporary `std::string` object. This means that we can't put any views after it, and need to store it in an intermediate variable (hence why we've called that constant `intermediate`).

	// The second one is `ranges::to<std::vector>`. That also can't be followed by a view, but it *can* be placed after one that returns a temporary because of how it's designed. `intermediate` is a vector of strings.

	//        Take our intermediate vector of strings,
	//        and join them into a single range,
	//        and then construct a string out of the flattened vector of strings.
	auto result = intermediate | views::join | ranges::to<std::string>;

	// Add the last character
	return result.append(fmt::format("[{}]", ints.back()));
}

```