import matplotlib

matplotlib.use("Agg")  # Отключаем интерактивный режим
import matplotlib.pyplot as plt
import timeit
import random
import pandas as pd
from t_6 import (
    insert_sort,
    choise_sort_1,
    choise_sort_2,
    bubble_sort,
    bubble_sort_optimized,
    counting_sort,
    radix_sort,
    merge_sort,
    quick_sort,
    shell_sort_1,
    shell_sort_2,
)


# Обёртка для встроенной сортировки Python
def python_sort(arr):
    arr.sort()


# Список алгоритмов для тестирования
algorithms = [
    ("Insertion Sort", insert_sort),
    ("Selection Sort 1", choise_sort_1),
    ("Selection Sort 2", choise_sort_2),
    ("Bubble Sort", bubble_sort),
    ("Optimized Bubble Sort", bubble_sort_optimized),
    ("Counting Sort", counting_sort),
    ("Radix Sort", radix_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Shell Sort 1", shell_sort_1),
    ("Shell Sort 2", shell_sort_2),
    ("Python Sort", python_sort),
]


# Функции генерации тестовых данных
def generate_random(size):
    return [random.randint(-1000, 1000) for _ in range(size)]


def generate_sorted(size):
    return list(range(size))


def generate_reversed(size):
    return list(range(size, 0, -1))


def generate_partially_sorted(size, percent=90):
    arr = list(range(size))
    num_elements_to_shuffle = int((100 - percent) / 100 * size)
    indices = random.sample(range(size), num_elements_to_shuffle)
    for i in indices:
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# Параметры тестирования
data_types = [
    ("Random", generate_random),
    ("Sorted", generate_sorted),
    ("Reversed", generate_reversed),
    ("Partially Sorted", generate_partially_sorted),
]

sizes = [100, 500, 1000, 5000]

# Замер времени выполнения
results = []

for data_name, data_generator in data_types:
    for size in sizes:
        data = data_generator(size)
        print(f"Testing {data_name} array of size {size}...")
        for algo_name, algo_func in algorithms:
            try:
                # Создаём копию данных для каждого теста
                data_copy = data.copy()
                # Для Merge Sort и Counting Sort передаём копию и получаем результат
                if algo_name in ["Merge Sort", "Counting Sort", "Radix Sort"]:
                    time = timeit.timeit(lambda: algo_func(data_copy.copy()), number=1)
                else:
                    time = timeit.timeit(lambda: algo_func(data_copy), number=1)
                results.append(
                    {
                        "Algorithm": algo_name,
                        "Data Type": data_name,
                        "Size": size,
                        "Time": time,
                    }
                )
            except Exception as e:
                print(f"Error with {algo_name} on {data_name} data (size {size}): {e}")

# Визуализация результатов
import pandas as pd

df = pd.DataFrame(results)


def save_plot(data_type, algo_name=None):
    if algo_name:
        filename = f"plot_{algo_name.replace(' ', '_').lower()}.png"
    else:
        filename = f"plot_{data_type.replace(' ', '_').lower()}.png"
    plt.savefig(filename, bbox_inches="tight")
    plt.close()


# Построение графиков для каждого типа данных
for data_type in df["Data Type"].unique():
    plt.figure(figsize=(12, 8))
    subset = df[df["Data Type"] == data_type]
    for algo in df["Algorithm"].unique():
        algo_data = subset[subset["Algorithm"] == algo]
        algo_data = algo_data.sort_values("Size")
        plt.plot(algo_data["Size"], algo_data["Time"], marker="o", label=algo)
    plt.title(f"Сравнение алгоритмов сортировки ({data_type} данные)")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (секунды)")
    plt.yscale("log")
    plt.xscale("log")
    plt.grid(True, which="both", linestyle="--")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    save_plot(data_type)  # Сохраняем и закрываем график

# Сводный график для всех алгоритмов
plt.figure(figsize=(15, 10))
for idx, (algo_name, algo_func) in enumerate(algorithms):
    plt.subplot(3, 4, idx + 1)
    for data_type in data_types:
        subset = df[(df["Algorithm"] == algo_name) & (df["Data Type"] == data_type[0])]
        subset = subset.sort_values("Size")
        plt.plot(subset["Size"], subset["Time"], marker="o", label=data_type[0])
    plt.title(algo_name)
    plt.xlabel("Размер")
    plt.ylabel("Время")
    plt.yscale("log")
    plt.xscale("log")
    plt.grid(True)
    plt.legend()
plt.tight_layout()
save_plot("summary")  # Сохраняем сводный график
