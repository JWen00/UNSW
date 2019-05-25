# Binary Trees

### Definitions
    * **Parent** has not outgoing edges
    * **Child** has no income edges
    * **Root** node as no parents
    * **Leaf** node has no children
    * **Depth/Level** number of edges from root to that node (starts from 0)

    Other types of trees:
    * **Balanced** trees have minimal height
    * **Degernate** tree has maximal height (Like a linked list)
    * **K-ary** tree's internl nodes have k children
    * **Ordered** trees have contrained data/keys

### Binary Trees
-----
For the nodes in a binary tree, the left subtree is always less than the right subtree

The data structure of a btree looks like:

```c
struct btree_node {
    Item item;
    btree_node *left;
    btree_node *right;
};
```
A recusive function to do a Search on a Binary tree:

```c
// Return the node if found, NULL otherwise
btree_node *btree_search(btree-node *tree, Item key)
{
    if (tree == NULL) return NULL;

    // Value that we compare it to
    int cmp = item_cmp(key, tree->item);
    if (cmp == 0) return tree;
    if (cmp > 0) return btree_search(tree->right, key);
    if (cmp < 0) return btree_search(tree->left, key);

}

int item_cmp(Item key, Item item)
{
    if (key == item) return 0;
    if (key > item) return 1;
    if (key < item) return -1;
}
```

### Btree Traversals
-----

Searching Depth-first:
    * Pre-order traveral (NLR)
    * In-order traversal (LNR)
    * Post-order traversal (LRN)

Searching Breadth-first:
    * level-order traversal (NC.. Node then Children)


### Btree Insertions

    1. Find the location
    2. Create the node
    3. Link the parent
