# METHOD-

# It is given that both arrays are sorted. We need to kth element which will be present when both are merged in a sorted manner. It gives us hints of approaching a solution with merge sort. Why so? If we see an algorithm of merge sort. It includes the following steps.

# 1) Divide the array into two halves.
# 2) Merge them in a sorted way.

# So, we can use the method of merging two sorted arrays.

# APPROACH--

# We will keep two pointers, say p1 and p2, each in two arrays. A counter to keep track of whether we have reached the kth position. Start iterating through both arrays. If array1[p1] < array2[p2], move p1 pointer ahead and increase counter value. If array2[p2] <array1[p1], move p2 pointer ahead and increase counter. When the count is equal to k, return the element in which condition makes the counter value equal to k.


# CODE-

def kthelement(array1, array2, m, n, k):
    p1 = 0
    p2 = 0
    counter = 0
    answer = 0


    while (p1 < m and p2 < n):
        if (counter == k):
            break
        elif (array1[p1] < array2[p2]):
            answer = array1[p1]
            p1 += 1
        else:
            answer = array2[p2]
            p2 += 1
        counter += 1
    if (counter != k):
        if (p1 != m-1):
            answer = array1[k-counter]
        else:
            answer = array2[k-counter]
    return answer




if __name__ == "__main__":
    array1 = [2, 3, 6, 7, 9]
    array2 = [1, 4, 8, 10]
    m = len(array1)
    n = len(array2)
    k = 5
    print("The element at the kth position in the final sorted array is",
          kthelement(array1, array2, m, n, k))



# Output: The element at the kth position in the final sorted array is 6

# Time Complexity :

# We iterate at total k times. This makes time complexity to O(k)

# Space Complexity :

# We do not use any extra data structure and hence, the time complexity is O(1).