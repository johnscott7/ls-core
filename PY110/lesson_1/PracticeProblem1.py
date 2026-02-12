fruits = ("apple", "banana", "cherry", "date", "banana")

def count_banana(grocery_list):
    bananas = []
    for food in grocery_list:
        if food == 'banana':
            bananas.append(food)
    return len(bananas)

print(count_banana(fruits))

# Or, use a list transformation:

fruits = ("apple", "banana", "cherry", "date", "banana")
bananas = ["banana" for food in fruits if food == "banana"]
count = len(bananas)
print(bananas)
print(count)

test = [food for food in fruits if food == "banana"]
print(test)
print(len(test))

# Most concise answer, using Python's documentation

count = fruits.count("banana")