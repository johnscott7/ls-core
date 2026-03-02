#  Write a function that takes a year as an argument and
# returns the number of Friday the 13ths in that year.
# You may assume that the year is greater than 1752,
# which is when the United Kingdom adopted the modern
# Gregorian Calendar. You may also assume that the same
# calendar will remain in use for the foreseeable future.

# Use the datetime.date function to determine whether the 13th of a given month falls on a Friday.

# Examples
# 1986 --> 1
# 2015 --> 3
# 2017 --> 2

# Code
import datetime

def friday_the_13ths(year):
    spooky_fridays = 0
    for month in range(12):
        thirteenth = datetime.date(year, month + 1, 13)
        day_number = thirteenth.weekday()
        if day_number == 4:
            spooky_fridays += 1
    return spooky_fridays


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True