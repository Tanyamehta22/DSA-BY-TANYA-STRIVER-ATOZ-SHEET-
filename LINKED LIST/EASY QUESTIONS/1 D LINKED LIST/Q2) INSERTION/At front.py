# Given a Linked List, the task is to insert a new node in this given Linked List at the following positions: 

# At the front of the linked list  
# After a given node. 
# At the end of the linked list.



# A)To Insert a Node at the Front/Beginning of Linked List

# Approach: 

# To insert a node at the start/beginning/front of a Linked List, we need to:

# 1) Make the first node of Linked List linked to the new node

# 2) Remove the head from the original first node of Linked List

# 3) Make the new node as the Head of the Linked List.

# CODE-

# This function is in LinkedList class
# Function to insert a new node at the beginning
def push(self, new_data):
 
    # 1 & 2: Allocate the Node &
    # Put in the data
    new_node = Node(new_data)
 
    # 3. Make next of new Node as head
    new_node.next = self.head
 
    # 4. Move the head to point to new Node
    self.head = new_node


# Complexity Analysis:

# Time Complexity: O(1), We have a pointer to the head and we can directly attach a node and change the pointer. So the Time complexity of inserting a node at the head position is O(1) as it does a constant amount of work.
# Auxiliary Space: O(1)