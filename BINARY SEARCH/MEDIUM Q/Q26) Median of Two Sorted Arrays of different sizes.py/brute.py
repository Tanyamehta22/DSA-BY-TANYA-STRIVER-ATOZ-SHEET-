# METHOD-

# The extremely naive approach is to merge the two sorted arrays and then find the median in that merged array.

# **How to merge two sorted arrays:**

# The word “merge” suggests applying the merge step of the merge sort algorithm. In that step, we essentially perform the same actions as required by this solution. By using two pointers on two given arrays, we fill up the elements into a third array.

# **How to find the median:**

# 1) If the length of the merged array (n1+n2) is even: The median is the average of the two middle elements. index = (n1+n2) / 2, median = (arr3[index] + arr3[index-1]) / 2.0.

# 2) If the length of the merged array (n
# 1+n2) is odd: index = (n1+n2) / 2,
# median = arr3[index].

# STEPS--

# 1) We will use a third array i.e. arr3[] of size (n1+n2) to store the elements of the two sorted arrays. 

# 2) Now, we will take two pointers i and j, where i points to the first element of arr1[] and j points to the first element of arr2[].

# 3) Next, using a while loop( while(i < n1 && j < n2)), we will select two elements i.e. arr1[i] and arr2[j], and consider the smallest one among the two. Then, we will insert the smallest element in the third array and increase that specific pointer by 1.

#            A) If arr1[i] < arr2[j]: Insert arr1[i] into the third array and increase i by 1.

#            B) Otherwise: Insert arr2[j] into the third array and increase j by 1.

# 4) After that, the left-out elements from both arrays will be copied as it is into the third array.

# 5) Now, the third array i.e. arr3[] will be the sorted merged array. Now the median will be the following:
 
#           A) If the length of arr3[] i.e. (n1+n2) is even: The median is the average of the two middle elements. index = (n1+n2) / 2, median = (arr3[index] + arr3[index-1]) / 2.0.

#           B) If the length of arr3[] i.e. (n1+n2) is odd: index = (n1+n2) / 2,
#            median = arr3[index].

# 6) Finally, we will return the value of the median.

# CODE-

def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)

    arr3 = []
    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            arr3.append(a[i])
            i += 1
        else:
            arr3.append(b[j])
            j += 1

    # copy the left-out elements:
    arr3.extend(a[i:])
    arr3.extend(b[j:])

    # Find the median:
    n = n1 + n2
    if n % 2 == 1:
        return float(arr3[n // 2])

    median = (arr3[n // 2] + arr3[(n // 2) - 1]) / 2.0
    return median


if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))



# Output: The median of two sorted arrays is 6.0

# Complexity Analysis--

# Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
# Reason: We traverse through both arrays linearly.

# Space Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
# Reason: We are using an extra array of size (n1+n2) to solve this problem.