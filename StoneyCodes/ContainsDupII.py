#Using Sliding Window
def containsDupsII(arr, k):
    seen = set()
    for i, num in enumerate(arr):
        if num in seen: #number is in sliding window range, i.e. k range
            return True
        seen.add(num) #add element to set
        if len(seen)>k: #Maintain sliding window of range k
            seen.remove(arr[i-k]) #range exceeded, remove oldest item, i.e. move sliding window forward
    return False