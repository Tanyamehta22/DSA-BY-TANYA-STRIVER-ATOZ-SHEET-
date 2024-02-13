# METHOD-
# An iterative approach for finding the length of the linked list:
    
# STEPS-

# 1) Initialize count as 0 

# 2) Initialize a node pointer, current = head.

# 3) Do following while current is not NULL

#     A) current = current -> next

#     B) Increment count by 1.

# 4) Return count 

# CODE-

#  Node class
 
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
 
    def push(self, new_data):
 
        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node
 
    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
 
    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count
 
 
# Driver code
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
     
    # Function call
    print("Count of nodes is :", llist.getCount())



# Output-
# count of nodes is 5

# Time complexity: O(N), Where N is the size of the linked list

# Auxiliary Space: O(1), As constant extra space is used.