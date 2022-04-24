''' Decorators sample '''

# Wraps decorator allow proper function name and documentation
from functools import wraps


# Decorator
def counter(func):
    '''Counter function called'''
    count = 0

    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} was called {count} times")
        return func(*args, **kwargs)

    return inner


@counter
def add(first: int, second: int) -> int:
    """Function to add two numbers"""
    return first + second


print(add(1, 2))
print(add(1, 2))
help(add)
