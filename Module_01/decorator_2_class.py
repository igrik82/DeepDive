''' Decorators class sample '''

# Wraps decorator allow proper function name and documentation
from functools import wraps

# Class decorator
class Counter:
    '''Couter how many times function called'''
    def __init__(self):
        self.count = 0

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            self.count += 1
            print(f"Function {func.__name__} was called {self.count} times")
            return func(*args, **kwargs)

        return inner


@Counter()
def add(first: int, second: int) -> int:
    """Function to add two numbers"""
    return first + second


print(add(1, 2))
print(add(1, 2))

help(add)
