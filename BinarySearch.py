# Binary search works with sorted lists; mostly in increasing order

def binarySearch(nums, target):
    left = 0 #left pointer set to beginning of the list
    right = len(nums) -1 # right pointer set to end of the list

    while left <= right: # while range is valid, left does not exceed right index
        mid = (left+right) // 2 # calculate index of middle element of the list
        
        if nums[mid] == target: return mid # found target at middle index

        elif nums[mid] < target:
            left = mid + 1 #if mid is too small; discard left half and begin pointer after the middle value
        else:
            right = mid -1 #if mid is too long; discard right half and begin right pointer before mid

    return -1 # target not found