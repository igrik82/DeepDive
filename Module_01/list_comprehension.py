# List comprehension
# [<expression1> for <varname> in <iterable> if <expression2>]

list_1 = range(10)
list_2 = list(filter(lambda y: y < 25, map(lambda x: x**2, list_1)))
print(list_2)
