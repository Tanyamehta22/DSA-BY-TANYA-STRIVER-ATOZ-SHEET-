# METHOD-

# To optimize the space used in the previous approach, we can eliminate the third array used to store the final merged result. After closer examination, we realize that we only need the two middle elements at indices (n1+n2)/2 and ((n1+n2)/2)-1, rather than the entire merged array, to solve the problem effectively.

# We will stick to the same basic approach, but instead of storing elements in a separate array, we will use a counter called ‘cnt’ to represent the imaginary third array’s index. As we traverse through the arrays, when ‘cnt’ reaches either index (n1+n2)/2 or ((n1+n2)/2)-1, we will store that particular element. This way, we can achieve the same goal without using any extra space.

# STEPS-

# 1) We will call the required indices as ind2 = (n1+n2)/2 and ind1 = ((n1+n2)/2)-1. Now we will declare the counter called ‘cnt’ and initialize it with 0.

# 2) Now, as usual, we will take two pointers i and j, where i points to the first element of arr1[] and j points to the first element of arr2[].

# 3) Next, using a while loop( while(i < n1 && j < n2)), we will select two elements i.e. arr1[i] and arr2[j], and consider the smallest one among the two. Then, we will increase that specific pointer by 1.

# In addition to that, in each iteration, we will check if the counter ‘cnt’ hits the indices ind1 or ind2. when ‘cnt’ reaches either index ind1 or ind2, we will store that particular element. We will also increase the ‘cnt’ by 1 every time regardless of matching the conditions.

#         A) If arr1[i] < arr2[j]: Check ‘cnt’ to perform necessary operations and increase i and ‘cnt’ by 1.

#        B) Otherwise: Check ‘cnt’ to perform necessary operations and increase j and ‘cnt’ by 1.

# 4) After that, the left-out elements from both arrays will be copied as it is into the third array. While copying we will again check the above-said conditions for the counter, ‘cnt’ and increase it by 1.

# 5) Now, let’s call the elements at the required indices as ind1el(at ind1) and ind2el(at ind2):

#         A) If the total length i.e. (n1+n2) is even: The median is the average of the two middle elements. median = (ind1el + ind2el) / 2.0.

#         B) If the total length i.e. (n1+n2) is odd: median = ind2el.

# 6) Finally, we will return the value of the median.

# CODE-

def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)
    n = n1 + n2  # total size
    # required indices:
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1

    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1

    # Find the median:
    if n % 2 == 1:
        return float(ind2el)

    return float(ind1el + ind2el) / 2.0


if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))



# Output: The median of two sorted arrays is 6.0

# Complexity Analysis--

# Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
# Reason: We traverse through both arrays linearly.

# Space Complexity: O(1), as we are not using any extra space to solve this problem.