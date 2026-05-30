def longest_substring_wo_repeating_chars(s):

    left = 0
    seen = set()
    best = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left]) # shrink until duplicate removed
            left += 1
        seen.add(s[right]) # increment window to add new unseen element to window
        best = max(best, right - left + 1) # update new best window
    return best

print(longest_substring_wo_repeating_chars("abcabcbb"))
