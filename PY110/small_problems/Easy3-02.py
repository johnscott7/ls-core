# As seen in the previous exercise, the time of day can 
# be represented as the number of minutes before or after
# midnight. If the number of minutes is positive, the time is
# after midnight. If the number of minutes is negative, the time
# is before midnight.

# Write two functions that each take a time of day in 24 hour format,
# and return the number of minutes before and after midnight, respectively.
# Both functions should return a value in the range 0 through 1439.

# Examples
# "00:00" ==> 0
# "00:00" ==> 0
# "12:34" ==> 754
# "12:34" ==> 686
# "24:00" ==> 0
# "24:00" ==> 0

# Data structure
# Input is a string
# Output will be an int

# Useful Inter Structures or values
# MINUTES_PER_DAY = 1440
# int conversions of each of the four str characters

# Algorithm
# Pull all four char by slicing and convert to int
# multiply first two by 60, set to variable total_min
# multiply third int by 10, add to total_min
# add fourth int to total_min
# total_min % 1440 to ensure value between 0 and 1439



def after_midnight(string):
    tens_hour = int(string[0])
    ones_hour = int(string[1])
    tens_min = int(string[-2])
    ones_min = int(string[-1])
    total_min = ((tens_hour * 10) + ones_hour) * 60
    total_min = total_min + (tens_min * 10) + ones_min
    min_after_midnight = total_min % 1440
    return min_after_midnight

def before_midnight(string):
    tens_hour = int(string[0])
    ones_hour = int(string[1])
    tens_min = int(string[-2])
    ones_min = int(string[-1])
    total_min = ((tens_hour * 10) + ones_hour) * 60
    total_min = total_min + (tens_min * 10) + ones_min
    min_before_midnight = (total_min % -1440)
    return -(min_before_midnight)


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True