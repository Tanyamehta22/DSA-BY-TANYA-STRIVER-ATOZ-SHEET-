# STEPS-

# 1) Find the previous node of the node to be deleted. 

# 2) Change the next of the previous node. 

# 3) Free memory for the node to be deleted.


# CODE-

# Python program to implement the above approach
class Node:
    # constructor to initialize the node object
    def __init__(self, data):
        self.number = data
        self.next = None
 
 
def push(head, A):
    n = Node(A)
    n.number = A
    n.next = head
    head = n
    return head
 
 
def deleteN(head, position):
    temp = head
    prev = head
    for i in range(0, position):
        if i == 0 and position == 1:
            head = head.next
 
        else:
            if i == position-1 and temp is not None:
                prev.next = temp.next
            else:
                prev = temp
 
                # Position was greater than
                # number of nodes in the list
                if prev is None:
                    break
                temp = temp.next
    return head
 
 
def printList(head):
    while(head):
        if head.next == None:
            print("[", head.number, "] ", "[", hex(id(head)), "]->", "nil")
        else:
            print("[", head.number, "] ", "[", hex(
                id(head)), "]->", hex(id(head.next)))
        head = head.next
    print("")
    print("")
 
 
head = Node(0)
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)
 
printList(head)
 
# Delete any position from list
head = deleteN(head, 1)
printList(head)



# Output-
# [3] [0x1b212c0]->0x1b212a0
# [2] [0x1b212a0]->0x1b21280
# [1] [0x1b21280]->0x1b21260
# [0] [0x1b21260]->(nil)


# [2] [0x1b212a0]->0x1b21280
# [1] [0x1b21280]->0x1b21260
# [0] [0x1b21260]->(nil)

# Time Complexity: O(n)

# Auxiliary Space: O(1)