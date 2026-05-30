# True if value appears more than once, else False

# Approach 1 by set
def contains_duplicates(nums):
    # nums_set = set(nums) # convert nums into a set
    # if len(nums) == len(nums_set):
    #     return False # no duplicates found
    # return True # length did not match, duplicates found

    #Instead:
    return len(nums) != len(set(nums)) # One line true false


# Approach 2 by traversing
def contains_duplicate(nums):
    # result = [] # empty result list 

    # for i in range(len(nums)):
    #     if nums[i] in result:
    #         return True # duplicate found
    #     else:
    #         result.append(nums[i]) # append to result

    # return False # duplicate not found

    # Update: result is a list so lookup becomes O(n2), use a set for O(n) lookup
    seen = set() # empty set seen

    for num in range(len(nums)):
        if num in seen:
            return True
        seen.add(nums[num])
    return False