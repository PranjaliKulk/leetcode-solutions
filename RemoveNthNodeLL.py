# use fast and slow pointers
# move fast by n nodes 
# when fast reaches none, slow is right before the nth node
# Remove slow.next

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head, n):

    dummy = ListNode(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    # Move fast n+1 steps ahead
    for _ in range (n+1):
        fast = fast.next # now gap between fast and slow is n nodes

    # move both simultaneously until fast reaches none
    while fast is not None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next # remove target node

    return dummy.next # return new head