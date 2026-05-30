# Key is atleast one half is always sorted
# Use binary search to eleminate sorted half and keep the unsorted half
# Only the minimum element will break the sorted order
# At any mid if mid > right; minimum element is in the right half

def findMin(nums):
    left = 0
    right = len(nums) -1

    while left < right: # loop until search space narrows to one element
        mid = (left+right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1 # minimum element is on the right side, discard left half
        else:
            right = mid # minimum is on the left side; to discard right half, update right to middle element
    
    return nums[left] # right and left pointing to same number, the minimum element
