# dummy node to keep smaller of two nodes from two lists
# return dummy.next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(self, list1, list2):
    dummy = ListNode(0) #Create dummy node to simplify merging
    current = dummy # pointer to build the merged list

    # traverse list1 and list2 while both have nodes
    while list1 and list2:
        # check smaller value in if else
        if list1 <= list2:
            current.next = list1 # Attach list1 node
            list1 = list1.next # move pointer forward
        
        else:
            current.next  = list2
            list2 = list2.next

        current = current.next #Move merged list pointer forward
    
    # if list1 has nodes left
    if list1:
        current.next = list1 # Attach remaining nodes from list1

    if list2:
        current.next = list2 # Attach remaining nodes from list2

    return dummy.next #dummy was none, thus return dummy.next
