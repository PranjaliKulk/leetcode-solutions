def find_min_in_roated_sorted_array(nums):
    left, right = 0, len(nums) - 1
    mid = 0

    while left < right:
        mid = (left+right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1 # min is in the right half
        else:
            right = mid  # middle is in the left half, include mid too because mid could be minimum
    return nums[left] # loop ends when left = rigtht, thats our minimum
