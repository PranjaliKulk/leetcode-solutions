# Sliding window problem. Use a window to track: max_freq
# window_size - max_freq > k -> too many replacements required thus not valid

from collections import defaultdict

def characterReplacements(s,k):
    count = defaultdict(int) # dictionary to keep character count
    left = 0 # left pointer at beginning of string; intial window
    max_freq = 0
    result = 0

    for right in range(len(s)): #initially right starts at the beginning of the list, then gradually right increases and left shrinks as needed
        count[s[right]] += 1 
        max_freq = max(max_freq, count[s[right]])

        # window size - max_freq > k -> shrink
        while(right -left +1) - max_freq > k: #difference calculates no. of replacemement required; if they are less than k -> valid
            # difference is more than k -> shrink from left
            count[s[left]] -= 1 # remove from dict
            left += 1 # move window forward
        result = max(result, right-left-+1) # max of previous substring vs current is our final result
    
    return result

