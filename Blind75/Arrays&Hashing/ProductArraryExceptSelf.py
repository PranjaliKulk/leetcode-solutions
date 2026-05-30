# Constraint is to not use divide operation.
# Naive approach would be to take product and divide by i

# Idea is to build two arrays left and right -> array stores product of elements to i's left/right
# E.g. nums = [1,2,3,4]
# left = [1,1,2,6] right = [24,12,4,1] result = [24,12,8,6]

def product_array_except_self(nums):
    left = [1] * len(nums)
    for i in range(1, len(nums)): # start at 1 because left[0] will cause a bug doing i-1
        left[i] = left[i-1] * nums[i-1]
    right = [1] * len(nums)
    for i in range(len(nums)-2, -1,-1): # right starts at second last element, loops backwards
        right[i] = right[i+1] * nums[i+1]
    result = []
    for i in range(len(nums)):
        result.append(left[i] * right[i])
    return result

nums = [1,2,3,4]
print(product_array_except_self(nums))


# Can reduce space complexity by only using one array
def product_array_except_self(nums):
    result = [1] * len(nums) # initially result will act as left array from above
    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]
    right = 1 # right is now the accumulating product as we move backwards
    for i in range(len(nums)-2,-1,-1):
        right *= nums[i+1]
        result[i] *= right