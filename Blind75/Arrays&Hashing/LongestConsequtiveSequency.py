# create a set
# check if n-1 is present in set -> if so, not start of sequence
# if not found -> start of sequence
# increment counter till n-1 is present to get sequence length

def longest_consequtive_sequence(nums):
    num_set = set(nums) 
    start = [] # empty list to store all starts of sequence
    for num in num_set:
        if not (num-1) in num_set: #start found
            start.append(num) # append start
    
    max_length = 0
    for val in start:
        current_length = 1 # initialise inside loop rather than outside so it resets
        while (val + current_length) in num_set:
            current_length += 1
        max_length = max(current_length, max_length)
    return max_length


# Without start list: All in one loop: cleaner

def longest_consequtive_sequence(nums):
    num_set = set(nums) 
    max_length = 0
    for num in num_set:
        if (num-1) not in num_set: #start found
            current_length = 1 # initialise inside loop rather than outside so it resets
            while (num + current_length) in num_set:
                current_length += 1
            max_length = max(current_length, max_length)
        
    return max_length

nums = [100,4,200,1,2,3]
print(longest_consequtive_sequence(nums))