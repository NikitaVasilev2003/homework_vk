"""Дан массив состоящий из нулей, единиц и двоек.
Необходимо его отсортировать за линейное время"""


def sort_colors_3(nums: list[int]):
    low = mid = 0
    n = len(nums)
    high = n - 1
    while mid <= high:
        if nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        elif nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        else:
            mid += 1
    return nums
