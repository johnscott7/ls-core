# Write a function that takes a year as input and returns the century. 
# The return value should be a string that begins with the century number, and ends
# with 'st', 'nd', 'rd', or 'th' as appropriate
# New centuries begin in years that end with 01. So, 1901-2000 is 20th century

# Example:
# century(2000) == "20th" 

# Input will be a year
# Output should be a string

def century(year):
    cent = (year - 1) // 100 + 1
    last_two = cent % 100
    last_one = cent % 10
    if last_two in (11, 12, 13):
        suffix = "th"
    elif last_one == 1:
        suffix = "st"
    elif last_one == 2:
        suffix = "nd"
    elif last_one == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{cent}{suffix}"


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True