# Given the following code, what will the final values
# of a and b be? 

a = 2
b = [5, 8]
lst = [a, b] # [2, [5, 8]]

lst[0] += 2
lst[1][0] -= a

print(a) # Will be 2
print(b) # Will be [3, 8]