"""Дан массив состоящий из нулей, единиц и двоек.
Необходимо его отсортировать за линейное время. Пример с доп память,
используя словарь"""


def sort_colors_2(nums: list[int]) -> None:
    dct = {}
    for i in nums:
        dct[i] = dct.get(i, 0) + 1
    ind = 0
    for i in range(3):
        x = dct.get(i, 0)
        nums[ind : ind + x] = [i] * x
        ind += x
    return nums
