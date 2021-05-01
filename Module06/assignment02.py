from random import randint

# Doubly linked list node
class Node:
    def __init__(self, data):
        '''Create a new node'''
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        '''Create empty Doubly Linked List'''
        self.head = None
        self.tail = None

    def __str__(self):
        the_string = []
        current_node = self.head
        while current_node != None:
            the_string.append(current_node.data)
            current_node = current_node.next
        return f"Head: {self.head.data}; Tail: {self.tail.data}; List: {str(the_string)}"

    def PrintList(self, node=None):
        '''This function prints contents of linked list starting from the given node'''
        if node == None:
            node = self.head
        while node != None:
            print (" % d" % (node.data), end ="")
            node = node.next
        print()

    def Push(self, new_data):
        '''Inserts a new node to the front of list'''
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
        if self.head == None:
            self.tail = new_node
        self.head = new_node

    def Append(self, new_data):
        '''Appends a new node at the end'''
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return

    def InsertAfter(self, prev_node, new_data):
        '''Insert a new node after the given node'''
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next != None:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    # DLL PROBLEMS

    # Palindrome:
    def IsPallindrome(self):
        '''Determine whether a dList is a pallindrome'''
        first = self.head
        last = self.tail
        if self.head == self.tail:
            return True
        while first.next != None:
            if first.data != last.data:
                return False
            first = first.next
            last = last.prev
            if first == last or first.prev == last:
                return True
        return True

    # Reverse:
    def ReverseList(self):
        '''Function to reverse nodes in a dList.'''
        current_node = self.head
        while current_node != None:
            next_node = current_node.next
            current_node.next, current_node.prev = current_node.prev, current_node.next
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    # Kth To Last Value:
    def KthToLast(self, k):
        '''Given k, return the value from the node ‘k’ distance from end of the list.'''
        the_value = None
        if self.tail != None:
            current_node = self.tail
            for i in range(k - 1):
                if current_node != None:
                    current_node = current_node.prev
            the_value = current_node.data if current_node != None else None
        return the_value

print("\n-----===== Start =====-----\n")

my_list = DoublyLinkedList()
length = randint(5,10)
for i in range(length):
    my_list.Append(randint(1,10))

print(f"My List: {my_list}")
print(f"Pallindrome: {my_list.IsPallindrome()}")

my_list.ReverseList()

print(f"Reversed List: {my_list}")

k = randint(1,length)

print(f"Kth to last: K: {k}; Value: {my_list.KthToLast(k)}")

print("\n-----===== End =====-----")