def isPalindrome(s):
    left, right = 0, len(s) - 1 # Define two points; left and right. Left is at start and right at the end of string

    while left < right: # Loop until left is less than right
        if s[left] != s[right]: # check if both letters are equal
            return False # return false if not equal
        left += 1 #Increment left pointer by 1
        right -= 1 #Decrement right pointer by 1

        return True
    #Time complexity O(n)

# Same code for reversing a word with two small changes
def reverseWord(word):
# Change 1. Convert word into list because lists are immutable
    char = list(word)

    left, right = 0, len(word) - 1

    while left < right:
        # Change 2. Swap the two characters
        char[left], char[right] = char[right], char[left]
        left +=1 # Inc left by 1
        right -=1 # Dec right by 1

        # Change 3. Join it back to string
        return ''.join(char)
    

