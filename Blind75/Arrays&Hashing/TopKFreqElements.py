# Naive Approach - sorting - O(n log n)
from collections import defaultdict
def top_k_freq(nums, k):
    frequency = defaultdict(int)

    for n in nums:
        frequency[n] += 1
    
    sorted_by_freq = sorted(frequency, key = lambda x: frequency[x], reverse = True) # order by last
    return sorted_by_freq[:k] # return k

# Most Optimal - Bucket Sort - O(n)
def top_k_bucket(nums, k):
    # Created freq dict
    frequency = defaultdict(int)
    for n in nums:
        frequency[n] += 1

    # create a bucket list for freq len(nums)
    buckets = [[] for _ in range(len(nums)+ 1)] 
    # append values to buckets
    for val,freq in frequency.items(): # .items() gives key, value pairs 
        buckets[freq].append(val)

    # create result list
    result = []
    # Iterate backwards to append to result
    for i in range(len(nums)-1, 0, -1): # (start, end, step) -> start at last, end on first, move backwards
        for val in buckets[i]: # bucket[i] is a list of value, thus for loop
            result.append(val)
        # check if reached k elements
        if len(result) == k:
            return result
        
nums = [1,1,1,2,2,3]
print(top_k_bucket(nums, 2))

