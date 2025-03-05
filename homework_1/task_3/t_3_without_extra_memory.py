"""Дан массив целых чисел.
Необходимо повернуть (сдвинуть) справа налево часть массива, которая
указана вторым параметром.
Сделать это надо за линейное время без дополнительных аллокаций
Исходный массив: 1, 2, 3, 4, 5, 6, 7
k = 3
Результат: 5, 6, 7, 1, 2, 3, 4"""


def rotate_3(nums: list[int], k: int) -> None:
    def reverse_array(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    n = len(nums)
    k = k % n
    reverse_array(0, n - 1)
    reverse_array(0, k - 1)
    reverse_array(k, n - 1)
    return nums
