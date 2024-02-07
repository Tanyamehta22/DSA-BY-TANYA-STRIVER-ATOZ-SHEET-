# Singly-linked list-

# Traversal of items can be done in the forward direction only due to the linking of every node to its next node.

# CODE-
# (A NODE CREATION)

# Node class 
class Node: 
  
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class 
  
  
class LinkedList: 
  
    # Function to initialize the Linked List object 
    def __init__(self): 
        self.head = None
