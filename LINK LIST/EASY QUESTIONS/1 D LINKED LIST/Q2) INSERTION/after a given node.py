# B) To Insert a Node after a Given Node in Linked List

# Approach: 

# To insert a node after a given node in a Linked List, we need to:

# 1)Check if the given node exists or not. 

#    A) If it do not exists, 
#        A.1) terminate the process.

#    B) If the given node exists,

#        B.1) Make the element to be inserted as a new node

#        B.2) Change the next pointer of given node to the new node

#        B.3)Now shift the original next pointer of given node to the next pointer of new node

# CODE-

# This function is in LinkedList class.
# Inserts a new node after the given prev_node. This method is
# defined inside LinkedList class shown above */
def insertAfter(self, prev_node, new_data):
 
    # 1. check if the given prev_node exists
    if prev_node is None:
        print("The given previous node must inLinkedList.")
        return
 
    # 2. Create new node &
    # 3. Put in the data
    new_node = Node(new_data)
 
    # 4. Make next of new Node as next of prev_node
    new_node.next = prev_node.next
 
    # 5. make next of prev_node as new_node
    prev_node.next = new_node


# Complexity Analysis:

# Time complexity: O(1), since prev_node is already given as argument in a method, no need to iterate over list to find prev_node

# Auxiliary Space: O(1) since using constant space to modify pointers    