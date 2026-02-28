# The base case occurs when the argument is 1 or 2; both of these arguments result in a value of 1.
# The Fibonacci function calls itself. In fact, it calls itself twice.
# Except when dealing with the base case, each call to the Fibonacci function comes closer to the base case.
# In this case, both F(n-1) and F(n-2) are closer to the base case thatn F(n).

# Write a recursive function that computes the nth Fibonacci number, where nth is an argument
# passed to the function.

# We know that if n is 1, the result is 1.

def fibonacci(n):
    if n == 1:
        return n
    if n == 2:
        return n - 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# 1 -> 1
# 2, return n + fibonacci(n - 1) # 2 + 1 = 3 (wrong)
        # returns 2

# 3, return n - fibonacci(n - 1) # Backing out: 3 - 1 = 2
    # open fibonacci again, now n = 2: 
    # return 2 - fibonacci(n - 1) # Backing out: 2 - 1 = 1
        # open fibonacci again, now n = 1
        # return 1

# 4, return n + fibonacci(n - 1) # Return 4 + TBD. Backing out: 4 - 1 = 3
    # Open fibonacci again, now n = 3
    # return 3 - fibonacci(n - 1) # Backing out: 3 - 1 = 2
        # Open fibonacci again
        # return 2 - fibonacci(n - 1). Backing out: 2 - 1 = 1
            # Open fibonacci again
            # return 1

# 5, return n - fibonacci(n - 1) # Return 5 + TBD. Backing out: 5 - 3 = 2
    # Open fibonacci again, now n = 4
    # Return 4 - fibonacci(n - 1).  # Backing out: 4 - 1 = 3
        # Open fibonacci again, now n = 3
        # return 3 - fibonacci(n - 1) # Backing out: 3 - 1 = 2
            # Open fibonacci again
            # return 2 - fibonacci(n - 1). Backing out: 2 - 1 = 1
                # Open fibonacci again
                # return 1





print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True