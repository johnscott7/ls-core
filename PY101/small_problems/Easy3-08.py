# P
# Write a function that determines the mean of the three scores passed to it
# And returns the letter associated with that grade
'''
90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
'''

# Example
# (95, 90, 93) ==> "A"

# D
# Input will be three ints passed as function arguments

# A
# Receive the function arguments and convert all three to int
# Calculate a mean
# print a grade with an if/elif/else block for appropriate score

def get_grade(grade1, grade2, grade3):
    score = (grade1 + grade2 + grade3) / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
    
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True