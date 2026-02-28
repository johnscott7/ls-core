fibonacci_dict = {}

def fibonacci(n):
    if n == 1:
        return n
    elif n == 2:
        return n - 1
    elif n in fibonacci_dict:
        return fibonacci_dict[n]
    
    fibonacci_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_dict(n)