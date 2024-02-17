# METHOD-

# The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one at the bottom of the stack. 

# STEPS-

# 1) Create a stack and push all the elements in it.

# 2) Call reverse(), which will pop all the elements from the stack and pass the popped element to function insert_at_bottom()

# 3) Whenever insert_at_bottom() is called it will insert the passed element at the bottom of the stack.

# 4) Print the stack         



# CODE-

# Python program to reverse a
# stack using recursion
 
# Below is a recursive function
# that inserts an element
# at the bottom of a stack.
 
 
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 
# Below is the function that
# reverses the given stack
# using insertAtBottom()
 
 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
 
# Below is a complete running
# program for testing above
# functions.
 
# Function to create a stack.
# It initializes size of stack
# as 0
 
 
def createStack():
    stack = []
    return stack
 
# Function to check if
# the stack is empty
 
 
def isEmpty(stack):
    return len(stack) == 0
 
# Function to push an
# item to stack
 
 
def push(stack, item):
    stack.append(item)
 
# Function to pop an
# item from stack
 
 
def pop(stack):
 
    # If stack is empty
    # then error
    if(isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
# Function to print the stack
 
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
    print()
 
# Driver Code
 
 
stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)



# Output-

# Original Stack
# 4 3 2 1 

# Reversed Stack
# 1 2 3 4 


# Time Complexity: O(N2).

# Auxiliary Space: O(N) use of Stack 