# Recursion

> "..this value, and the rest of the values.."

#### Examples of recusion

* Using a linked list

    ``` c
    struct node {
        Item item;
        node *next;
    };
    ```

* Finding the length of a list

    ``` c
    size_t list_length (node *curr)
    {
        if (curr == NULL) return 0; // base case
        return 1 + list_length (curr->next); // recursive case
    }
    ```

### Recursion using divide and conquer algos
-----
Divide and conquer algorithms:
    * Divide the input into parts
    * Solve the parts recursively
    * Combine the results into an overal solution

#### Example: Divide and Conquer
Consider the iterative and recursive approach to the divide and conquer algo
**Iterative**
```c
// Find the max no. within the array
// Has complexity: O(n)
int array_max (int a[], size_t n)
{
    int max = a[0];
    for (size_t i = 0; i < n; i++)
        if (a[i] > max) max = a[i];
    return max;
}
```

**Recursive**
```c
// Find the max no. within the array
// Has complexity: O(n)
int array_max (int a[], size_t l, size_t r)
{
    if (l == r) return a[l];
    int m = (l + r) / 2;
    int m1 = array_max (a, l, m);
    int m2 = array_max (a, m + 1, r);
    return (m1 < m2) ? m2 : m1;
}
```

#### Example: Binary Search
Consider the iterative and recursive approach to the binary search algo
**Iterative**
```c
// Complexity O(logn)
ssize_t binary_search (int a[], size_t n, int key)
{
    size_t lo = 0, hi = n - 1;
    while (hi >= lo) {
        size_t mid = (lo + hi) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] > key) hi = mid - 1;
        if (a[mid] < key) lo = mid + 1;
}
return -1;
}
```
**Recursively**
```c
// Complexity O(logn)
ssize_t binary_search (int a[], size_t n, int key)
{
    return binary_search_do (a, 0, n - 1, key);
}
ssize_t binary_search_do (int a[], size_t lo, size_t hi, int key)
{
    if (lo > hi) return -1;
    size_t mid = (lo + hi) / 2;
    if (a[mid] == key) return mid;
    if (a[mid] > key) return binary_search_do (a, lo, mid - 1, key);
    if (a[mid] < key) return binary_search_do (a, mid + 1, hi, key);
    assert (!"unreachable");
}
```

### The Search Problem
-----
Given an input, how can we create an algorithm go give us an output?
~~ Extends to trees ~~
