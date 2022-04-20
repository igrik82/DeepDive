#!/usr/bin/env python

# Sample function
def hello(name: str) -> str:
    return (f'Hello, {name}!')


func = hello
print(func("Igor"))
