# use a min heap for stream
# Have min heap keep k elements and return heap[0]
# A heap will keep k largest element and 0th element will be kth largest overall

import heapq

class KLargest:
    def __init__(self, nums, k):
        self.k = k
        self.heap = nums # define nums array as heap array
        heapq.heapify(self.heap) # convert heap array to min heap (keeps smallest at 0th position i.e root)

        # keep only k elements, so 0th in heap would be kth overall
        while (self.heap) > self.k:
            heapq.heappop(self.heap)
    
    def addHeap(self, val):
        heapq.heappush(self.heap, val) # add new value to heap

        # check if heap if greater than k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) # keep heap of size k

        return self.heap[0]  #kth largest


#------------------------------------------------------------------------------------------------------------------------
# we cannot use heappush as we go by all the elements like in kth largest in an array because a stream is continous
# and we have to keep checking for every new element being pushed.