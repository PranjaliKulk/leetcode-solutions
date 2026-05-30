# True if two strings are anagrams: strings with same chars and length
from collections import Counter
def is_anagram(str1, str2):
    #return len(set(str1)) == len(set(str2)) -> cannot use set because you lose freq count even if same letters
    return Counter(str1) == Counter(str2)

from collections import defaultdict
def is_anagram_two(str1, str2):
    #freq = defaultdict(int)
    # str2 = stack() # define a stack of all letters?
    # for letter in freq:
    #     if letter in str2:
    #         stack.pop()
    # if stack == None: return True

    # Create two dict, compare them
    freq1 = defaultdict(int)
    freq2 = defaultdict(int)

    for c in str1:
        freq1[c] += 1
    for c in str2:
        freq2[c] += 1
    return freq1 == freq2

def is_anagram(str1, str2):
    freq = defaultdict(int)
    for c in str1:
        freq[c] += 1
    
    for c in str2:
        freq[c] -= 1 # decrement count
        if freq[c] < 0:
            return False # str2 has more count than str1
    return True

print(is_anagram("listen", "silent"))
print(is_anagram_two("listen", "silent"))
