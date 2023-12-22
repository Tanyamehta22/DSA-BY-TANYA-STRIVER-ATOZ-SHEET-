# METHOD 2- USING HASHING-

def countfreq(arr,n):

    mp=dict()

    # TRAVERSE THROUGH ARRAY ELEMENTS AND COUNT FREQUENCIES
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] +=1
        else:
            mp[arr[i]]=1


    # TRAVERSE THROUGH MAP AND PRINT FREQUENCIES
    for x in mp:
        print(x,"",mp[x])


# DRIVER CODE-
arr=[10,20,20,10,10,20,5,20]
n=len(arr)
countfreq(arr,n)

# Output
# 5 1
# 20 4
# 10 3
# Complexity Analysis:

# Time Complexity : O(n) 
# Auxiliary Space : O(n)