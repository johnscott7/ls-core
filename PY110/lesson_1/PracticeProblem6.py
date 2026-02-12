ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# Determine the minimum age from the above dictionary

min_age = ages["Herman"]
for people in ages:
    if ages[people] < min_age:
        min_age = ages[people]


# Official solution using Python's built-in function:
min_age = min(ages.values())
print(min_age)