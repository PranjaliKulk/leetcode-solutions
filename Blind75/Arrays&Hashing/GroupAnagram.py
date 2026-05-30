from collections import defaultdict
def group_anagram(strs):
    groups = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))    # tuple stores ('a', 'e', 't') for eat. Can use str too but tuple is cleaner
        groups[key].append(word)
    return groups

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagram(strs))