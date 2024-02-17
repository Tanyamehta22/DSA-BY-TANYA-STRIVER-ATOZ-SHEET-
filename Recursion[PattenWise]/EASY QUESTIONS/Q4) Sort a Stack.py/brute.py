# METHOD--

# The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one in sorted order. and then print the stack.


# STEPS-

# 1) Create a stack and push all the elements in it.

# 2) Call sortStack(), which will pop an element from the stack and pass the popped element to function sortInserted(), then it will keep calling itself until the stack is empty.

# 3) Whenever sortInserted() is called it will insert the passed element in stack in sorted order.

# 4) Print the stack  


# CODE --

# Recursive method to insert element in sorted way
 
 
def sortedInsert(s, element):
 
    # Base case: Either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
 
        # Remove the top item and recur
        temp = s.pop()
        sortedInsert(s, element)
 
        # Put back the top item removed earlier
        s.append(temp)
 
# Method to sort stack
 
 
def sortStack(s):
 
    # If stack is not empty
    if len(s) != 0:
 
        # Remove the top item
        temp = s.pop()
 
        # Sort remaining stack
        sortStack(s)
 
        # Push the top item back in sorted stack
        sortedInsert(s, temp)
 
# Printing contents of stack
 
 
def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    s = []
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
 
    print("Stack elements before sorting: ")
    printStack(s)
 
    sortStack(s)
 
    print("\nStack elements after sorting: ")
    printStack(s)
 


# Time Complexity: O(N2). 

# Auxiliary Space: O(N) use of Stack