# Write a function that returns True if the string passed as an argument is a palinfrome, False otherwise.
# A palindrome reads the same forwards and backwards. For this problem the case matters, and all characters matter.

# Example
# (is_palindrome('madam') ==> True)
# (is_palindrome('356653') ==> True)

# Data
# input is a string
# output will be a bool

# Algorithm
# Will want to use floor division (//) to slice the len of the string. 
# Need to be careful about odd length strings

def is_palindrome(my_string):
    if len(my_string) % 2 == 0:
        back_half_str = my_string[(len(my_string)//2):]
        back_half_rev = []
        for char in back_half_str:
               back_half_rev.insert(0, char)
        return "".join(back_half_rev) == my_string[:(len(my_string)//2)]
    else:
        back_half_str = my_string[((len(my_string)+1)//2):]
        back_half_rev = []
        for char in back_half_str:
               back_half_rev.insert(0, char)
        return "".join(back_half_rev) == my_string[:((len(my_string))//2)]


print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# A much, much easier way of doing this is the following:
def is_palindrome2(s):
     return s == s[::-1]
# All of these examples should print True

print(is_palindrome2('madam') == True)
print(is_palindrome2('356653') == True)
print(is_palindrome2('356635') == False)

# case matters
print(is_palindrome2('Madam') == False)

# all characters matter
print(is_palindrome2("madam i'm adam") == False)