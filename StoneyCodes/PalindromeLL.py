def isPalindrome(self):
    fast = self.head
    slow = self.head
    #Find middle of linked list
    while(fast) and (fast.next): #breaks when fast reaches the end
        fast = fast.next.next #increment twice
        slow = slow.next #increment once; returns middle

    #Reverse second half
    prev = None

    while slow!= None:
        next_pointer = slow.next #Move pointer along LL
        slow.next = prev #Change direction, i.e. reverse node
        #update the pointers for next iteration
        prev = slow
        slow = next_pointer

    #Check for palindrome with two pointers
    left = self.head #start
    right = prev #End, prev is last of original LL

    while right != None:
        if left.data != right.data:
            return False #return false if not a match
        #update left and right to next for next compare
        left = left.next
        right = right.next


    return True #return true if all while loop executed