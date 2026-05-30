# Use a hashmap where key is the sorted version of string (eat = aet) and value is list of all original strings that match the key (ate, tea, eat).
# Time complexity id O(n log n)

from collections import defaultdict

def groupAnagram(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word to use as key
        key = ''.join(sorted(word))
        anagram_map[key].append(word) # Group by the sorted key

    return list(anagram_map.values())


# refer to most optimal soultion using frequency count from "CommonConcepts&Problems" folder