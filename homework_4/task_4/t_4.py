"""Дано бинарное дерево поиска в виде массива. Необходимо найти
произведение минимального и максимального значений."""


def max_min_multiplication(data):
    if len(data) < 2:
        return -1

    min_index = 0
    while True:
        next_left = 2 * min_index + 1
        if next_left >= len(data) or data[next_left] is None:
            break
        min_index = next_left

    max_index = 0
    while True:
        next_right = 2 * max_index + 2
        if next_right >= len(data) or data[next_right] is None:
            break
        max_index = next_right

    if (
        min_index >= len(data)
        or (max_index >= len(data))
        or (data[min_index] is None)
        or (data[max_index] is None)
    ):
        return -1

    return data[min_index] * data[max_index]
