# Heaps

Heaps look the same as Btrees, but instead of going left to right, they go from top to bottom.

They are a good solution for priority queues

### Properties
-----
    * Heap Order (Top to Bottom)
    * Complete Tree
    * Usually implemented with arrays

Their array implementations look like:

    // Need to add in image of array_implementation -->images //

### Heap Insertion
-----
    1. Add new element at the bottom-most, right-most position
    2. Reorganise values along the path to the root to maintain order

```c
// Move the value at a[k] to correct the position
void heap_fixup (Item a[], size_t k)
{
    // While we haven't reached root and the order is wrong.
    while (k < 1 && item_cmp(a[k/2], a[k]) < 0)
    {
        // Swap the parent with the child
        swap(a, k, k/2);
        k = k/2;
    }
}
```
### Heap Deletion

    1. Swap the root value with the bottom-most, right-most value
    2. Remove the that value
    3. Reorganise the values along from root

```c
// Move the value at a[k] to correct position
void heap_fixdown (Item a[], size_t k)
{
    // While are nodes below the one just deleted
    while (2 * k <= N)
    {
        // Get the child of the node
        size_t j = 2 * k;

        // Check if it has two children and pick the bigger one
        if (j < N && item_cmp(a[j], a[j + 1]) < 0) j++;

        // If this child is smaller than it's parent, it is in the right order
        if (item_cmp(a[k], a[j]) >= 0) break;

        // Else swap them
        swap (a, k, j);

        // Move down and fix the child.
        k = j;
    }
}

