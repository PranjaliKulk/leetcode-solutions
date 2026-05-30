class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length dont match, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        char_count = {} # store frequency of each char

        # Count the char is s
        for ch in s:
            char_count[ch] = char_count.get(ch, 0) + 1

        #count the char in t and keep decreasing as we match
        for ch in t:
            if ch not in char_count:
                return False
            char_count[ch]-=1
            if char_count[ch] == 0:
                del char_count[ch]

        
        # if dict is empty, strings are anagrams
        return len(char_count) == 0

        