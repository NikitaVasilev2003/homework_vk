# Найти корень числа (ближайшее целое)
# если хотим найти наименьшее значение, квадрат которого
# БОЛЬШЕ или равен исходному
def left_binarySearchSqrt(target):
    # if target == 1:
    #     return 1
    l = 0
    r = target
    while l < r:
        m = (l + r) // 2
        sq = m**2
        if sq == target:
            return m
        elif sq > target:
            r = m
        else:
            l = m + 1
    return l
