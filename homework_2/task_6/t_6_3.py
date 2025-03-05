"""Напишите функцию, которая принимает на вход строку и возвращает
true, если она является палиндромом*. В противном случае верните false.

*слово или текст, одинаково читающиеся в обоих направлениях.
3 решение
"""

from collections import deque


def isPalindrome(s):
    s = s.lower()
    deq = deque(s)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True
