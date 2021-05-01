
print("\n-----===== Start =====-----\n")

class BinaryTree():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def InsertLeft(self, value):
        self.left = BinaryTree(value)

    def InsertRight(self, value):
        self.right = BinaryTree(value)

    def Add(self, node):
        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.Add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.Add(node)

    def Size(self):
        '''Counts and returns the number of nodes in the tree.'''
        counter = 1
        if self.left != None:
            counter = counter + self.left.Size()
        if self.right != None:
            counter = counter + self.right.Size()
        return counter

    def LeafCounter(self):
        '''Counts and returns the number of leaf nodes in the tree.'''
        counter = 0
        if self.left != None:
            counter = counter + self.left.LeafCounter()
        if self.right != None:
            counter = counter + self.right.LeafCounter()
        if self.left == None and self.right == None:
            counter += 1
        return counter

    def TreeHeight(self):
        '''Returns the height of the tree. The height of the tree is the number of levels it contains.'''
        height = 1
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = leftHeight + self.left.TreeHeight()
        if self.right != None:
            rightHeight = rightHeight + self.right.TreeHeight()
        height = height + max(leftHeight, rightHeight)
        return height

    def MinTreeHeight(self):
        '''Returns the minimum height of the tree. The minimum height of the tree is the number of levels it contains in it's shortest branch. '''
        height = 1
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = leftHeight + self.left.MinTreeHeight()
        if self.right != None:
            rightHeight = rightHeight + self.right.MinTreeHeight()
        height = height + min(leftHeight, rightHeight)
        return height

    def Contains(self, val):
        '''Returns whether the tree contains a given value.'''
        contained = False
        if val == self.data:
            contained = True
        elif val < self.data and self.left != None:
            val = self.left.Contains(val)
        elif self.right != None:
            val = self.right.Contains(val)
        return contained

    def Min(self):
        '''Returns the smallest value found in the BST.'''
        minValue = self.data
        if self.left != None:
            minValue = self.left.Min()
        return minValue

    def Max(self):
        '''Returns the BST’s largest value.'''
        maxValue = self.data
        if self.right != None:
            maxValue = self.right.Max()
        return maxValue

    def IsEmpty(self):
        '''Create an isEmpty() method that returns whether BST is empty (empty BSTs contains no values).'''
        emptyTree = True
        if self.data != None:
            emptyTree = False
        return emptyTree

    def HeightBalanced(self):
        '''Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).'''
        maxHeight = self.TreeHeight()
        minHeight = self.MinTreeHeight()
        if abs(maxHeight - minHeight) <= 1:
            return True
        return False

    def IsValid(self):
        '''Write a function to check that a binary tree is a valid binary search tree.'''
        IsValid = True
        LeftValid = True
        RightValid = True
        if self.left != None:
            LeftValid = self.left.IsValid()
        if self.right != None:
            RightValid = self.right.IsValid()
        if LeftValid and RightValid:
            if self.left != None:
                if self.left.data > self.data:
                    IsValid = False
            if self.right != None:
                if self.right.data < self.data:
                    IsValid = False
        return IsValid

    def SecondLargest(self):
        value = self.data
        if self.right != None and self.right.right != None:
            value = self.right.SecondLargest()
        return value

tree = BinaryTree(
    5,
    BinaryTree(
        1,
        None,
        BinaryTree(
            2,
            None,
            BinaryTree(
                3,
                None,
                BinaryTree(4)
            )
        )
    ),
    None
)

print(f"Tree Nodes: {tree.Size()}")
print(f"Tree Leafs: {tree.LeafCounter()}")
print(f"Tree Height: {tree.TreeHeight()}")
print(f"Tree Min Height: {tree.MinTreeHeight()}")
print(f"Tree Superbalanced: {tree.HeightBalanced()}")
print(f"Tree Is Valid: {tree.IsValid()}")
print(f"Tree Second Largest: {tree.SecondLargest()}")

print("\n-----===== End =====-----")