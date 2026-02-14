# The following dictionary has list values that contains strings.
# Write some code to create a list of every vowel (a, e, i, o , u)
# that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Start by trying to write using nested loops.
# Once that is complete, refactor the code so it uses a single list comprehension.

vowels = 'aeiou'

chars = []
for key in dict1:
    for word in dict1[key]:
        for char in word:
            if char in vowels:
                chars.append(char)
print(chars)

vowels = 'aeiou'

list_of_vowels = [char for key in dict1
              for word in dict1[key]
              for char in word if char in vowels]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']