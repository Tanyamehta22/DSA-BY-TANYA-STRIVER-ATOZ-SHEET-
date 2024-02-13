# STEPS-

# 1) We pass node* (node pointer) as a reference to the function (as in node* &head)

# 2) Now since the current node pointer is derived from the previous node’s next (which is passed by reference) so now if the value of the current node pointer is changed, the previous next node’s value also gets changed which is the required operation while deleting a node (i.e points previous node’s next to current node’s (containing key) next).

# 3) Find the node containing the given value.

# 4) Store this node to deallocate it later using the free() function.

# 5) Change this node pointer so that it points to its next and by performing this previous node’s next also gets properly linked.


# CODE-

# Python program to delete a node in
# singly linked list recursively
 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
# Deletes the node containing 'data'
# part as val and alter the head of
# the linked list (recursive method)
def deleteNode(head, val):
    # Check if list is empty or we
    # reach at the end of the
    # list.
    if (head == None):
        print("Element not present in the list")
        return -1
    # If current node is the
    # node to be deleted
    if (head.data == val):
        # If it's start of the node head
        # node points to second node
        if head.next: 
            head.data = head.next.data
            head.next = head.next.next
            return 1
        else: return 0
    if deleteNode(head.next, val) == 0:
        head.next = None
        return 1
 
# Utility function to add a
# node in the linked list
# Here we are passing head by
# reference thus no need to
# return it to the main function
def push(head, data):
    newNode = Node(data) 
    newNode.next = head 
    head = newNode 
    return head
 
# Utility function to print
# the linked list (recursive
# method)
def printLL(head):
    if (head == None):
        return
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()
 
# Driver Code
 
# Starting with an empty linked list
head = None
# Adds new element at the
# beginning of the list
head = push(head, 10) 
head = push(head, 12) 
head = push(head, 14) 
head = push(head, 15)
# original list
printLL(head) 
# Call to delete function
deleteNode(head, 20) 
# 20 is not present thus no change
# in the list
printLL(head) 
deleteNode(head, 10) 
printLL(head) 
deleteNode(head, 14) 
printLL(head)


# Output-

# 15 14 12 10 
# Element not present in the list
# 15 14 12 10 
# 15 14 12 
# 15 12 

# Time Complexity: O(n)

# Auxiliary Space: O(n) (due to recursion call stack)