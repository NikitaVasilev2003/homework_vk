import timeit
import random
import matplotlib.pyplot as plt
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

# Категории сортировок
CATEGORIES = {
    "O(n^2)": [
        (insert_sort, "Insertion Sort"),
        (choise_sort_1, "Selection Sort 1"),
        (choise_sort_2, "Selection Sort 2"),
        (bubble_sort, "Bubble Sort"),
        (bubble_sort_optimized, "Optimized Bubble Sort"),
    ],
    "O(n log n)": [
        (merge_sort, "Merge Sort"),
        (quick_sort, "Quick Sort"),
        (shell_sort_1, "Shell Sort 1"),
        (shell_sort_2, "Shell Sort 2"),
        (list.sort, "Built-in Sort"),
    ],
    "O(n)": [
        (counting_sort, "Counting Sort"),
        (radix_sort, "Radix Sort"),
    ],
}


# Генераторы тестовых данных
def generate_random(size):
    return [random.randint(-1000, 1000) for _ in range(size)]


def generate_sorted(size):
    return list(range(size))


def generate_reversed(size):
    return list(range(size, 0, -1))


def generate_with_duplicates(size):
    return [random.randint(0, 100) for _ in range(size)]


DATA_GENERATORS = {
    "Random": generate_random,
    "Sorted": generate_sorted,
    "Reversed": generate_reversed,
    "With Duplicates": generate_with_duplicates,
}


def benchmark(sort_func, data):
    if sort_func == list.sort:
        # Для встроенной сортировки
        arr = data.copy()
        timer = timeit.Timer(lambda: arr.sort())
    elif sort_func in [merge_sort, counting_sort, radix_sort]:
        # Для сортировок, возвращающих новый список
        timer = timeit.Timer(lambda: sort_func(data.copy()))
    else:
        # Для in-place сортировок
        arr = data.copy()
        timer = timeit.Timer(lambda: sort_func(arr))

    return timer.timeit(number=1)


def run_benchmarks(sizes, data_name, data_gen):
    results = {category: {} for category in CATEGORIES}

    for size in sizes:
        data = data_gen(size)
        print(f"\nTesting {data_name} data, size: {size}")

        for category, algorithms in CATEGORIES.items():
            print(f"  {category} algorithms:")
            for sort_func, name in algorithms:
                # Пропускаем квадратичные для больших размеров
                if category == "O(n^2)" and size > 5000:
                    continue
                # Пропускаем O(n) для несовместимых данных
                if (
                    "Sort" in name
                    and data_name == "Sorted"
                    and (min(data) < 0 or max(data) > 1000)
                ):
                    continue

                time_taken = benchmark(sort_func, data)
                if name not in results[category]:
                    results[category][name] = []
                results[category][name].append((size, time_taken))
                print(f"    {name}: {time_taken:.5f}s")

    return results


def plot_results(results, data_name):
    for category, algorithms in results.items():
        plt.figure(figsize=(10, 6))
        plt.title(f"Sorting Algorithms Performance ({category}, {data_name} data)")
        plt.xlabel("Array Size")
        plt.ylabel("Time (seconds)")
        plt.grid(True)

        for algo_name, points in algorithms.items():
            sizes = [p[0] for p in points]
            times = [p[1] for p in points]
            plt.plot(sizes, times, label=algo_name, marker="o")

        plt.legend()
        plt.savefig(f"plot_{category}_{data_name}.png")
        plt.close()


if __name__ == "__main__":
    # Настройки тестирования
    test_sizes = {
        "O(n^2)": [100, 500, 1000, 2000, 5000],
        "O(n log n)": [1000, 5000, 10000, 50000, 100000],
        "O(n)": [1000, 10000, 100000, 500000, 1000000],
    }

    # Запуск тестов для всех типов данных
    for data_name, data_gen in DATA_GENERATORS.items():
        # Формируем общий список размеров
        all_sizes = sorted(
            set(test_sizes["O(n^2)"] + test_sizes["O(n log n)"] + test_sizes["O(n)"])
        )

        # Запускаем тесты
        results = run_benchmarks(all_sizes, data_name, data_gen)

        # Строим графики
        plot_results(results, data_name)
