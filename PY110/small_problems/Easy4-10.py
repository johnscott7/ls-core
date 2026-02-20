# Building on the previous exercise, 
# write a function that returns True or False 
# based on whether or not an inventory item (an ID number)
# is available. 
# As before, the function takes two arguments: 
# an item ID and a list of transactions. 
# The function should return True only if the sum of the 
# quantity values of the item's transactions is greater 
# than zero. Notice that there is a movement property in 
# each transaction object. A movement value of 'out' will 
# decrease the item's quantity.

# You may (and should) use the transactions_for function from the previous exercise.

# Examples
# see below

# DS
# Input is an int and a list of dictionaries
# Output will be a list

# Algorithm
# Define a function that accepts an int and list as arguments
# Pass existing transactions_for function with same int and list and assign to variable
# This function returns a list of all transactions for that item
# Initialize item_quantity = 0
    # Iterate over all transactions in this list
    # if transaction['movement'] = in
        # subtract transactions['quantity'] from item_quantity
    # else
        # add transactions['quantity'] to item_quantity
# return True if item_quantity > 0

# Code
def is_item_available(item_id, transact_list):
    item_transactions = transactions_for(item_id, transact_list)
    item_quantity = 0
    for transaction in item_transactions:
        if transaction["movement"] == "out":
            item_quantity -= transaction["quantity"]
        else: 
            item_quantity += transaction["quantity"]
    return item_quantity > 0   

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

def transactions_for(item_id, transact_list):
    matching = []
    for sale in transact_list:
        if sale.get("id") == item_id:
            matching.append(sale)
    return matching

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True