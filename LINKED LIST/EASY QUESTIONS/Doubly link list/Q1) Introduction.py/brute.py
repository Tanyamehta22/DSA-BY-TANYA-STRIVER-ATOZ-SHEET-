# What is Doubly Linked List?

# --A doubly linked list (DLL) is a special type of linked list in which each node contains a pointer to the previous node as well as the next node of the linked list.

# CODE-

# Node of a doubly linked list
 
class Node:
    def __init__(self, next=None, prev=None, data=None):
         
        # reference to next node in DLL
        self.next = next
         
        # reference to previous node in DLL
        self.prev = prev
        self.data = data



# Advantages of Doubly Linked List over the singly linked list:

# 1) A DLL can be traversed in both forward and backward directions. 

# 2) The delete operation in DLL is more efficient if a pointer to the node to be deleted is given. 

# 3) We can quickly insert a new node before a given node. 

# 4) In a singly linked list, to delete a node, a pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using the previous pointer. 



# Disadvantages of Doubly Linked List over the singly linked list:

# 1) Every node of DLL Requires extra space for a previous pointer. It is possible to implement DLL with a single pointer though (See this and this). 

# 2) All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous pointers together with the next pointers. For example in the following functions for insertions at different positions, we need 1 or 2 extra steps to set the previous pointer.



# Applications of Doubly Linked List:

# 1) It is used by web browsers for backward and forward navigation of web pages

# 2) LRU ( Least Recently Used ) / MRU ( Most Recently Used ) Cache are constructed using Doubly Linked Lists.

# 3) Used by various applications to maintain undo and redo functionalities. 

# 4) In Operating Systems, a doubly linked list is maintained by thread scheduler to keep track of processes that are being executed at that time.        