# COMP2521 19T0 - Sort Detective Report  

In this lab, the aim is to measure the performance of two sorting programs, without access to the code, and determine which sort algorithm each program implements.

## Background and analysis on the possible sorts 

  * Oblivious Bubble Sort 
    > This bubble sort is done by comparing each adjacent values and traversing through every adjacent value.   
    > It has a worst-case and average complexity of `O(n^2)`  
    > It is generally slower than other other sorts the bigger the input gets  
  * Bubble Sort with early exit
    > This is an improved version of the Oblivious Bubble Sort as it registers
    > whether the input been completely sorted without traversing through all the possibilities.   
    > Early exit Bubble Sort also has a worse-case and average complexity of `O(n^2)` 
    > but it is generally faster thanks to the early exit condition.  
    > Bubble sort is: Unstable, and not in-place  
  * Insertion Sort 
    > Insertion sort is very intuitive as it builds the final sorted array one at a time.
    > It takes a value and 'inserts' it into the correct place.
    > It has a worst case scenario of `O(n^2)` but is slightly faster than bubblesort. 
    > It is practical for small amounts of input but proves to be impractical as the input increases.   
    > Insertion sort is: Stable and in-place
  * Selection Sort 
    > Selection sort is very similar to insertion sort.
    > It takes an element and swaps it with the smallest element to the right of the current element.  
    > It has a worse case scenario of `O(n^2)` but is slightly slower than insertion sort as it has to go through every single element within the array while insertion sort only touches what is out of place
    > Selection sort is: Stable and in-place `
  * Shell Sort, Powers of 4 
    > It is also known as h-sort since it traverses the array sorting every 'h' values and decreases the h value until h equals 1   
    > The powers of 4 shell sort uses '4096,1024,256,64,16,4,1' as its h values. 
    > Shell Sort has a worst-case scenario of O(n^2)` and `O(nlog^2n)`
    > Shell sort is: non-stable and in-place
  * Shell Sort, Sedgewick 
    > It is also known as h-sort since it traverses the array sorting every 'h' values and decreases the h value until h equals 1   
    > Sedgewick's sort in particular uses '4193,1073,281,23,8,1'
  * Psuedo-Bogo Sort 
    > This sort was created as a joke to test the concept of randomness. 
  
  ## Experimental Design 
  
 There are two aspects to our analysis: 
  1. Determine that the sorting programs actually sort correctly;
  2. Measure their performance over a range of inputs and requesting of different outputs (A/D) 
  
 ## Correctness Analysis 
 * In computer sicnece, the correctness of an algorithm is asserted when the output behaviour produces the expected output. *  
 
 To ensure the correctness of our findings, we tested each program against the same inputs: 
  * Random 5     numbers; ascending 
  * Random 10    numbers; ascending 
  * Random 20    numbers; ascending 
  * Random 50    numbers; ascending 
  * Random 100   numbers; ascending 
  * Random 200   numbers; ascending 
  * Random 500   numbers; ascending 
  * Random 1000  numbers; ascending 
  * Random 5     numbers; descending 
  * Random 10    numbers; descending 
  * Random 20    numbers; descending 
  * Random 50    numbers; descending 
  * Random 100   numbers; descending 
  * Random 200   numbers; descending 
  * Random 500   numbers; descending 
  * Random 1000  numbers; descending   

We chose these inputs to ensure that we are able to observe the correct sorting for both SortA and SortB for both descending and acsending. 

 
## Performance Analysis 
 In our performance analysis, we measured how each program’s execution time varied as the size and initial sortedness of the input varied. 
 We tested using much bigger numbers to ensure we see the difference between each sort as the number of inputs up until 100,000. This ensures accuracy. We also ran each test three times and found the average to graph to ensure reliability. 
  
  * Random 10     numbers; ascending && descending  
  * Random 50     numbers; ascending && descending  
  * Random 100    numbers; ascending && descending  
  * Random 1000   numbers; ascending && descending  
  * Random 5000   numbers; ascending && descending  
  * Random 10,000 numbers; ascending && descending  
  * Random 20,000 numbers; ascending && descending  
  * Random 30,000 numbers; ascending && descending  
  * Random 40,000 numbers; ascending && descending  
  * Random 50,000 numbers; ascending && descending  
  * Random 60,000 numbers; ascending && descending  
  * Random 70,000 numbers; ascending && descending  
  * Random 80,000 numbers; ascending && descending  
  * Random 90,000 numbers; ascending && descending  
  * Random 100,000 numbers; ascending  && descending  
 
## Experimental Results 

### Correctness Experiments 
  All test cases had expected outputs and generated their outputs in ascending order. 

### Performance Experiments 
  After graphing both graphs (See Appendix A and B), we observed that both seemed to have a time complexity of `O(n^2)`.  
  Through observing the time taken to sort 100,000 inputs, we saw that SortB is much faster than SortB. (See appendix E)
  
  My partner had: 
   * SortA which took less than 1 second to sort 100,000 inputs. 
   * SortB which took longer than 20 seconds to sort 100,000 inputs. 
  
  My sorts: 
   * SortA took 41 seconds to sort 100,000 inputs. 
   * SortB took 6 seconds to sort 100,000 inputs
 
  From this, I concluded that my two sorts must be a bubble sort of some kind while sort be must be a selection sort or insertion sort. 
  
  For sortA, to decipher which type of bubble sort it was, we tested it against already sorted ascending inputs. 
  If it was much faster for an already sorted input, then it must be an early exit bubble sort. 
  However, if it was the the same time or similar, then it must be an oblivious bubble sort since it is **always** `O(n^2)`. After observing the results, SortA now took less than 10 seconds to sort 100,000 inputs. Hence, from my results, SortA must be an early exit sort. 
  
  For SortB, to decipher whether it was selection sort or insertion sort, we tested it against already sorted ascending inputs. If it was much faster for an already sorted inpuit, then it must be an insertion sort. However, it if was the same time or similar, then it must be a selection sort, since selection sort is **always** `O(n^2)`. After observing the results (See Appendix G) SortB now took less than 1 second to sort 100,000 inputs. (Also less than 1 second to sort 1,000,000 inputs wow) Hence, SortB must be an insertion sort. 
  
## Conclusion 

  In conclusion, from our testing the results are:   
    * SortA is an early exit bubble sort 
    * SortB is an insertion sort 

## Appendix 

Appendix A::   
![Graph for SortA](https://github.com/JWen00/UNSW2521_19t0/edit/master/lab06/SortA_graph.png)

Appendix B::  
![Graph for SortB](https://github.com/JWen00/UNSW2521_19t0/edit/master/lab06/SortB_graph.png) 
 
Appendix C::  
![Table for SortA](https://github.com/JWen00/UNSW2521_19t0/edit/master/lab06/SortA_table.png)

Appendix D::  
![Table for SortB](https://github.com/JWen00/UNSW2521_19t0/edit/master/lab06/SortB_table.png)

Appendix E::   
![Comparison](https://github.com/JWen00/UNSW2521_19t0/edit/master/lab06/AvsB.png)
  


 
