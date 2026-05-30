num = 12345
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10
print(reversed_num)

# Itr 1
# num = 12345
# original_num = 12345
# reversed_num = 0

# Itr 2:
# digit = 12345 % 10 = 5
# reversed_num = 0 * 10 + 5 = 5
# num = 12345 // 10 = 1234

# To check if it is a Palindrome
#return num == reversed_num