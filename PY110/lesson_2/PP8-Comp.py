# Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables.
# The sizes should be uppercase, and the colors should be capitalized.


dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# The return value should look like:
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

def fruit_list(fruit_dict):
    new_list = []
    for fruit, fruit_data in fruit_dict.items():
        if fruit_data['type'] == 'fruit':
            colors = []
            for color in fruit_data['colors']:
                colors.append(color.capitalize())
            new_list.append(colors)
        else:
            new_list.append(fruit_data['size'].upper())
    return new_list
        
print(fruit_list(dict1))


# As a comprehension now:

def fruit_list_comp(fruit_dict):
    return [
        [color.capitalize() for color in fruit_data['colors']]
        if fruit_data['type'] == 'fruit'
        else fruit_data['size'].upper()
        for fruit_data in fruit_dict.values()
    ]

print(fruit_list_comp(dict1))
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
