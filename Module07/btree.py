
print("\n-----===== Start =====-----\n")

class BinaryTreeTemplate():
    '''Write your own version of a class template that will create a binary tree that can hold values of any data type. Demonstrate the class with a driver program.'''
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def NodeCounter(self):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that counts and returns the number of nodes in the tree. Demonstrate the function in a driver program.'''
        counter = 1
        if self.left != None:
            counter = counter + self.left.NodeCounter()
        if self.right != None:
            counter = counter + self.right.NodeCounter()
        return counter

    def LeafCounter(self):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that counts and returns the number of leaf nodes in the tree. Demonstrate the function in a driver program.'''
        counter = 0
        if self.left != None:
            counter = counter + self.left.LeafCounter()
        if self.right != None:
            counter = counter + self.right.LeafCounter()
        if self.left == None and self.right == None:
            counter += 1
        return counter

    def TreeHeight(self):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that returns the height of the tree. The height of the tree is the number of levels it contains. '''
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
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that returns the height of the tree. The height of the tree is the number of levels it contains. '''
        height = 1
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = leftHeight + self.left.MinTreeHeight()
        if self.right != None:
            rightHeight = rightHeight + self.right.MinTreeHeight()
        height = height + min(leftHeight, rightHeight)
        return height

    def TreeWidth(self):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that returns the width of the tree. The width of the tree is the largest number of nodes in the same level.'''
        queue = []
        queue.append(self)
        if self.left != None or self.right != None:
            if self.left != None:
                queue.put(self.left)
            if self.right != None:
                queue.put(self.right)

    def Add(self, node):
        '''Create an add(val) method on the bst object to add a new value to the tree. This entails creating a btNode with this value and connecting it at the appropriate place in the tree. Note: BSTs can contain duplicate values.'''
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

    def Min(self):
        '''Create a min() method on the bst class that returns the smallest value found in the BST.'''
        minValue = self.data
        if self.left != None:
            minValue = self.left.Min()
        return minValue

    def Size(self):
        '''Write a size() method that returns the number of nodes (values) contained in the tree.'''
        return self.NodeCounter()

    def Contains(self, val):
        '''Create a contains(val) bst method that returns whether the tree contains a given value. Take advantage of the BST’s structure to make this a much more rapid operation than sList.contains() would be.'''
        contained = False
        if val == self.data:
            contained = True
        elif val < self.data and self.left != None:
            val = self.left.Contains(val)
        elif self.right != None:
            val = self.right.Contains(val)
        return contained

    def Max(self):
        '''Create a max() bst method that returns the BST’s largest value.'''
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
        print(abs(maxHeight - minHeight))
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

tree = BinaryTreeTemplate(
    5,
    BinaryTreeTemplate(
        1,
        None,
        BinaryTreeTemplate(
            2,
            None,
            BinaryTreeTemplate(
                3,
                None,
                BinaryTreeTemplate(4)
            )
        )
    ),
    None
)

print(f"Tree Nodes: {tree.NodeCounter()}")
print(f"Tree Leafs: {tree.LeafCounter()}")
print(f"Tree Height: {tree.TreeHeight()}")
print(f"Tree Min Height: {tree.MinTreeHeight()}")
print(f"Tree Superbalanced: {tree.HeightBalanced()}")
print(f"Tree Is Valid: {tree.IsValid()}")
print(f"Tree Second Largest: {tree.SecondLargest()}")


print("\n-----===== End =====-----")
