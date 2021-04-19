# Tree Types

https://www.bigocheatsheet.com/

https://www.educba.com/types-of-trees-in-data-structure/

## General Tree

General trees have no constraints on the number of child nodes.

```python
class GeneralTree:
    def __init__(self):
        data = None
        children = []
```

# Binary Tree

There can only be two children per parent node. These are usually referred to as left child and right child.

```python
class BinaryTree:
    def __init__(self):
        data = None
        leftChild = None
        rightChild = None
```

## Binary Search Tree

In a BST, the left child must be less than the parent node and the right child must be greater than the parent node.

```python
class BinarySearchTree:
    def __init__(self):
        data = None
        leftChild = None # Must be less than data
        rightChild = None # Must be greater than data
```

## AVL Tree

A dynamically balanced tree. A balance factor is determined and rotations performed if adding a node imbalances the tree.

```python
class AVLTree:
    def __init__(self):
        root = None
        balance = height(left-subtree) − height(right-subtree)
        leftChild = None
        rightChild = None

    def LeftRotation(self):
        pass

    def RightRotation(self):
        pass

    def LeftRightRotation(self):
        pass

    def RightLeftRotation(self):
        pass
```

## Red-Black Tree

```python
class RedBlackTree:
    def __init__(self):
        root = None
        color = 0
        leftChild = None
        rightChild = None
```

https://towardsdatascience.com/8-useful-tree-data-structures-worth-knowing-8532c7231e8c

## Treap

A treap is and heap tree and is a binary search tree.

Each node has a key and a priority. The keys follow the binary-search-tree property. The priorities (which are random values) follow the heap property.

```python
class Treap:
    def __init__(self):
        key = None
        priority = 0
        leftChild = None
        rightChild = None
```

## B-tree

A B tree is a search tree that has multiple nodes that to keep data sorted

```python
class BTree:
    def __init__(self):

```