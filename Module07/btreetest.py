from queue import Queue
# put(element)
# get(element)

class BinaryTreeTemplate():
    '''Write your own version of a class template that will create a binary tree that can hold values of any data type. Demonstrate the class with a driver program.'''
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def NodeCounter(self):
        '''Write  a member function, for either the template you designed in Q1 or the binaryTree class, that counts and returns the number of nodes in the tree. Demonstrate the function in a driver program.'''
        counter = 1
        if self.left != None:
            counter = counter + self.left.NodeCounter()
        if self.right != None:
            counter = counter + self.right.NodeCounter()
        return counter

    def LeafCounter(self, counter = [0]):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that counts and returns the number of leaf nodes in the tree. Demonstrate the function in a driver program.'''
        if self.left != None:
            self.left.LeafCounter()
        if self.right != None:
            self.right.LeafCounter()
        if self.left == None and self.right == None:
            counter[0] += 1
        return counter[0]

    def TreeHeight(self, leftHeight = 1, rightHeight = 1):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that returns the height of the tree. The height of the tree is the number of levels it contains. '''
        if self.left != None:
            leftHeight = self.left.TreeHeight(leftHeight = leftHeight + 1)
        if self.right != None:
        	rightHeight = self.right.TreeHeight(rightHeight = rightHeight + 1)
        return max(leftHeight, rightHeight)

    def TreeWidth(self):
        '''Write a member function, for either the template you designed in Q1 or the binaryTree class, that returns the width of the tree.  The width of the tree is the largest number of nodes in the same level.'''
        node = self
        que = Queue()
        que.put(node)
        while (not que.empty()):
          node = que.get()
          if (node.left != None):
            que.put(node.left)
          if (node.right != None):
            que.put(node.right)
          print(node.data, end=" ")

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
        pass

    def Size(self):
        '''Write a size() method that returns the number of nodes (values) contained in the tree.'''
        pass

    def Contains(self):
        '''Create a contains(val) bst method that returns whether the tree contains a given value. Take advantage of the BST’s structure to make this a much more rapid operation than sList.contains() would be.'''
        pass

    def Max(self):
        '''Create a max() bst method that returns the BST’s largest value.'''
        pass

    def IsEmpty(self):
        '''Create an isEmpty() method that returns whether BST is empty (empty BSTs contains no values).'''
        pass
        
tree = BinaryTreeTemplate(4, BinaryTreeTemplate(2, BinaryTreeTemplate(1), BinaryTreeTemplate(3)), BinaryTreeTemplate(6, BinaryTreeTemplate(5), BinaryTreeTemplate(7)))
cpyTree = BinaryTreeTemplate(4)
print(tree.NodeCounter())