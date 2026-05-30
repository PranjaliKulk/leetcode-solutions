class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder(self,head):

        # Find middle of LinkedList
        slow, fast = head, head 
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            # Middle is now at slow
            # cut the list in half by using second
            second = slow.next
            slow.next = None

        # Reverse Second half
        prev = None
        curr = second 

        # Traverse the whole list
        while curr: # while curr is not None (i.e. end of list)

            next_node = curr.next # set up next node before breaking link of nodes

            curr.next = prev # Move direction of node
            prev = curr # update pointer for next iteration
            curr = next_node # update pointer for next iteration
        second = prev # second now points to reversed head; prev

        # Merge Two halves (Not using sorted merge becuase reorder just merges without comparing values)
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2