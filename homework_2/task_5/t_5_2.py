"""В исходную строку добавили некоторое количество символов.
Необходимо выявить, была ли строка a исходной для строки b.
2 cпособ с помощью очереди """

import queue


def isSubsequence(a, b):
    q = queue.Queue()
    for el in a:
        q.put(el)

    if q.empty():
        return True

    for el in b:
        if el == q.queue[0]:
            q.get()

    return q.empty()
