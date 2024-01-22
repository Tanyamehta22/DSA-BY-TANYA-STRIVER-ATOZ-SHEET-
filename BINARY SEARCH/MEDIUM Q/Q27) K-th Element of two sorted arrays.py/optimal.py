# METHOD (USING BINARY SEARCH)--

# It is mentioned that given arrays are sorted. This gives us some hints to use binary search in them.

# We can part it in such a way that our kth element will be at the end of the left half array. Let’s make some observations. The left portion of the array is made of some elements of both array1 and array2. We can see that all elements of the right half of the array are always larger than the left ones. So, with help of binary search, we will divide arrays into partitions with keeping k elements in the left half. We have to keep in mind that l1 <= r2 and l2 <= r1. Why so? This ensures that left-half elements are always lesser than right elements.

# APPROACH--

# Apply binary search in an array with a small size. Start iterating with two pointers, say left and right. Find the middle of the range. Take elements from low to middle of array1 and the remaining elements from the second array. Then using the condition mentioned above, check if the left half is valid. If valid, print the maximum of both array’s last element. If not, move the range towards the right if l2 > r1, else move the range towards the left if l1 > r2.


# CODE--

def kth_element(nums1, nums2, m, n, k):
    if m > n:
        return kth_element(nums2, nums1, n, m, k)
    low = max(0, k-m)
    high = min(k, n)
    while low <= high:
        cut1 = (low+high)//2
        cut2 = k - cut1
        l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
        l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
        r1 = float('inf') if cut1 == m else nums1[cut1]
        r2 = float('inf') if cut2 == n else nums2[cut2]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1+1
    return 1




if __name__ == '__main__':
    nums1 = [2, 3, 6, 7, 9]
    nums2 = [1, 4, 8, 10]
    m = len(nums1)
    n = len(nums2)
    k = 5
    print(
        f'The element at the kth position in the final sorted array is {kth_element(nums1, nums2, m, n, k)}')




# Output: The element at the kth position in the final sorted array is 6

# Time Complexity : log(min(m,n))

# Reason: We are applying binary search in the array with minimum size among the two. And we know the time complexity of the binary search is log(N) where N is the size of the array. Thus, the time complexity of this approach is log(min(m,n)), where m,n are the sizes of two arrays.

# Space Complexity: O(1)

# Reason: Since no extra data structure is used, making space complexity to O(1).