
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

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        the_string = []
        current_node = self.head
        while current_node != None:
            the_string.append(current_node.data)
            current_node = current_node.next
        return str(the_string)

    def Append(self, data):
        node = LinkedNode(data)
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def CheckCycle(self):
        cycle = False
        visited = set()
        current_node = self.head
        while current_node and not cycle:
            if current_node in visited:
                cycle = True
            visited.add(current_node)
            current_node = current_node.next
        return cycle

my_list = LinkedList()
for i in range(10):
    my_list.Append(randint(1,10))

print(f"My List: {my_list}")
print(f"Contains Cycle: {my_list.CheckCycle()}")

print("\nInsterting Cycle")
my_list.head.next.next.next.next.next = my_list.head.next.next.next
print(f"Contains Cycle: {my_list.CheckCycle()}")

my_new_list = LinkedList()
for i in range(10):
    my_new_list.Append(randint(1,10))

print(f"\nMy New List: {my_new_list}")
print(f"Contains Cycle: {my_new_list.CheckCycle()}")

print("\n-----===== End =====-----")