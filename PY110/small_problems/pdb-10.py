# A developer is trying to remove duplicates
# from a list. They use a set for deduplication,
# but the order of elements is lost.
# How can we preserve the order?

'''
Buggy code:
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
'''

# Notes
# Sets do not preserve order, therefore converting
# to a set and back again will not preserve the 
# original list order.
# We can preserve the order by iterating across
# the original list and only appending the unique
# values to unique_list as we go.

# Revised code:
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for value in data:
    if value not in unique_data:
        unique_data.append(value)
print(unique_data == [4, 2, 1, 3])