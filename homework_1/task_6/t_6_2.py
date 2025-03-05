"""Дан массив, содержащий только 0 и 1. Напишите функцию,
которая сортирует его так, чтобы все нули оказались в
начале, а все единички - в конце. Решение должно быть
in-place."""


def sort_binary_array_2(lst: list[int]):
    count = 0
    n = len(lst)
    for i in lst:
        if i == 0:
            count += 1
    for i in range(n):
        if count > 0:
            lst[i] = 0
        else:
            lst[i] = 1
        count -= 1
    return lst
