# sort array
# fix i, get two pointers (left and right) to iterate through the remaining list
# add found matches in the resultant list of lists
# Moving pointer logic from two sum
# Time: O(n^2) Space: O(1) #excluding output

def threeSum(nums):
    nums.sort() #Sort the array
    res = [] # result list

    for i in range(len(nums) -2): # there needs to be atleat two elements after i; if we go beyond that we wont have a solution so stop at thrid last
        # skip duplicates for the first number
        if i > 0 and nums[i] == nums[i-1]: continue

        left = i + 1
        right = len(nums) - 1

        while left < right: # traverse whole array for current i element
            total = nums[i] + nums[left] + nums[right]

            if total == 0: # match found
                res.append([nums[i], nums[left], nums[right]])
                # skip duplicates
                # compare two adjecent elements from current pointer; move left and right forward or backwards accrodingly
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    right -= 1
                left += 1
                right -= 1
            
            elif total < 0: # too small -> move left towards right
                left += 1

            else: # too big -> move right towards left
                right -= 1

    return res
