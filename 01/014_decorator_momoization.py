#!/usr/bin/env python
"""Memoization decorator"""


def memoize(func):
    """Cached function"""
    cache = {}

    def closure(num):
        if num not in cache:
            cache[num] = func(num)
        return cache[num]

    return closure


@memoize
def fib(num):
    """Fibonaci function"""
    print(f"Calculating fib({num})")
    return 1 if num < 3 else fib(num - 1) + fib(num - 2)


print(fib(9))
print(fib(10))
