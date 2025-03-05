import unittest

from t_4 import merge_sorted_arrays


class TestMergeSorted(unittest.TestCase):
    def test_merge_sorted_arrays_empty_array(self):
        """Тест 1: один из массивов пуст"""
        result = merge_sorted_arrays([1, 2, 3, 4], [])
        self.assertEqual(result, [1, 2, 3, 4])

    def test_merge_sorted_arrays_basic_case(self):
        """Тест 2: массивы с элементами"""
        result = merge_sorted_arrays([1, 2, 6, 10, 15], [-1, 0, 4, 5, 20])
        self.assertEqual(result, [-1, 0, 1, 2, 4, 5, 6, 10, 15, 20])

    def test_merge_sorted_arrays_one_more_two(self):
        """Тест 3: все значения одного массива больше второго"""
        result = merge_sorted_arrays([0, 0, 0, 0], [1, 2, 3, 4, 5])
        self.assertEqual(result, [0, 0, 0, 0, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
