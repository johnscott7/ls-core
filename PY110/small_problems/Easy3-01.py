# The time of day can be represented as the number of minutes
# before or after midnight. If the number of minutes is positive, 
# the time is after midnight. If the number of minutes is negative, 
# the time is before midnight.

# Write a function that takes a time 
# using this minute-based format and returns 
# the time of day in 24-hour format (hh:mm). 
# Your function should work with any integer input.

# Do not use Python's datetime module.

# Examples
# 0 --> "00:00"
# -3 --> "23:57"
# 35 --> "00:35"
# -1437 --> "00:03"
# 3000 --> "02:00"
# 800 --> "13:20" 
# -777 --> 

# Data structure
# Input will be a positive or negative integer
# Output will be a string

# Some useful data structures
#    mins_in_day = 1440 (24 * 60)


# Algorithm
# Accept integer argument 'number' and check if it is less than min_in_day (see above)
# if not, set number = number divided by mins_in_day to get it in a 24-hour format
# Have to be careful with floor division as it rounds DOWN, not to zero
# First let's calculate hour on the clock, doing it separately for pos/neg
# if number is less than zero, convert it to positive version:
    # number = 1440 - number
# Determine hour of the day using floor division
    # (number // 60)
# Determine minute of the hour using NON-floor division with the above
    # (number // 60) - number

# Calculate minutes remaining (above formula without floor division - above value)
    # --> minutes = (number / 60) - hour
    # if minutes is positive, minutes
    # if minutes is negative, minutes = 60 - minutes 
# Combine into a string
    # Use formatted string with {hour} and {minutes

# Code

MINUTES_PER_DAY = 1440

def time_of_day(number):
    number = number % MINUTES_PER_DAY
    clock_hour = number // 60
    clock_min = number % 60
    return f'{clock_hour:02}:{clock_min:02}'


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
