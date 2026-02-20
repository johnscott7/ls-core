# Write a function that takes a string as an argument and 
# returns that string with a staggered capitalization scheme. 
# Every other character, starting from the first, should be 
# capitalized and should be followed by a lowercase or 
# non-alphabetic character. Non-alphabetic characters 
# should not be changed, but should be counted as characters 
# for determining when to switch between upper and lower case.

# Examples
# 'I Love Launch School!' --> "I LoVe lAuNcH ScHoOl!"
# 'ALL_CAPS' --> "AlL_CaPs"
# 'ignore 77 the 4444 numbers' --> "IgNoRe 77 ThE 4444 nUmBeRs"
# '' --> ""

# DS
# Input is a string
# Output will also be a string

# Alg
# define a function staggered_case that takes a string argument
# Initialize an empty list
# Iterate over enumerated string
    # If index number is even
        # append character as is
    # If index number is odd
        # if char isalphanumeric
            # append char swapcase
        # else
            # append char as is
    # return list joined on ''

# Code

def staggered_case(string):
    char_list = []
    for idx, char in enumerate(string):
        if idx % 2 == 0:
            char_list.append(char.upper())
        else:
            char_list.append(char.lower())
    return ''.join(char_list)


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True