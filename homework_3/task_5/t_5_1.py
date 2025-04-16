"""Дан не отсортированный массив целых чисел и некоторое число target. Необходимо
написать функцию, которая найдет два таких элемента в массиве, сумма которых будет
равна target
Один элемент можно использовать лишь один раз. В случае если два таких элемента не
нашлось, возвращаем пустой массив
"""


# классический twosum
def twoSum(data, target):
    seen = {}
    for i in range(len(data)):
        x = target - data[i]
        if x in seen:
            return seen[x], i
        seen[data[i]] = i
    return []


# более питонячий вариант
# def twoSum(data, target):
#     seen = {}
#     for i, val in enumerate(data):
#         x = target - val
#         if x in seen:
#             return seen[x], i
#         seen[val] = i
#     return []
