# Slidng Window with set or hashmap
# Move two pointers (left and right) to maintain a window with unique chars
# if you hit a duplicate, shrink window from left
# Time: O(n) Space: O(k) for all chars (worst case scenario, longest unique string)

def lengthOfLongesrSubstring(s):
    char_set = set() # a set to track chars in a window
    left = 0 # sart of window
    max_len = 0 # result

    for right in range(len(s)):
        # Shrink a window if dupliacte found
        while s[right] in char_set:
            char_set.remove(s[left]) #remove from window found dups
            left +=1

        # Add a current char to window
        char_set.add(s[right])
        # Update result
        max_len = max(max_len, right - left + 1)

    return max_len
