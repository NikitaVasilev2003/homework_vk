"""Дан не отсортированный массив целых чисел и некоторое число target. Необходимо
написать функцию, которая найдет два таких элемента в массиве, сумма которых будет
равна target
Один элемент можно использовать лишь один раз. В случае если два таких элемента не
нашлось, возвращаем пустой массив
"""


# никто не запрещает отсортировать, тогда будет задача, которую разбирали раньше
def twoSum(data, target):
    l = 0
    r = len(data) - 1
    while l < r:
        val = data[l] + data[r]
        if val == target:
            return l, r
        elif val > target:
            r -= 1
        else:
            l += 1
    return []
