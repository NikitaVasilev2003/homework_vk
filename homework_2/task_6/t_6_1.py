"""Напишите функцию, которая принимает на вход строку и возвращает
true, если она является палиндромом*. В противном случае верните false.

*слово или текст, одинаково читающиеся в обоих направлениях.
1 решение
"""


def isPalindrome(s):
    s = s.lower()
    stack = []
    for i in s:
        stack.append(i)
    for i in s:
        if i != stack.pop():
            return False
    return True
