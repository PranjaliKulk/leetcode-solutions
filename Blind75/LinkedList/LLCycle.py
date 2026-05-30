class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def cycle(self, head):
        slow, fast = head, head # technically slow=fast=head works for LL because they are pointers but comma is cleaner. It should not be used for mutable objects.

        while fast and fast.next: # fast will eventually hit none if there is no cycle
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # cycle detected
                return True
        return False