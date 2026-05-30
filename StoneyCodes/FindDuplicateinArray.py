def duplicateArray(nums):
    seen = set() # Empty set for unique elements

    for num in nums:
        if num in seen: #if element found
            return True # Array has duplicates
        seen.add(num)
    return False # No dup found