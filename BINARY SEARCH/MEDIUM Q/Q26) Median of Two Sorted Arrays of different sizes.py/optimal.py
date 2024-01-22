# METHOD (USING BINARY SEARCH)--

# We are going to use the Binary Search algorithm to optimize the approach.

# **KINDLY SEE VIDEO AND NOTES FOR METHOD**

# STEPS--

# 1) First, we have to make sure that the arr1[] is the smaller array. If not by default, we will just swap the arrays. Our main goal is to consider the smaller array as arr1[].

# 2) Calculate the length of the left half: left = (n1+n2+1) / 2.

# 3) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to n1(i.e. The size of arr1[]).

# 4) Calculate the ‘mid1’ i.e. x and ‘mid2’ i.e. left-x: Now, inside the loop, we will calculate the value of ‘mid1’ using the following formula:

# mid1 = (low+high) // 2 ( ‘//’ refers to integer division)
# mid2 = left-mid1

# 5) Calculate l1, l2, r1, and r2: Generally,
#       a) l1 = arr1[mid1-1]
#       b) l2 = arr2[mid2-1]
#       c) r1 = arr1[mid1]
#       d) r2 = arr2[mid2]
#          The possible values of ‘mid1’ and ‘mid2’ might be 0 and n1 and n2 respectively. So, to handle these cases, we need to store some default values for these four variables. The default value for l1 and l2 will be INT_MIN and for r1 and r2, it will be INT_MAX.

# 6) Eliminate the halves based on the following conditions:

#       a) If l1 <= r2 && l2 <= r1: We have found the answer.

#          a.1) (n1+n2) is odd: Return the median = max(l1, l2).

#          a.2) Otherwise: Return median = (max(l1, l2)+min(r1, r2)) / 2.0

#       b) If l1 > r2: This implies that we have considered more elements from arr1[] than necessary. So, we have to take less elements from arr1[] and more from arr2[]. In such a scenario, we should try smaller values of x. To achieve this, we will eliminate the right half (high = mid1-1).

#       c) If l2 > r1: This implies that we have considered more elements from arr2[] than necessary. So, we have to take less elements from arr2[] and more from arr1[]. In such a scenario, we should try bigger values of x. To achieve this, we will eliminate the left half (low = mid1+1).

# 7) Finally, outside the loop, we will include a dummy return statement just to avoid warnings or errors.

# The steps from 4-6 will be inside a loop and the loop will continue until low crosses high.

# CODE--

def median(a, b):
    n1, n2 = len(a), len(b)
    # if n1 is bigger swap the arrays:
    if n1 > n2:
        return median(b, a)

    n = n1 + n2  # total length
    left = (n1 + n2 + 1) // 2  # length of left half
    # apply binary search:
    low, high = 0, n1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        # calculate l1, l2, r1, and r2;
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1 < n1:
            r1 = a[mid1]
        if mid2 < n2:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0  # dummy statement


a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print("The median of two sorted arrays is {:.1f}".format(median(a, b)))




# Output: The median of two sorted array is 6.0

# Complexity Analysis--

# Time Complexity: O(log(min(n1,n2))), where n1 and n2 are the sizes of two given arrays.
# Reason: We are applying binary search on the range [0, min(n1, n2)].

# Space Complexity: O(1) as no extra space is used.