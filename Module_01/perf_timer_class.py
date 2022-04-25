"""Decorator for testing speed execution. Class method"""
import time
import functools


class TimeIt:
    '''Decorator for time mesurment'''
    def __init__(self, quantity=1):
        self.quantity = quantity
        self.result = None

    def __call__(self, func):

        """Called magic metod"""

        @functools.wraps(func)
        def inner(*args, **kwargs):
            # Wrapper
            start_timer = time.perf_counter()

            for _ in range(self.quantity):
                self.result = func(*args, **kwargs)

            elapsed_time = start_timer - time.perf_counter()
            print(
                f"Execution time {elapsed_time:.6f} in {self.quantity} \
times."
            )
            return self.result

        return inner


@TimeIt(100_000_000)
def add(first: int, second: int) -> int:
    '''Simple adder'''
    return first + second


print(add(1, 2))
help(add)
