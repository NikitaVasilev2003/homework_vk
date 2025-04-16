"""Напишите функцию, которая проверяет, является ли заданный массив корректной кучей (максимум).
Алгоритм должен проверить, что все узлы удовлетворяют свойству кучи."""


def isMaxHeap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[i]:
            return False

        if right < n and arr[right] > arr[i]:
            return False

    return True
