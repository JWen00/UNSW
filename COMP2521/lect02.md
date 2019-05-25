# Complexity

### Definitions
-----
    * **problem**: Something that needs to be solved
    * **algorithm**: well-defined instructions to solve the problem
    * **program**: implementation of the algorithm
    * **process**: an instance of the program being executed

### Algorithm Efficiency
-----
    We can test an algoritms efficienty through measuring it's properties:
    * Run-time using *time*
    * profiling tools like *gprof(1)*
    * performance counters like *pmc(3), hwpmc(4)*

### On run-time execution..
-----
    To measure run-time execution we use:
    `time ./program_name`
    Which will give us a result that looks something like:
    ```
    ./prog 0.01s user 0.02s system 97% cpu 0.028 total
    0k shared 0k local 11k max 0+3280 faults
    13+0 in 0+0+0 out 4 vcsw 4 ivcsw
    ```

    We are interested in the *relative* change in run-time and the problem size increases

#### Example: Searching in a Sorted Array

> Given an array *a* of *n* elements,  where for indicies *i*, *j* are both smaller than n, search for an element *e* in the array

``` c
int a[N]; // array with N items
bool found = 0;
bool finished = false;
int i = 0;
while ((i < N) && (! found)) {&& (! finished)) {
    found = (a[i] == e);
    finished = (e < a[i]);
    i++;
}

```

In an array of size *n*:

    * Best case scenario we make <n comparisons (t(n) ~ O(1))
    * Worse case scenario we make n comparisons (t(n) ~ O(N))
    * Hence the average case is (t(n) ~ O(n/2)).


### Time complexity
-----
We often use the **Big-O notation** to represent the worst case complexity (WCET)

Name   | Notation | Explanation
-------|:--------:|------------------------
constant| O(1)| Independant of input size
logarithmic| O(log n)| Divide and conquer algorithms
linear|O(n)| Every element of the input has to be processed
n-log-n|O(nlogn)| divide and conquer algorithms where split/recombine is proportional to input
quadratic| O(n^2)| compute every input with every other input
cubic |O(n^3)| .. misery
factorial| O(n!)|..real misery
exponsntial |O(2^n)|.. basically runs forever
tractable| -- |an algorithm exists and is denoted by some *P*
intractable| -- | no tractable algorithm, feasible for only a small n , and is denoted by *NP*
non-computable| -- | no algorithm exists (or can)
