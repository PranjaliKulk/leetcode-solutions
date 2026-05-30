# Use two pointers n apart from each other
# when the fast pointer reaches the end of list, slow pointer points to the node to be deleted

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node_from_end(self, head, n):
        dummy = ListNode(0, head) # dummy points to head (dummy -> 0, head -> 1) (0->1->2->3->4->5)
        slow = dummy
        fast = head

        # move fast n times ahead in the list
        for _ in range(n):
            fast = fast.next 
         # while fast reaches last node
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is not just before the node to delete
        slow.next = slow.next.next 
        return dummy.next



