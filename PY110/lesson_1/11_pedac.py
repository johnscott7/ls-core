# PROCESS
# Inputs: Integer for available blocks
# Outputs: Integer for blocks left over after building the tallest possible valid structure

# Explicit rules:
    # Structure is built in layers
    # Top layer is a single block
    # Block in an upper layer must be supported by four blocks in a lower layer
    # Block in a lower layer can support more than one block in an upper layer
    # You cannot leave gaps between blocks
# Implicit:
    # Since top layer is always one block, this will be a pyramid shape

# Questions:
# What is the relationship between lower and upper block support? An upper block needs four lower blocks,
# but lower blocks can also support more than one block, so could four blocks support four blocks?
# If not, how many?
# Answer: Four blocks must be supporting each individual block, but some of those four
# can also be in use supporting other blocks. It's like a pyramid of blocks.


# EXAMPLES AND TEST CASES
# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True 
# print(calculate_leftover_blocks(14) == 0) # True (3 levels)


# DATA STRUCTURE
# May want to use a list of ints, each element representing the number of blocks per level. 
# Could also use a dictionary with key-value pairs of level: number of blocks
# Output in both cases will be an int, calculated from initial number of blocks minus total sum of ints in my collection type of choice

# ALGORITHM
# Will need a formula that determines how many blocks go into each level
# Level 1: 1
# Level 2: 4
# Level 3: 9
# Level 4: 16
# Level 5: 25
# Okay, so number of blocks used is level number squared. But, we need to remove one level amount from the total one at a time.
# For example, if 50 blocks, we would do 50 - 1 = 49, then check if 49 > 2 * 2 (yes)
# 49 - 4 = 45. Check if 45 > 3 * 3 (yes), and continue, incrementing the level # one at a time

# def function calculate_leftover_blocks(num):
    # Initialize an empty list
    # Initialize index = 0
    # current_blocks = num
    # While current_blocks > index * index (meaning, there are enough blocks remaining to make another level)
        # current_blocks -= (index * index)
        # Optionally, append the (9idx * idx) value to the list to see how big the structure is at the end
        # index += 1
    # return current_blocks (this will return the number once it is too small to create another structure level)

def calculate_leftover_blocks(num):
    current_layer = 0
    current_blocks = num
    while current_blocks >= (current_layer * current_layer):
        current_blocks -= (current_layer * current_layer)
        current_layer += 1
    return current_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True 
print(calculate_leftover_blocks(14) == 0) # True (3 levels)