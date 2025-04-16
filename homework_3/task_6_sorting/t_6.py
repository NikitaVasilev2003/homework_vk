# квадратичные сортировки


def insert_sort(data):
    """сортировка списка вставками"""
    n = len(data)
    for i in range(1, n):
        k = i
        while k > 0 and data[k - 1] > data[k]:
            data[k - 1], data[k] = data[k], data[k - 1]
            k -= 1


def choise_sort_1(data):
    """сортировка списка выбором 1 способ"""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]


def choise_sort_2(data):
    """сортировка списка выбором 2 способ"""
    n = len(data)
    for i in range(n):
        minindex = i
        for j in range(i + 1, n):
            if data[j] < data[minindex]:
                minindex = j
        if minindex != i:
            data[i], data[minindex] = data[minindex], data[i]


def bubble_sort(data):
    """сортировка списка методом пузырька"""
    n = len(data)
    for i in range(1, n):
        for j in range(n - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def bubble_sort_optimized(data):
    """сортировка списка методом пузырька оптимизированная"""
    n = len(data)
    i = 1
    flag = True
    while flag:
        flag = False
        for j in range(n - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        i += 1
    return data


# сортировки за O(n)
def counting_sort(data):
    """сортировка списка подсчетом"""
    if not data:
        return data

    min_val = min(data)
    max_val = max(data)
    count = [0] * (max_val - min_val + 1)

    for num in data:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


# за это не ручаюсь, творчество нейросети :)
def radix_sort(arr, max_bits=32):
    """поразрядная сортировка"""
    if not arr:
        return arr

    # Определяем shift_value на основе max_bits (для отрицательных чисел)
    shift_value = 1 << (max_bits - 1)
    for i in range(len(arr)):
        arr[i] += shift_value

    # Количество проходов (по 8 бит каждый)
    num_passes = max_bits // 8
    bit_mask = 0xFF
    n = len(arr)
    output = [0] * n

    for exp in range(num_passes):
        shift = exp * 8
        count = [0] * 256

        # Подсчёт частот
        for num in arr:
            digit = (num >> shift) & bit_mask
            count[digit] += 1

        # Префиксные суммы
        for i in range(1, 256):
            count[i] += count[i - 1]

        # Распределение элементов
        for num in reversed(arr):
            digit = (num >> shift) & bit_mask
            output[count[digit] - 1] = num
            count[digit] -= 1

        arr, output = output, arr

    # Обратное преобразование
    for i in range(len(arr)):
        arr[i] -= shift_value

    return arr


# сортировки за O(n*log(n))


# сортировка слиянием
def merge_sort(data):
    """сортировка слиянием"""
    n = len(data)
    if n <= 1:
        return data
    mid = n // 2
    left = data[:mid]
    right = data[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    i = j = 0
    result = []
    l1, l2 = len(left) - 1, len(right) - 1
    while i < l1 and j < l2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < l1:
        result.extend(left[i:])
    if j < l2:
        result.extend(left[j:])
    return result


# сортировка Тони Хоара (быстрая)
def quick_sort(data):
    """Быстрая сортировка Тони Хоара"""
    _quick_sort(data, 0, len(data) - 1)


def _quick_sort(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        _quick_sort(data, low, pivot)
        _quick_sort(data, pivot + 1, high)


def partition(data, low, high):
    mid = (low + high) // 2
    a, b, c = data[low], data[mid], data[high]
    pivot = sorted([a, b, c])[1]
    if pivot == a:
        data[low], data[mid] = data[mid], data[low]
    elif pivot == c:
        data[high], data[mid] = data[mid], data[high]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while data[i] < pivot:
            i += 1
        j -= 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            return j
        data[i], data[j] = data[j], data[i]


# сортировка Шелла 1 реализация
def shell_sort_1(data):
    n = len(data)
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            j = i
            while j >= interval and data[j - interval] > data[j]:
                data[j], data[j - interval] = data[j - interval], data[j]
                j -= interval
        interval //= 2
    return data


# сортировка Шелла 2 реализация
def shell_sort_2(data):
    n = len(data)
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = data[i]
            j = i
            while j >= interval and data[j - interval] > temp:
                data[j] = data[j - interval]
                j -= interval
            data[j] = temp
        interval //= 2
    return data
