# same logic as steam

import heapq

def klargest(nums, k):
    # define heap
    heap = []

    for num in nums:
        heapq.heappush(heap, num) # push element in heap

        # check if heap reaches size k
        if len(heap) > k:
            # pop element if heap is greater than k
            heapq.heappop(heap)

    return heap[0] # return 0th element of heap which is kth element overall

# Use QuickSelect for most optimal - used quick sort