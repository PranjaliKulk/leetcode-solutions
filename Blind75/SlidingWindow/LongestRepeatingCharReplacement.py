from collections import defaultdict
def longest_repeating_char_replacement(s, k):
    left = 0
    freq = defaultdict(int)
    best = 0
    max_freq = 0

    for right, c in enumerate(s):
        # add character to frequency
        freq[c] += 1
        max_freq = max(max_freq, freq[c])

        # check if window is valid
        window_size = right - left + 1
        if window_size - max_freq > k: # not valid -> shrink window
            left += 1
            freq[s[left]] -= 1 # can do without, but its good to remove stale values from freq 

        best = max(best, window_size)
    return best

print(longest_repeating_char_replacement("XYYX", 2))