# Trees & Graphs

## Binary Tree Traversal

### Inorder
root -> left -> right

### Preorder
left -> root -> right

### Postorder
left -> right -> root

### Level Order
Traverse the tree one layer at a time
```python
     3
    / \
   9  20
     /  \
    15   7
------------
[
    [3],
    [9, 20],
    [15, 7]
]
```
This is similar to Bread-first Search. The trick is to use a queue, and iterate the length of the queue to store each layer node.

## Graph Search

### Bread-first Search (BFS)

### Depth-first Search (DFS)
