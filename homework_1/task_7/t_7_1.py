"""Дан массив состоящий из нулей, единиц и двоек.
Необходимо его отсортировать за линейное время. Пример с доп память,
используя список"""


def sort_colors_1(nums: list[int]) -> None:
    lst = [0] * 3
    for i in nums:
        lst[i] += 1
    ind = 0
    for i in range(3):
        x = lst[i]
        nums[ind : ind + x] = [i] * x
        ind += x
    return nums
