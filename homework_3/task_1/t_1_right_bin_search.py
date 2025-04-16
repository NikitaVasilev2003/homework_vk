# Найти корень числа (ближайшее целое)
# если хотим найти наименьшее значение, квадрат которого
# МЕНЬШЕ или равен исходному
def right_binarySearchSqrt(target):
    l = 0
    r = target
    while l < r:
        m = (l + r + 1) // 2
        sq = m**2
        if sq == target:
            return m
        elif sq < target:
            l = m
        else:
            r = m - 1
    return l
