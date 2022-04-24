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
        # make args iterable and apply to reduce functions
        args = tuple(args)
        print(f"Function {func} was called {count} times")
        return functools.reduce(func, args)

    return add_improved


@counter
def add(first: int, second: int) -> int:
    """Function to add two numbers"""
    return first + second


print(add(1, 2))
help(add)
