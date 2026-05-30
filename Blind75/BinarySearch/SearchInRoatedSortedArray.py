def search_in_roated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]: # left half is sorted
            if nums[left] <= target < nums[mid]: # target lies in left half
                right = mid - 1
            else: # short circuit else, MUST be right -> go right
                left = mid + 1
        else: # right half is sorted
            if nums[mid] < target <= nums[right]: # target is in right half
                left = mid + 1
            else: # short circuit else, MUST be left -> go left
                right = mid - 1

    return -1 # target not found