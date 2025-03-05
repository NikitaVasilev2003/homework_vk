"""Дан отсортированный по возрастанию
массив целых чисел и некоторое число target
Необходимо найти два числа в массиве,
которые в сумме дают заданное значение
target, и вернуть их индексы."""


def two_sum(nums: list, target: int):
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        summ = nums[left] + nums[right]
        if summ == target:
            return left, right
        elif summ > target:
            right -= 1
        else:
            left += 1
    return []
