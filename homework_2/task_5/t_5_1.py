"""В исходную строку добавили некоторое количество символов.
Необходимо выявить, была ли строка a исходной для строки b.
1 cпособ с помощью списка (как очередь используем)
"""


def isSubsequence(a, b):
    l = len(a)
    lst = []
    for i in range(l - 1, -1, -1):
        lst.append(a[i])
    for el in b:
        if lst:
            val = lst[-1]
            if val == el:
                lst.pop()
    return len(lst) == 0
