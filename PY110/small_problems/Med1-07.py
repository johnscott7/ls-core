# The Fibonacci series is a sequence of numbers in which each number
# is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1.
# The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5,
# the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:
'''
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
'''
# Write a function called fibonacci that computes the nth Fibonacci number, 
# where nth is an argument passed to the function:

# seems like a formula must exist

# Fibonacci sequence
# 1 1st
# 1 2nd
# 2 3rd
# 3 4th 
# 5 5th 
# 8 6th
# 13 7th


# Examples
# See below
# 6th --> 8                  # True
# 12th --> 144

# DS
# Input is an int representing the nth value
# Output will be a calculated int
# Might be useful to build a list of all values

# Alg
# Def fibonacci() function that accepts int argument
# Initialize an empty list and add 1, 1 to it
# for num in range(2, number)
    # append (num + new_list[num - 1])
# return empty_list[number - 1]

# Code
def fibonacci(number):
    fib_list = [0, 1, 1, 2]
    for num in range(1, number):
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list[number]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True