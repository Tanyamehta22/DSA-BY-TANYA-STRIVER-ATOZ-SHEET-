# Doubly linked list-

# Traversal of items can be done in both forward and backward directions as every node contains an additional prev pointer that points to the previous node.

# CODE-

# Node of a doubly linked list 
class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next  # reference to next node in DLL 
        self.prev = prev  # reference to previous node in DLL 
        self.data = data 