# METHOD-

# Add a node after a given node in a Doubly Linked List:


# STEPS-

# 1) Firstly create a new node (say new_node).

# 2) Now insert the data in the new node.

# 3) Point the next of new_node to the next of prev_node.

# 4) Point the next of prev_node to new_node.

# 5) Point the previous of new_node to prev_node.

# 6) Change the pointer of the new node’s previous pointer to new_node.

# CODE-

# Given a node as prev_node, insert
# a new node after the given node
 
 
def insertAfter(self, prev_node, new_data):
 
    # Check if the given prev_node is NULL
    if prev_node is None:
        print("This node doesn't exist in DLL")
        return
 
    # 1. allocate node  & 
    # 2. put in the data
    new_node = Node(data=new_data)
 
    # 3. Make next of new node as next of prev_node
    new_node.next = prev_node.next
 
    # 4. Make the next of prev_node as new_node
    prev_node.next = new_node
 
    # 5. Make prev_node as previous of new_node
    new_node.prev = prev_node
 
    # 6. Change previous of new_node's next node
    if new_node.next is not None:
        new_node.next.prev = new_node


# Time Complexity: O(1)
# Auxiliary Space: O(1)