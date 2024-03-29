# METHODS-

# INTERCHANGE THE FRONT AND BACK OF EACH NODE AND PUT THE LAST NODE AS HEAD.


# STEPS-

# 1) Traverse the linked list using a pointer

# 2) Swap the prev and next pointers for all nodes

# 3) At last, change the head pointer of the doubly linked list



# CODE-

# A node of the doubly linked list
 
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
class DoublyLinkedList:
     # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
 
    # Function reverse a Doubly Linked List
    def reverse(self):
        temp = None
        current = self.head
 
        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev
 
    # Given a reference to the head of a list and an
    # integer,inserts a new node on the front of list
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
 
        # 5. move the head to point to the new node
        self.head = new_node
 
    def printList(self, node):
        while(node is not None):
            print(node.data, end=' ')
            node = node.next
 
 
# Driver's code
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)
 
    print("\nOriginal Linked List")
    dll.printList(dll.head)
 
    # Function call
    dll.reverse()
 
    print("\nReversed Linked List")
    dll.printList(dll.head)




# Output--

#  Original Linked list 10 8 4 2 
#  Reversed Linked list 2 4 8 10 


# Time Complexity: O(N), where N denotes the number of nodes in the doubly linked list.

# Auxiliary Space: O(1)
 