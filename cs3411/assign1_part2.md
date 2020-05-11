# cs3411 Assign1 Part 2 
Written by Jennifer Wen Xu 
z5207930 

## Question 1: Search Algorithms for the 15-puzzle 

### (a) Table 

|    |start10|start12|start20|start30|start40|
|:--:|:-----:|:-----:|:-----:|:-----:|:-----:|
|UCS |2565   |Mem    |Mem    |Mem    |Mem    |
|IDS |2407   |13812  |5297410|Time   |Time   |
|A*  |33     |26     |915    |Mem    |Mem    |
|IDA*|29     |21     |952    |17297  |112571 |

### (b) Discussion

From our table, we can see that: 
* UCS uses large amounts of memory, only being able to perform start10. 
* IDS is not very efficient as the number of nodes almost matches UCS and although it uses less memory, it still takes ~5,000,000 expanded states for start 20, and Time for the rest. 
* A* is much more efficient than UCS and IDS, however because it stores all generated nodes in its memory, by start30, it uses too much memory to be effienct. 
* IDA* is similar to A* except it's a depth first approach and hence as the search space becomes bigger, it utilises less memory. 

Overall, we can see that IDA* is the most efficient and consistant search algorithm out of the 4. 

## Question 2: Heuristic Path Search for 15-puzzle 

### (a) Table 

|      |start 50       |start60         |start64          |
|:----:|:-------------:|:--------------:|:---------------:| 
|IDA*  |G=50 N=14642512|G=60 N=321252368|G=64 N=1209086782| 
|1.2   |G=52 N=191438  |G=62 N=230681   |G=66 N=431033    | 
|1.4   |G=66 N=116342  |G=82 N=4432     |G=94 N=190278    |
|1.6   |G=100 N=33504  |G=148 N=55626   |G=162 N=234848   |
|greedy|G=164 N=5447   |G=166 N=1617    |G=184 N=2174     |

### (b/c) Heuristic Path Search Algorithm 

From Week 3 Tutorial, we are given the equation 

```
f(n) = (2-w)*g(n) + w*h(n)
```

Since A* uses 

```
f(n) = g(n) + h(n)
```

we can alter the code like below: 

```
    G2 is G1 * 0.8,
    H2 is H1 * 1.2,
    F1 is G2 + H2,
```

### Discussion 

Before we start our discussion, it is important to note that IDA* uses `f(n)` when `w = 1` and greedy search uses `f(n)`when `w=2` and the values in between allow us to consider the tradeoffs while we move from using `f(n) = g(n) + h(n)` (A* Search) to `f(n) = 2h(n)`(Greedy Search).

In our table, we are able to see a trend as w increases from 1 to 2, the length of the path, G, increases while the number of nodes, N, expanded decreases. This trend applies to start50, 60 and 64. 

We know that our search is guaranteed to be optimal when 0 <= w <= 1 because A* search ensures that h(n) is admissible. However when w > 1, we are not guaranteed for it to be optimal. Hence for w values 1.2, 1.4, 1.6 and greedy search it is not a optimal search, as indicated by the G values greater than the most optimal path length @50, 60 and 64.  

However, greedy search's space complexity is much better than that of A* searches. We can see that with just a little more incorporation of h(n) where `w = 1.2` the nodes expanded is almost half for start50 and considerably less for start60 and 64. 

A particularly interesting case is observed when `w = 1.4` while running start60. This is most likely an outlier as it does not belong within our trend of increasing G and decreasing N. It may have occurred due to pure luck where it found the goal within it's first few searches.  