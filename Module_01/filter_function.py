# Функция первым аргументом принимает функцию, вторым итератор.
# Делает выборку из итератора согласно возвращаемому значению функции
# (True or False)

list_1 = []
for i in range(1, 101):
    list_1.append(i)


# Even numbers
def even(a: int) -> int:
    return not (a % 2)


print(list(filter(even, list_1)))
