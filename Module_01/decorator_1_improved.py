""" Decorators sample improved"""
import functools

# Decorator
def counter(func):
    """Counter function called"""
    count = 0

    def add_improved(*args):
        '''Decorator for changing quantity arguments'''
        nonlocal count
        count += 1
        print(f"Function \"{func.__name__}\" was called {count} times")
        return functools.reduce(func, args)

    return add_improved


@counter
def add(first: int, second: int) -> int:
    """Function to add two numbers"""
    return first + second


print(add(1, 2, 3))
