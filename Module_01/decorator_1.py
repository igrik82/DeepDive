# Decorators sample

# Wraps decorator allow proper function name and documentation
from functools import wraps


# Decorator
def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("Function {0} was called {1} times".format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


@counter
def add(a: int, b: int) -> int:
    """Function to add two numbers"""
    return a + b


print(add(1, 2))
print(add(1, 2))
help(add)
