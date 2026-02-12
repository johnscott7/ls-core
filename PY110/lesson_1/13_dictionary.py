produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(any_dict):
    new_dict = {}
    for key in any_dict:
        if any_dict[key] == 'Fruit':
            new_dict[key] = any_dict[key]
    return new_dict

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }


# A generalized version for more than just 'Fruit':
def select_type(produce_list, selection_criterion):
    selected_items = {}
    for key in produce_list:
        if produce_list[key] == selection_criterion:
            selected_items[key] = produce_list[key]

    return selected_items

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_type(produce, 'Fruit'))
# {'apple': 'Fruit', 'pear': 'Fruit'}

print(select_type(produce, 'Vegetable'))
# {'carrot': 'Vegetable', 'broccoli': 'Vegetable'}

print(select_type(produce, 'Meat'))
# {}