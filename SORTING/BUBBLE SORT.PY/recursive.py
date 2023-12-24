# RECURSIVE BUBBLE SORT-

class bubbleSort:
     """ 
     bubbleSort: 
          function: 
              bubbleSortRecursive : recursive  
                  function to sort array 
              __str__ : format print of array 
              __init__ : constructor  
                  function in python 
          variables: 
              self.array = contains array 
              self.length = length of array 
    """
     
     def __init__(self,array):
        self.array= array
        self.length = len(array)

     def __str__(self):
         return " ".join([str(x) for x in self.array])
     
     def bubbleSortRecursive(self, n=None):
         if n is None:
             n=self.length
         count = 0    

         #Base Case
         if n==1:
             return
          # One pass of bubble sort. After 
        # this pass, the largest element 
        # is moved (or bubbled) to end. 
         for i in range(n-1):
             if self.array[i]>self.array[i+1]:
                 self.array[i],self.array[i+1]=self.array[i+1], self.array[i]
                 count = count+1

        # Check if any recursion happens or not 
        # If any recursion is not happen then return
         if (count==0):
            return
         
         
        # Largest element is fixed, 
        #  recur for remaining array 
         self.bubbleSortRecursive(n-1)

# DRIVER CODE-
def main():
    array = [64,34,25,12,22,11,90]

# creating object for class
sort = bubbleSort(array)

 # Sorting array 
sort.bubbleSortRecursive()
print("Sorted array:\n",sort)

if __name__=="__main__":
    main()



# OUTPUT--
# Sorted array : 
# 11 12 22 25 34 64 90


# Time Complexity: O(n*n)
# Auxiliary Space: O(n)
    

# QUESTIONS--
# 1. Difference between iterative and recursive bubble sort?
# Ans. Recursive bubble sort runs on O(n) auxiliary space complexity whereas iterative bubble sort runs on O(1) auxiliary space complexity.

# 2. Which is faster iterative or recursive bubble sort?
# Ans. Based on the number of comparisons in each method, the recursive bubble sort is better than the iterative bubble sort, but the time complexity for both the methods is same.

# 3. Which sorting method we should prefer more iterative or recursive bubble sort?
# Ans. Both the methods complete the computation at the same time(according to time complexity analysis) but iterative code takes less memory than recursive one, so we should prefer iterative bubble sort more than recursive bubble sort.    




              

     

       
