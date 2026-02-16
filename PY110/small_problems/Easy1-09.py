# In the previous problem, we developed a function that 
# converts simple numeric strings to integers. In this exercise,
# you're going to extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the appropriate
# number as an integer. The string may have a leading 
# + or - sign; if the first character is a +, your function should
# return a positive number; if it is a -, your function should
# return a negative number. If there is no sign, return a 
# positive number.

# You may assume the string will always contain a valid number.

# You may not use any Python standard conversion functions (int).
# You may use the solution from the previouse exercise as a jumping
# off point.

# Examples
# "4321" --> 4321
# "-570" --> -570
# "+100" --> 100


def string_to_integer(num_string):
    total_num = 0
    for char in num_string:
        total_num = (10 * total_num) + (ord(char) - ord('0'))
    return total_num

def string_to_signed_integer(num_string):
    if num_string[0] == '-':
        return -(string_to_integer(num_string[1:]))
    elif num_string[0] == '+':
        return -(string_to_integer(num_string[1:]))
    else:
        return string_to_integer(num_string)
    

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True