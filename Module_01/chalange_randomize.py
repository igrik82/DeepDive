from random import random


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def randomize(list_to_randomize: list) -> list:
    return sorted(list_to_randomize, key=lambda x: random())


print(randomize(sorted_list))
