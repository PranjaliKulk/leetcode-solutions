# Floyds Cycle detection
# Tortoise and Hare problem

def isCycle(self, head):
    slow = head # slow pointer to head initially
    fast = head # fast pointer to head initially

    while fast and fast.next:
        slow = slow.next #move one position
        fast = fast.next.next #move two positions

        # If fast catches up with slow, there is a cycle
        if slow == fast: 
            return True
        
    return False # no cycle