# METHOD-

# Push the node’s data into the stack while traversing the doubly linked list, then pop out the elements from the stack and copy the value to the nodes of the linked list by again traversing it.

# STEPS-

# 1) Traverse the whole Linked List and  Keep pushing the node’s data into the stack

# 2) Then keep popping the elements out of the stack and updating the Doubly Linked List



# CODE-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
 
    """
    method to reverse a Doubly-Linked List using Stacks
    """
 
    def reverseUsingStacks(self):
 
        stack = []
        temp = self.head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
 
        # Add all the elements in the stack
        # in a sequence to the stack
        temp = self.head
        while temp is not None:
            temp.data = stack.pop()
            temp = temp.next
 
        # Popped all the elements and the
        # added in the linked list,
        # in a reversed order.
 
    """
    method to push a new item before the head
    """
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
 
        if self.head is not None:
            self.head.prev = new_node
 
        self.head = new_node
 
    """
    method to traverse the doubly-linked 
    list and print every node in the list
    """
 
    def printList(self, node):
        while(node is not None):
            print(node.data)
            node = node. next
 
 
# driver's code
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)
 
    print("original doubly-linked list")
    dll.printList(dll.head)
 
    # Function call
    dll.reverseUsingStacks()
 
    print(" reversed doubly-linked list")
    dll.printList(dll.head)



# Output-
# Original linked list 
# 10 8 4 2 
# The reversed Linked List is 
# 2 4 8 10 


# Time Complexity: O(N)
# Auxiliary Space: O(N)
