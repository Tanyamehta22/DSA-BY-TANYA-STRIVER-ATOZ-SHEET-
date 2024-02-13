# METHOD-

# Inserting a new node in a doubly linked list is very similar to inserting new node in linked list. There is a little extra work required to maintain the link of the previous node. A node can be inserted in a Doubly Linked List in four ways:

# 1) At the front of the DLL. 
# 2) In between two nodes

#     A) After a given node.
#     B) Before a given node.

# 3) At the end of the DLL.


# 1) AT THW FRONT OF THE DLL-

# STEPS-

# The new node is always added before the head of the given Linked List. The task can be performed by using the following 5 steps:

# 1) Firstly, allocate a new node (say new_node).

# 2) Now put the required data in the new node.

# 3) Make the next of new_node point to the current head of the doubly linked list.

# 4) Make the previous of the current head point to new_node.

# 5) Lastly, point head to new_node.



# CODE--

# Adding a node at the front of the list
def push(self, new_data):
 
    # 1 & 2: Allocate the Node & Put in the data
    new_node = Node(data=new_data)
 
    # 3. Make next of new node as head and previous as NULL
    new_node.next = self.head
    new_node.prev = None
 
    # 4. change prev of head node to new node
    if self.head is not None:
        self.head.prev = new_node
 
    # 5. move the head to point to the new node
    self.head = new_node



# Time Complexity: O(1)
# Auxiliary Space: O(1)