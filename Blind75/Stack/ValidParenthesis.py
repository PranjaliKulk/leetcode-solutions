def valid_parenthesis(s):
    stack = [] # empty stack to push new brackets
    hashmap = {')':'(', '}':'{', ']':'['}

    for element in s:
        if element in hashmap:
            if stack and stack[-1] == hashmap[element]:
                stack.pop()
            else:
                return False
        else:
            stack.append(element)

    return not stack

s = "(())"
print(valid_parenthesis(s))