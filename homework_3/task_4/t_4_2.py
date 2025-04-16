"""
Найти разницу между двух строк

На вход функции подается две строки: a и b. Строка b образована из строки a путем
перемешивания и добавления одной буквы. Необходимо вернуть эту букву
"""

# то решение, которое требуется


def extraLetter(s1, s2):
    d1 = {}
    for i in s1:
        d1[i] = d1.get(i, 0) + 1

    for i in s2:
        if i not in d1:
            return i
        d1[i] -= 1
        if d1[i] == 0:
            del d1[i]
    return ""
