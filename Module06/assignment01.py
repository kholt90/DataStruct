
# You have a singly-linked list and want to check if it contains a cycle.
# A singly-linked list is built with nodes, where each node has:
# node.next—the next node in the list.
# node.value—the data held in the node. For example, if our linked list stores people in line at the movies, node.value might be the person's name.
# For example:
#   class LinkedListNode(object):

#     def __init__(self, value):
#         self.value = value
#         self.next  = None
# A cycle occurs when a node’s next points back to a previous node in the list. The linked list is no longer linear with a beginning and end—instead, it cycles through a loop of nodes.
# Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

print("\n-----===== Start =====-----\n")

from random import randint

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        the_string = []
        if self.head != None:
            print(a)
            current_node = self.head
            while current_node.next != None:
                print(b)
                the_string.append(current_node.value)
                current_node = current_node.next
        print(the_string)
        return str(the_string)

    def Append(self, data):
        node = LinkedListNode(data)
        print(f"Node: Value")
        if self.head == None:
            self.head == node
            print(self.head.value)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

my_list = LinkedList()
for i in range(10):
    my_list.Append(randint(1,10))

print(f"My list: {my_list}")

print("\n-----===== End =====-----")