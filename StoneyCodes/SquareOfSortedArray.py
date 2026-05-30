#O(n) O(1)
from collections import deque
def sqSortArray(arr):
    l,r = 0, len(arr) -1 #left and right to start and end of array
    q = deque() #empty deque

    while l <= r: #while boundaries are valid
        left, right = abs(arr[l]), abs(arr[r]) #Store absolute values for negative numbers
        if arr[l] > arr[r]:
            q.append(left*left) #add to queue the square of element
            l +=1 #increment left pointer

        else:
            q.append(right*right) #append square of right pointer element to queue
            r -=1 #decrement right by 1

    return list(q)

