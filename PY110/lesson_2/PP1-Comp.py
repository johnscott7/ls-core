# Start with a very simple example
# Sum all ages from this dictionary using both a loop
# and a list comprehension

munsters_simple = {
    'Herman': 32,
    'Lily': 30,
    'Grandpa': 402,
    'Eddie': 10,
    'Marilyn': 23,
}

# for ages in munsters.values():
#     print(ages)

# total_age = sum([age for age in munsters_simple.values()])
# print(total_age)


munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Compute and display the total age of the family's male members,
# First by using an ordinary loop:
total_age = 0
for people in munsters:
    if munsters[people]['gender'] == 'male':
        total_age += munsters[people]['age']
print(total_age)

# Now solve this using a list comprehension:
# Using .values()
total_male_age = sum([people['age'] for people in munsters.values() if people['gender'] == 'male'])
print(total_male_age)

# Now, accessing the values through the keys:
male_total_age = sum([munsters[people]['age'] for people in munsters if munsters[people]['gender'] == 'male'])
print(male_total_age)
