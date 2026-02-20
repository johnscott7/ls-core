# Modify the function from the previous exercise so it 
# ignores non-alphabetic characters when determining whether 
# it should uppercase or lowercase each letter. The non-alphabetic 
# characters should still be included in the return value; 
# they just don't count when toggling the desired case.

# Examples
# 'I Love Launch School!' --> "I lOvE lAuNcH sChOoL!"
# 'ALL_CAPS' --> "AlL_cApS"
# 'ignore 77 the 4444 numbers' --> "IgNoRe 77 ThE 4444 nUmBeRs"
# ('') --> ""

# DS
# Input is a string
# Output will also be a string

# Alg
# Existing logic from previous problem
# Need to manually increment a counter instead
# Only increase the counter value when a character is counted


# Code

def staggered_case(string):
    char_list = []
    counter = 0
    for char in string:
        if counter % 2 == 0:
            char_list.append(char.upper())
        else:
            char_list.append(char.lower())
        if char.isalpha():
            counter += 1
    return ''.join(char_list)

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True