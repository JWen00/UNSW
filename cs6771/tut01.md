# Tutorial 1 
## Summary 

1) Use `auto` on the RHS 
2) `std::cout`
3)  `std::cin`
4) `std::getline`
5) `const` -> no modification allowed
6) `const&` (const reference) -> also no modification allowed
7) `ranges::swap(x, y)`

### Translate the following c code into c++.
```c
int main() {
  char buffer[100];
  fgets(buffer, 100, stdin);
  printf("%s\n", buffer);
  return 0;
}
```

```c++
auto main() -> int { 
    auto buffer = std::string(); 
    std::getline(std::cin, buffer); 
    std::cout << buffer << "\n"; 
    return 0; 
}
```
### Identify which parts are declarations and which are definitions
```c++ 
int get_age(); // Declaration

// Definition
int main() {
  auto name = std::string{}; // Declaration
  name = "Gary Bai"; // Definition
  std::cout << name << " is " << get_age() << '\n';
  return 0;
}

// Definition
int get_age() {
  return 38;
}
```

### Write a sort_3 function 

```c++ 
void sort3 (int& i, int& j, int& k) { 
    if (i > k) { 
        ranges::swap(j, k); 
    }
    if (j > k) { 
        ranges::swap(k, l); 
    }
    if (i > k) { 
        ranges::swap(j, l); 
    }
```