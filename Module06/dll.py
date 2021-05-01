# Doubly linked list node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# create a Doubly Linked List
class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.tail = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        if self.head is None:
            self.tail = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    # Given a node as prev_node, insert a new node after
    # the given node
    def insertAfter(self, prev_node, new_data):

        # 1. Check if the given prev_node is None
        if prev_node is None:
            print ("the given previous node cannot be NULL")
            return

        # 2. allocate new node
        # 3. put in the data
        new_node = Node(new_data)

        # 4. Make net of new node as next of prev node
        new_node.next = prev_node.next

        # 5. Make prev_node as previous of new_node
        prev_node.next = new_node

        # 6. Make prev_node ass previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_nodes's next node
        if new_node.next:
            new_node.next.prev = new_node

        if prev_node == self.tail:
            self.tail = new_node

    # Given a reference to the head of DLL and integer,
    # appends a new node at the end
    def append(self, new_data):

        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(new_data)

        # 3. This new node is going to be the last node,
        # so make next of it as None
        # (It already is initialized as None)

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # 5. Change the next of last node
        self.tail.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = self.tail

        return

    # This function prints contents of linked list
    # starting from the given node
    def printList(self, node):

        print ("\nTraversal in forward direction")
        while node:
            print (" % d" % (node.data), end ="")
            last = node
            node = node.next

        print ("\nTraversal in reverse direction")
        while last:
            print (" % d" % (last.data), end ="")
            last = last.prev

    def kthToLast(self, k):
        cur_node = self.tail
        for i in range(k):
            cur_node = cur_node.prev
        return cur_node

    def isValid(self):
        cur_node = self.head
        next_node = self.head.next
        while next_node is not None:
            if cur_node != next_node.prev:
                return False
            cur_node = next_node
            next_node = next_node.next
        return True

    def isPallindrome(self):
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

    def deleteNode(self, given):
        given.prev.next = given.next
        given.next.prev = given.prev

    def reverseList(self):
        if self.head != None:
            current_node = self.head
            self.head, self.tail = self.tail, self.head
            while current_node.next != None:
                current_node.next, current_node.prev = current_node.prev, current_node.next
                current_node = current_node.prev

# Start with empty list
llist = DoublyLinkedList()

# Insert 6. So the list becomes 6->None
llist.append(6)

# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.push(7)

# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.push(1)

# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.append(4)

# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertAfter(llist.head.next, 8)

print ("Created DLL is: ")
llist.printList(llist.head)
llist.reverseList()
