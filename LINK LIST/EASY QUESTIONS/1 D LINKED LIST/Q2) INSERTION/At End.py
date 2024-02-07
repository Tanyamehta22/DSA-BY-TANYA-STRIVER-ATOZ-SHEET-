# C) To Insert a Node at the End of Linked List

# Approach: 

# To insert a node at the end of a Linked List, we need to:

# 1) Go to the last node of the Linked List

# 2) Change the next pointer of last node from NULL to the new node

# 3) Make the next pointer of new node as NULL to show the end of Linked List


# CODE-

# This function is defined in Linked List class
# Appends a new node at the end. This method is
# defined inside LinkedList class shown above
def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node



# Complexity Analysis:

# Time complexity: O(N), where N is the number of nodes in the linked list. Since there is a loop from head to end, the function does O(n) work. 
# This method can also be optimized to work in O(1) by keeping an extra pointer to the tail of the linked list/

# Auxiliary Space: O(1)      
