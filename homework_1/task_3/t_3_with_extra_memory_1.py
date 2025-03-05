"""Дан массив целых чисел.
Необходимо повернуть (сдвинуть) справа налево часть массива, которая
указана вторым параметром.
Сделать это надо за линейное время с доп памятью 1 способ
Исходный массив: 1, 2, 3, 4, 5, 6, 7
k = 3
Результат: 5, 6, 7, 1, 2, 3, 4"""


def rotate_1(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n
    rotated = [0] * n

    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    for i in range(n):
        nums[i] = rotated[i]
    return nums
