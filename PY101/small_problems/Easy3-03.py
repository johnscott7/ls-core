# Write a function that takes a short line of text and prints it within a box
# Example
# print_in_box('To boldly go where no one has gone before.')
'''
+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+
'''

# Input can be a string or an empty string
# Output will be the same exact string with the added symbols around it


def print_in_box(words):
    width = len(words)
    top_and_bottom = "+" + "-" * (width + 2) + "+"
    empty_line = "|" + " " * (width + 2) + "|"
    text_line  = f"| {words} |"
    print(top_and_bottom)
    print(empty_line)
    print(text_line) 
    print(empty_line)
    print(top_and_bottom)


print_in_box('')
print_in_box('To boldly go where no one has gone before.')