from collections import deque

def reverseK(queue, k):
    if k == 0: #if empty
        return
    
    x = queue.popleft() #remve first element
    reverseK(queue, k-1) #reursively call for remaining elements
    queue.append(x) #add current element to rear

def reverseKElements(queue, k):
    reverseK(queue, k)
    for i in range(len(queue) - k):
        queue.append(queue.popleft())
    return queue