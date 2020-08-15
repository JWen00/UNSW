# Tutorial 3 

## Summary 
1) Lamda Functions `[](){}`

Capture by value: 
* when variable may change, and you require the variable at the current time
* when the lifetime of lambda may exceed the lifeime of a variable 

Capture by reference: 
* when the variable may change and you need it to stay updated
* when the variable is unable to be copied or expensive to copy

## Tutorial Exercises
### Write a function that uses standard algorithms split the string into words that are in the word dict and reconstruct it into a string 
```c++
void print_valid_words(const std::vector<std::string>& valid_words,
                     std::istream& input,
                     std::ostream& output) {
  std::copy_if(
      std::istream_iterator<std::string>{input},
      std::istream_iterator<std::string>{},
      std::ostream_iterator<std::string>{output, " "},
      [&](const std::string& s) {
        return std::find(valid_words.begin(), valid_words.end(), s) != valid_words.end();
      });
}

```


###  write a function that takes in the word list as a stream, and outputs a vector of strings that are the words.
```c++ 
std::vector<std::string> to_word_list(std::istream& input) {
  return {std::istream_iterator<std::string>{input}, std::istream_iterator<std::string>{}};
}
```

### Create Car Class

*Initialiser lists and uniform initialisation* avoid having to construct an object once, and then reassign it to a different value after construction. It is more efficient, and for some types, you will not be able to compile without it.

1) Create a constructor for the car that takes in the manufacturer name (e.g. Toyota) and the number of seats. Ensure that your constructor uses a member initializer list and uniform initialisation. 

A *const-correct* class provides const member functions when no state is changed inside a function, and provides both const and non-const overloads for when a function returns a reference to a data member that the user may be able to modify.

2) Create const member functions to get the manufacturer and number of seats.

3) Create a static data member to keep count of the number of car objects created and a statuc function to return the objec count

4) Create a destructor that decreases the object count when an object is destroyed

```c++
"car.h"
class car {
 public:
  car(): car{"unknown", 4} {}
  car(car const& c): car{c.manufacturer_, c.num_seats_} {}
  car(std::string manufacturer, int n_seats)
    : manufacturer_{ std::move(manufacturer) }, num_seats_{n_seats}
  {
    ++n_objects_;
  }

  ~car() noexcept;

  [[nodiscard]] auto get_manufacturer() const -> const std::string&;
  [[nodiscard]] auto get_num_seats() const -> int;
  void set_num_seats(int num_seats);

  static int get_num_cars();

 private:
  std::string manufacturer_;
  int num_seats_;

  static int n_objects_;
};

"car.cpp"

int car::n_objects_ = 0;

car::~car() noexcept {
  --n_objects_;
}

auto car::get_manufacturer() const -> const std::string& {
  return manufacturer_;
}

auto car::get_num_seats() const -> int {
  return num_seats_;
}

auto car::set_num_seats(int num_seats) -> void {
  num_seats_ = num_seats;
}

auto car::get_num_cars() -> int {
  return n_objects_;
}

```

