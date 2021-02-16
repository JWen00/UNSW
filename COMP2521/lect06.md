
Directed graph, also known as digraph:

    > The relationship is not mutual
    > You can have self-loops
    You can have parallel edges

Problems to solve:
1. transitive closure
2. shortest path search
3. strong connectivity

    // Lesser

4. Topological sort
5. Graph traveral
6. Page rank

Features of directed graphs:
* Sparse, loosely connected
* Uses an adjacency lists

Terminology:
* in-degree
* out-degree
* sink
* source
* Reachability
* strongly connected
* strong connectivity
* strongly-connected component

Comparing directed graphs to undirected graphs
* adjacency matrix … asymmetric, sparse; less space efficient
* adjacency lists … fairly common solution
    // Easier to understand for directed graphs
* edge lists … order of edge components matters
* linked data structures … pointers inherently directional
Can we make our undirected graph implementations directed? Yes!

> NON-EXAMINABLE - Directed Acylic Graphs (DAG)  
> Tree like because every vertex has children
But also graph like because a child vertex an have a multiple parents

Weighted Graphs
properties:
* Uses geometric interpretations
* Low weight, short edge and viceversa  

How to implement:

1. For adjacency matrices
    Store weight in each cell
    Need some 'no edge exits' values.. (What?)

2. Ajacency list
    Add weight to each node

3. Edge list
    Add weight to each edge

4. LInked data structure
    Links because link and weight pairs

Problems to solve:
* Shortest path problem  
(assumes non-negative weights)  
(assumes non-directed)

Shorter path may have more hops due to the weight differences
Applications:  
* Source-target  
* Single-source  
* all-pairs  

Single Source Shortest Path Search --> Edge relaxation

* Minimum spanning trees
    Whose overal vosts are minimised

Kruskals Algorithm - Go through all the edges by weight

Prims Algorithm - Consider available edges and chose the one with the lowest weight

Final Notes: 

* DFS && BFS   
* DFS Uses a stack  
* BFS Uses a queue  
