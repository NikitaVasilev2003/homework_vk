"""Дан массив целых чисел.
Необходимо развернуть его.
Сделать это надо за линейное время без
дополнительных аллокаций памяти"""


def reverse_array(lst):
    n = len(lst)
    left = 0
    right = n - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst
