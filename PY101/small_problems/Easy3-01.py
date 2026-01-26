# P
# Write a function that takes two arguments, a string and a positive integer, and prints the string as many times at the integer.

# E
# repeat( 'dog', 3) -> 'dogdogdog'

# D
# input will be two arguments passed to a function
# output will be a string

# A
# Receive the two arguments, validate type or convert type if needed
# multiply together, and print

# C
# My original solution
def repeat(word, num):
    print(word * int(num))

# Launchschool approach is to print each word on a separate line. Try again:
def repeat2(word, num):
    for _ in range(num):
        print(word)

repeat('Hello', 3)
repeat2('Hello', 3)