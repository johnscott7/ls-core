# Access the letter g from each object below:

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

g_list1 = lst1[2][1][3]
print(g_list1)
g_list2 = lst2[1]['third'][0]
print(g_list2)
g_list3 = lst3[2]['third'][0][:1]
print(g_list3)
g_dict1 = dict1['b'][1]
print(g_dict1)
g_dict2 = list(dict2['3rd'].keys())[0]
print(g_dict2)