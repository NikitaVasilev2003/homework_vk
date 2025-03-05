"""Дано два отсортированных массива. Необходимо
написать функцию которая объединит эти два массива
в один отсортированный."""


def merge_sorted_arrays(lst1, lst2):
    i = j = 0
    n1, n2 = len(lst1), len(lst2)
    merged_array = []
    while i < n1 and j < n2:
        if lst1[i] < lst2[j]:
            merged_array.append(lst1[i])
            i += 1
        else:
            merged_array.append(lst2[j])
            j += 1
    if i < n1:
        merged_array.extend(lst1[i:])
    if j < n2:
        merged_array.extend(lst2[j:])
    return merged_array
