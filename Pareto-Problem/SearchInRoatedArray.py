# Check if target lies in left or right sorted half

def searchRoated(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right: # While valid
        mid = (left+right)//2

        if nums[mid] == target: return mid # if mid is target return mid

        # check if left half is sorted
        if nums[left] < nums[mid]: #left half is sorted
            # check if target lies in the left sorted half
            if nums[left] <= target < nums[mid]: # target does lie in left half
                right = mid - 1 # discard right half
            else: 
                left = mid + 1 # discard left half
        # right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1 # discard left half
            else:
                right = mid - 1 # discard right half
    return -1 # target not found
