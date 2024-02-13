# METHOD-

# Add a node before a given node in a Doubly Linked List

# STEPS-

# 1) Allocate memory for the new node, let it be called new_node.

# 2) Put the data in new_node.

# 3) Set the previous pointer of this new_node as the previous node of the next_node.

# 4) Set the previous pointer of the next_node as the new_node.

# 5) Set the next pointer of this new_node as the next_node.

# 6) Now set the previous pointer of new_node.

#     A) If the previous node of the new_node is not NULL, then set the next pointer of this previous node as new_node.

#     B) Else, if the prev of new_node is NULL, it will be the new head node.



# CODE-

# Given a node as prev_node, insert
# a new node after the given node
 
 
def insertAfter(self, next_node, new_data):
 
    # Check if the given next_node is NULL
    if next_node is None:
        print("This node doesn't exist in DLL")
        return
 
    # 1. Allocate node  & 
    # 2. Put in the data
    new_node = Node(data=new_data)
 
    # 3. Make previous of new node as previous of prev_node
    new_node.prev = next_node.prev
 
    # 4. Make the previous of next_node as new_node
    next_node.prev = new_node
 
    # 5. Make next_node as next of new_node
    new_node.next = next_node
 
    # 6. Change next of new_node's previous node
    if new_node.prev is not None:
        new_node.prev.next = new_node
    else:
        head = new_node
 


# Time Complexity: O(1)
# Auxiliary Space: O(1)