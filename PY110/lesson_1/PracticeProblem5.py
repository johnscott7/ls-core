ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# Calculate the total age given the above dictionary:
total_age = 0
for people in ages:
    total_age += ages[people]

print(total_age)

# Method using Python's documentation:
total_age = sum(ages.values())
print(total_age)