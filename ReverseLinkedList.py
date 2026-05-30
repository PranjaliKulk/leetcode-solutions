# prev, curr, next node pointers
# Reverse curr.next and move pointers ahead

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # store value of node
        self.next = next #pointer to next

class Solution:
    def reversweList(self, head):
        
        prev = None # prev node points to none initially
        curr = head # current node is at beginning

        # Traverse entire list
        while curr is not None: #till list is valid
            
            next_node = curr.next # Save the next node before breaking link

            curr.next = prev # reverse the pointer
            prev = curr #Move prev one step forward
            curr = next_node # move curr one step forward

        self.head = prev
        return prev #Prev becomes head after reversal