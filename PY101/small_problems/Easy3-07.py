# A double number is an even-length number whose left-side digits are exactly the same as its right side.
# It's like a numeric palindrome
# Write a function that returns the number provided as an argument multipled by two, UNLESS
# the argument is a double number. If the argument is a double number, return it as-is.

# Example
# twice(334433) ==> 668866  
# twice(107) ==> 214

# Input will be an integer passed as function argument
# Output is a calculated integer, or same argument returned

# Receive the integer passed to the argument
# Convert the integer to a string.
# Reverse the string, assign to a new variable, compare the two values
# If equal, return the original argument
# If not equal, double the original argument and return

def twice_(num):
    str_num = str(num)
    if (str_num == str_num[::-1]) and len(str_num) % 2 == 0:
        return num
    else:
        return num * 2



# Okay. I did this one wrong. It's not a palindrome. I need to work on my reading comprehension. 
# This is the appropriate solution:
def double_number_check(num):
    str_num = str(num)
    center = len(str_num) // 2
    left_num = str_num[:center]
    right_num = str_num[center:]
    return left_num == right_num

def twice(num):
    if double_number_check(num):
        return num
    else:
        return num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True