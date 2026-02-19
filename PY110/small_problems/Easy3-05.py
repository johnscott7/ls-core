# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

# Examples
# reverse_number(12345) == 54321)
# reverse_number(12213) == 31221)
# reverse_number(456) == 654)
# reverse_number(1) == 1)
# reverse_number(12000) == 21)
# reverse_number(12345) == 54321)

def reverse_number(number):
    str_num = list(str(number))
    result = []
    while str_num:
        item = str_num.pop()
        result.append(item)
    return int(''.join(result))
 


print(reverse_number(12213) == 31221)  # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True