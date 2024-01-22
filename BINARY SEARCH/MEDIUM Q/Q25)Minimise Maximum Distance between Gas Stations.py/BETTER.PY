# METHOD ( USING PRIORITY QUEUE/HEAP )--

# In the previous approach, for every gas station, we were finding the index i for which the distance between arr[i+1] and arr[i] is maximum. After that, our job was to place the gas station. Instead of using a loop to find the maximum distance, we can simply use the heap data structure i.e. the priority queue.

# Priority Queue: Priority queue internally uses the heap data structure. In the max heap implementation, the first element is always the greatest of the elements it contains and the rest elements are in decreasing order.

# Thus using a priority queue, we can optimize the search for the maximum distance. We will use the max heap implementation and the elements will be in the form of pairs i.e. <distance, index> as we want the indices sorted based on the distance. As we are using max heap the maximum distance will always be the first element.
    
#     STEPS--

# 1) First, we will declare an array ‘howMany[]’ of size n-1, to keep track of the number of placed gas stations and a priority queue that uses max heap.

# 2) We will insert the first n-1 indices with the respective distance value, arrr[i+1]-arr[i] for every index.

# 3) Next, using a loop we will pick k gas stations one at a time.

# 4) Then we will pick the first element of the priority queue as this is the element with the maximum distance. Let’s call the index ‘secInd’.

# 5) Now we will place the current gas station at ‘secInd’(howMany[secInd]++) and calculate the new section length,

# new_section_length = initial_section_length / (number_of_stations_ inserted+1)
#             = (arr[secInd+1] – arr[secInd]) / (howMany[i] + 1)

# 6) After that, we will again insert the pair <new_section_length, secInd> into the priority queue for further consideration.

# 7) After performing all the steps for k gas stations, the distance at the top of the priority queue will be the answer as we want the maximum distance.

# CODE-

import heapq

def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array.
    howMany = [0] * (n - 1)
    pq = []

    # insert the first n-1 elements into pq
    # with respective distance values:
    for i in range(n - 1):
        heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))

    # Pick and place k gas stations:
    for gasStations in range(1, k + 1):
        # Find the maximum section
        # and insert the gas station:
        tp = heapq.heappop(pq)
        secInd = tp[1]

        # insert the current gas station:
        howMany[secInd] += 1

        inidiff = arr[secInd + 1] - arr[secInd]
        newSecLen = inidiff / (howMany[secInd] + 1)
        heapq.heappush(pq, (newSecLen*(-1), secInd))

    return pq[0][0]*(-1)

arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)


# Output: The answer is: 0.5

# Complexity Analysis--

# Time Complexity: O(nlogn + klogn),  n = size of the given array, k = no. of gas stations to be placed.
# Reason: Insert operation of priority queue takes logn time complexity. O(nlogn) for inserting all the indices with distance values and O(klogn) for placing the gas stations.

# Space Complexity: O(n-1)+O(n-1)
# Reason: The first O(n-1) is for the array to keep track of placed gas stations and the second one is for the priority queue.