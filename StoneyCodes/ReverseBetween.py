class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    #Setting up of pointers for LL
    dummy_head = (-1, ListNode) #dummy head as the head of LL
    left_prev, current_node = dummy_head, head #curr_node to point to every node step by step, left_prev to point to one node before left pointer
    for i in range(left-1):
        left_prev, current_node = current_node, current_node.next #setting up our left_prev and curr node pointers
    #Reversing LL
    prev = None #previous pointer; initially to None
    for i in range(right-left+1): #true for our sublist to reverse
        next_pointer = current_node.next # updating current and next
        current_node.next = prev #changing direction of node
        prev, current_node = current_node, next_pointer #updating pointers for next iteration
    #cleaning up remaining pointers
    left_prev.next.next = current_node
    left_prev.next = prev
    return dummy_head.next #Head of LL; return entire LL

