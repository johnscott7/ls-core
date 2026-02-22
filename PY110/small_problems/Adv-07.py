# Write two functions: one that takes a Rational number as an argument, 
# and returns a list of the denominators that are part of an Egyptian 
# Fraction representation of the number, 
# and another that takes a list of numbers in the same format, 
# and calculates the resulting Rational number. 
# You will need to use the Fraction class provided by the fractions module.

# Examples

# DS
# For first function
# Input will be a rational number
# Output will be a list

# For second function, 
# Input will be a list 
# Output will be a rational number

# Alg
# First function
# Def func egyptian that takes a rational number argument
# Initialize an empty list
# Start with idx = 1
# Start while loop for desired_value not 0
    # Create a unit fraction using 1 / current value
    # If unit fraction is less than (or equal to) the remaining fraction
        # subtract the unit fraction from the remaining fraction
        # Add the current value to the results list
    # Increase current value by 1
# Return results

# Second function
# def func unegyptian that takes a list argument
# convert each element to fraction 1 / number
# Add all elements together
# Return the total fraction

# Code
from fractions import Fraction

def egyptian(target_value):
    denominators = []
    unit_denominator = 1
    while target_value != 0:
        unit_fraction = Fraction(1, unit_denominator)
        if unit_fraction <= target_value:
            target_value -= unit_fraction
            denominators.append(unit_denominator)

        unit_denominator += 1

    return denominators

def unegyptian(denominators):
    return sum([Fraction(1, d) for d in denominators])

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))