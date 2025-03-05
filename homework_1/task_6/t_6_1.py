"""Дан массив, содержащий только 0 и 1. Напишите функцию,
которая сортирует его так, чтобы все нули оказались в
начале, а все единички - в конце. Решение должно быть
in-place."""


def sort_binary_array_1(lst: list[int]):
    left = 0
    n = len(lst)
    right = n - 1
    while left < right:
        if lst[left] == 0:
            left += 1
        elif lst[right] == 1:
            right -= 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    return lst
