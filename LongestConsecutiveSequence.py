# use a set
# if num - 1 is NOT in the set; num is beginning of the set -> start counting sequrnce untill it breaks; store max length

def longestConsecutiveSequence(nums):
    num_set = set(nums) # space complexity O(n)
    longest = 0

    for num in num_set:
        # only start from numbers that are sequence starts
        if num - 1 not in num_set:
            current = num
            count = 1

            # start counting sequence till it breaks
            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count) # max if previous count and new count
            
    return longest

