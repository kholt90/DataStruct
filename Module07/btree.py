
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
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = 1 + self.left.LeafCounter()
        if self.right != None:
            rightHeight = 1 + self.right.LeafCounter()
        return max(leftHeight, rightHeight)

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
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

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


tree1 = BinaryTreeTemplate(1)

tree2 = BinaryTreeTemplate(1,
        BinaryTreeTemplate(2),
        BinaryTreeTemplate(3)
    )

tree3 = BinaryTreeTemplate(1,
        BinaryTreeTemplate(2,
            BinaryTreeTemplate(4),
            BinaryTreeTemplate(5)
        ),
        BinaryTreeTemplate(3,
            BinaryTreeTemplate(6),
            BinaryTreeTemplate(7)
        )
    )

print()
print(f"Tree1 Nodes: {tree1.NodeCounter()}")
print(f"Tree1 Leafs: {tree1.LeafCounter()}")
print(f"Tree1 Height: {tree1.TreeHeight()}")
print()
print(f"Tree2 Nodes: {tree2.NodeCounter()}")
print(f"Tree2 Leafs: {tree2.LeafCounter()}")
print(f"Tree2 Height: {tree2.TreeHeight()}")
print()
print(f"Tree3 Nodes: {tree3.NodeCounter()}")
print(f"Tree3 Leafs: {tree3.LeafCounter()}")
print(f"Tree3 Height: {tree3.TreeHeight()}")
