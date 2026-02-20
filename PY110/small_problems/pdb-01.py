# Our countdown to launch isn't behaving as expected. 
# Why? 
# Change the code so that our program successfully counts down from 10 to 1 before launching.

'''
Faulty code:
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)

print('LAUNCH!')
'''

# Revised code:

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')
