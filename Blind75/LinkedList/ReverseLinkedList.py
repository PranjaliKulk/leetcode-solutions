class ListNode:
    # define a node structure with value and the pointer next
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_ll(self, head):
        # Define two pointers to reverse LL
        prev = None
        curr = head 

        # Traverse the whole list
        while curr: # while curr is not None (i.e. end of list)

            next_node = curr.next # set up next node before breaking link of nodes

            curr.next = prev # Move direction of node
            prev = curr # update pointer for next iteration
            curr = next_node # update pointer for next iteration
    
        return self.prev # update head to be at prev pointer (prev pointer is at the new head after traversal)

