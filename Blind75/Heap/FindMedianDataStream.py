import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self,num):
        # always push to small first
        heapq.heappush(self.small, num)

        # balance values - small top should be <= large top
        # also check if small and large both have values present before comapring
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = - heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes, large heap can only be 1 bigger
        if len(self.small) > len(self.large) + 1:
            val = - heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self):
       
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        
# Time complexity: addNum: O(log n), findMedian: O(1) -> just peaking at the top
# Space complexity: O(n) -> sort n numbers across both heap