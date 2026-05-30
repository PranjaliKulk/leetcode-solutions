# use max heap and get first two values (largest two)
# if values are samee -> return 0 else return the difference
# Python does not have max heap so convert all values to negative to use min heap as max heap

import heapq

class Solution:
    def stoneWeight(stones):
        # Use max heap by defining min heap into negative values
        heap = [-s for s in stones] # convert to negative values
        heapq.heapify(heap) # store in heap

        # get first two elements -> 0 and 1 are largest
        while len(heap) > 1:
            # we want to make calculations on positive values (real ones) thus the reconverting of negative sign
            first = - heapq.heappop(heap) 
            second = - heapq.heappop(heap)

        # check if two stones are equal
        if first != second:
            heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0 # return 0th element if present else return 0 