# Splay Trees 
Within btrees, they can have any height, but for a splay tree, balance is always maintained when inserting a new node. 

### What is balance? 
'Balance' can be referred to as height balanced or breadth balance. This can be calculated by: 
/// TODO How do we calculate it again? ??

### Rotating graphs
In order to maintain balance we use graph rotations. The aim of a rotation is to bring a particular node higher and transform it from a child node to a parent node. 

Rotation is performed as we insert a new node into a splay tree. The rough code is as follows:  
```c 
btree_node *btree_insert_splay(btree_node *tree, Item it) 
{ 
    if (tree is empty) return a newly created node; 

    // Find the difference between the item and the value of the curr_tree 
    if (item is smaller) { 
        if (the left is empty) make a new node there and return tree; 

        // Find the difference on the left 
        if (left_difference is smaller) { // CASE1: Left-Left 
            insert a node at tree->left->left 
            rotate right 
        } else { //CASE2: Left-Right 
            insert a node at tree->left->right 
            rotate left
        } 
    } else if (item is larger) { 
        if (right_difference is smaller) { // CASE3: right-Left 
            // SIMILAR
        } else { //CASE2: right-Right // CASE4: right-right
            // SIMILAR 
        } 
    } 
} 
```

#### Some analysis
Although rotating costs us a great amount of time, it is a good (amortised) overall cost 


