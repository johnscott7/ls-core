# Given the object shown below, 
# print the name, age and gender of each family member.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

'''
(name) is a (age)-year-old (male or female).
Expected output:
Herman is a 32-year-old male.
Lily is a 30-year-old female.
Grandpa is a 402-year-old male.
Eddie is a 10-year-old male.
Marilyn is a 23-year-old female.
'''
for people in munsters:
    name = people
    age = munsters[people]['age']
    gender = munsters[people]['gender']
    print(f'{name} is a {age}-year-old {gender}.')


# Alternatively, use .items() to unpack the key and values directly:
for name, info in munsters.items():
    print(f"{name} is a {info['age']}-year-old {info['gender']}.")