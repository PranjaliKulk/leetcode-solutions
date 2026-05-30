# while encoding -> length+word e.g. "hello","world" -> "5#hello5z3world"

def encode(strs):
    result = ""
    for word in strs:
        result += str(len(word)) + "#" + word    
    return result

def decode(s):
    resultdecode = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j]) # get number before #
        word = s[j+1 : j+1+length] # extract exactly word length
        resultdecode.append(word)
        i = j+1+length # move i to next round
    return resultdecode

strs = ["hello", "world"]
encoded = encode(strs)
decoded = decode(encoded)

print(encoded)
print(decoded)
