# Write a function that takes two arguments,
# an inventory item ID and a list of transactions, 
# and returns a list containing only the transactions for the specified inventory item.

# Examples
# See below

# DS
# Inputs are a number (int) and list of dictionaries 
# Output will be a list

# Alg
# Define a func that takes an int and list
# Initialize an empty list
# Iterate over the elements (dicts) of the list
    # Using the get method, if value = num
        # Append dict to empty list
    # return list


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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True