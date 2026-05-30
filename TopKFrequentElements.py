# Approach 1 : second optinal 
# Time complexity O (n log k), Space O(n)
# Uses min heap of size k and counter 

from collections import Counter
import heapq

def topKelements(nums, k):
    # Count frequencies
    count = Counter(nums) # e.g., {1:3, 2:2, 3:1}

    # Return using minheap nlargest
    return heapq.nlargest(k, count.keys(), key=count.get)

# Approach 2 : Bubble sort
# Bubble sort: compare two adj elements; if right is greater than left -> swap
# For top k frequent elements -> do K passes to get top k in positions
# Time complexity is O(n), space O(k)

def topKFrequentBubbleSort(arr, k):
    n = len(arr)

    for i in range(k): # we only need to perform k passes(not the entire list)
        for j in range(n - i -1): #Get the two adjecent elementts
            if arr[j] > arr[j+1]:
                # swap if left is greater than right
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Return the last k elements
    return arr[-k:] #slice last k (they are at the end)
