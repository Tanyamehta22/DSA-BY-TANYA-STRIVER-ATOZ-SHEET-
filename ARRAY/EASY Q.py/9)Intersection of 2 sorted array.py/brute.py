# METHOD--1 (USING SETS)
# The idea is to add elements of first array in a set. Then, iterate through the second array and check for each element whether it exists in the set. If an element is present in set, it means the element is present in both arrays and the element is added to the output, and its occurrence in the set is removed to avoid duplicates in the output.

# CODE--

# Function to find the intersection of two arrays
def find_intersection(arr1,arr2):
    set1 = set(arr1)

    # Removing duplicates from the first array
    result = []

    # Avoiding duplicates and adding intersections
    for num in arr2:
        if num in set1:
            result.append(num)
            set1.remove(num)

    return result

# Driver code
if __name__ == '__main__':
    arr1=[1,2,4,5,6]
    arr2=[2,3,5,7]


    # Function call
    intersection = find_intersection(arr1,arr2)
    for num in intersection:
        print(num,end=" ")        


# Time Complexity: O(m*log(m) + n*log(n)), where ‘m’ and ‘n’ are the size of the arrays

# Auxiliary Space: O(m + n)