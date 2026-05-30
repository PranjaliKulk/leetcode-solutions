def removeDup(s):
    seen = set() # empty set
    result = [] # result array

    for char in s: 
        if char not in seen:  # Check every character
            seen.add(char) # Add if not already present
            result.append[char]

    return ''.join(result) # convert back to string 