"""В исходную строку добавили некоторое количество символов.
Необходимо выявить, была ли строка a исходной для строки b.
3 cпособ с помощью deque """

from collections import deque


def isSubsequence(a, b):
    q = deque(a)
    if not q:
        return True

    for el in b:
        if el == q[0]:
            q.popleft()

    return not q
