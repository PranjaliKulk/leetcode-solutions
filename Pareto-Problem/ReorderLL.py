# Use fast and slow pointers to get to the middle element
# Reverse second half of the list
# Merge both halves alternatively


def reorderList(self, head):

    # if list has 0m or 1 node, nothing to order
    if head is None or head.next is None: return

    #-----------Find middle of the list-----------------
    slow = head
    fast = head # both pointers pointing to head initially

    # Reach middle element by moving slow by 1 and fast by 2 postions
    while fast is not None and fast.next is not None:
        slow = slow.nwxt
        fast = fast.next.next
    
    #------------Reverse Second Half-------------------
    prev = None # set previous to None initially
    curr = slow.next # next of middle element (beginning of second half)
    slow.next = None # cut list into two halves

    while curr is not None:
        next_node = curr.next # save next node
        curr.next = prev # reverse pointer
        prev = curr # Move prev forward
        curr = next_node # move current forward
    
    second = prev # second half pointer start
    first = head # first half pointer start

    #-------------Merge two halves alternatively--------------
    while second is not None: # end of list
        temp1 = first.next # save next node of first half
        temp2 = second.next # save next node of second half

        first.next = second # link first node to second
        second.next = temp1 # next node from second half to next node from first half

        first = temp1 # Move first pointer ahead
        second = temp2 # Move second pointer ahead