# A featured number (something unique to this exercise)
# is an odd number that is a multiple of 7,
# with all of its digits occurring exactly once each.
# For example, 49 is a featured number,
# but 98 is not (it is not odd),
# 97 is not (it is not a multiple of 7),
# and 133 is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument
# and returns the next featured number greater than the integer.
# Issue an error message if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201.

# Problem
# We are searching for a (next) special number invented by launchschool.
# This number is divisible by 7.
# This number is odd.
# This number cannot have any digits that repeat more than once
# It exists between 0 and 9876543201 (This is an assumption based
# on the fact no negative numbers are shown in the examples)


# Examples
# 12 -> 21
# 999999 --> 1023547

# Data Structure
# Input will be an int
# Output will also be an int
# Will definitely need some data structures to get there
# Might convert the digit to a string and use a dictionary
# to detect repeated values
# Could also accomplish this with a list. Add each value to the list
# and then check if char in list. This would be easier.

# Algorithm
# define next_featured to accept an int argument
# set error = "there is no possible number..."
# validate the int argument is between 0and 9876543201. If not,
    # return error
# iterate over a range from inputnumber + 1 to 9876543201
    # if num % 2 == 0:
        # continue
    # if num % 7 != 0:
        # continue
    # set individual_nums = []
    # set str_number = str(num)
        # for char in str_number:
            # if char in individual_nums
                # continue
            # append num to individual_nums
        # return num
    # return error



# Code
def next_featured(number):
    error = ("There is no possible number that "
         "fulfills those requirements.")
    if number < 0 or number > 9876543201:
        return error
    for num in range(number + 1, 9876543202):
        if num % 2 == 0:
            continue
        if num % 7 != 0:
            continue
        duplicated_number = False
        individual_nums = []
        str_number = str(num)
        for char in str_number:
            if char in individual_nums:
                duplicated_number = True
                break
            individual_nums.append(char)
        if duplicated_number:
            continue
        return num
    return error

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True