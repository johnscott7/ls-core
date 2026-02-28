# Write a function that calculates and returns the index of the first Fibonacci number
# that has the number of digits specified by the argument. The first Fibonacci 
# number has an index of 1. You may assume that the argument is always an 
# integer greater than or equal to 2.

# Example
# If the argument is 2, we want the index of the first Fibonacci number that has 2 digits.
# That’s 13 at index 7, so the function should return 7.
# If the argument is 3, we want the first Fibonacci number that has 3 digits.
# That’s 144 at index 12, so return 12.

# So, generate Fibonacci numbers in order, starting from 1
# Keep track of the index as you go
# For each Fibonacci number, check how many digits it has
# Stop and return the index as soon as you hit a Fibonacci number whose digit length 
# equals the argument

# Examples
# See below

# Data structure
# Input will be an int
# Output will be an int representing the index
# Intermediate will be a list, to check index against appended values

import sys

sys.set_int_max_str_digits(50_000)

fibonacci_dict = {}

def fibonacci(n):
    if n == 1:
        return n
    elif n == 2:
        return n - 1
    elif n in fibonacci_dict:
        return fibonacci_dict[n]
    
    fibonacci_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_dict[n]

def find_fibonacci_index_by_length(n):
    fibonacci_results = []
    i = 1
    while True:
        fibonacci_results.append(fibonacci(i))
        if n == len(str(fibonacci_results[i - 1])):
            return i
        i += 1
                    
    

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)

