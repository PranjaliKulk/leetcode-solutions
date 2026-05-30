# Use min heap
# push value, index, node for each list head
# pop minimum, add to result, push nodes next
# index is needed because if two nodes have the same value, compare will fail and index will act as a tiebreaker

import heapq

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    dummy = ListNode(0)
    curr = dummy
    heap = []
    
    # step 1 - push all heads into heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node)) # push value, index and node into heap

    # step 2 - keep popping minimum and adding to result
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node 
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next