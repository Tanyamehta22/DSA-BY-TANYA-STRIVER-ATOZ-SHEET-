# STEPS -

# 1) Initialize a node pointer, current = head.

# 2) Do following while current is not NULL

#     A) If the current value (i.e., current->key) is equal to the key being searched return true.

#     B) Otherwise, move to the next node (current = current->next).

# 3) If the key is not found, return false

# CODE-

# Node class
 
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
# Linked List class
 
 
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
 
    # This function insert a new node at the
    # beginning of the linked list
    def push(self, new_data):
 
        # Create a new Node
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node
 
    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):
 
        # Initialize current to head
        current = self.head
 
        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True  # data found
 
            current = current.next
 
        return False  # Data Not found
 
 
# Driver code
if __name__ == '__main__':
 
    # Start with the empty list
    llist = LinkedList()
    x = 21
     
    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)
 
       # Function call
    if llist.search(x):
        print("Yes")
    else:
        print("No")



# Output-
# Yes

# Time Complexity: O(N), Where N is the number of nodes in the LinkedList

# Auxiliary Space: O(1)        