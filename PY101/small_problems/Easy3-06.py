# Madlibs
# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, 
# and injects them into a story that you create.

# Example
'''
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
'''

# Input will be four strings received from the user
# Output wil be three sentences as shown above

print("Hi. Let's do a madlib.")
noun = input("Please input a noun: ")
verb = input("Please input a verb: ")
adjective = input("Please input a adjective: ")
adverb = input("Please input a adverb: ")
print("Thank you. Here is your madlib:")
print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
print(f"The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.")
print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")
