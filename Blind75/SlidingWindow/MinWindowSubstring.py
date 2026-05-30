from collections import defaultdict
from collections import Counter
def min_window_substring(s, t):
    left = 0
    have = defaultdict(int) # dict to store all chars we currently have in the window
    need = Counter(t) # dict to store all characters we need i.e string t
    formed = 0 # variable to track uniquely formed characters i.e. completed chars 
    required = len(need) # no. of chars we need, initialised to length of string t
    best = ""

    for right, c in enumerate(s):
        have[c] += 1 # add current char to have dict
        if have[c] == need[c]:
            formed += 1 # formed will increase if both dict for that value match
        # to get minimum substring, we need to update best
        while formed == required:
            window = s[left:right + 1]
            if best == "" or len(window) < len(best):
                best = window # update new best value
            # remove char from have before shrinking window
            have[s[left]] -= 1
            # check if formed is still valid after removing char from have
            if have[s[left]] < need[s[left]]:
                formed -= 1 # lost a char, decrement formed
            left += 1 # shrink window
    return best

print(min_window_substring("OUZODYXAZV","XYZ")) 

