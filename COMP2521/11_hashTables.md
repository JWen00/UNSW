# Hash Tables 

As a faster and more efficient solution to considering the complexities of all the search methods, hash tables were invented.  

Hash tables use Key-indexed arrays which allow us to get constant-time `O(1)` access.     

We use these tables to:  
  * Map keys into a compact range of index values
  * Store items in an array using an index value 
 
A has table needs three things: 
  1. An array of items (size N) 
  2. A Hash function 
  3. Collision resolution method 

## Different types of hashing 
### Chaining
 If multiple values have the same key, then it is stored ina  linked list. 
 If the table size is small, the long linked list defeats the purpose of a hash table.
### Linear Probing 
 If the current one is full, go into the next one, next one and following that one.. 
 Cannot exceed the size of the hash table.
### Double Hashing  
 A method of collision resolution. If the first key index is occupied, you successively increase by the key of the second hash. However, if the second hash is terribly written, then it'll crash and the computer will be sad.  
 
