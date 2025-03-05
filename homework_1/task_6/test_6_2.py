import unittest

from t_6_2 import sort_binary_array_2


class TestSortBinaryArray(unittest.TestCase):
    def test_sort_binary_array_second_empty_array(self):
        """Тест 1: второй массив пуст"""
        result = sort_binary_array_2([])
        self.assertEqual(result, [])

    def test_sort_binary_array_basic_case(self):
        """Тест 2: массивы с элементами"""
        result = sort_binary_array_2([0, 1, 1, 0, 1, 0, 1, 0])
        self.assertEqual(result, [0, 0, 0, 0, 1, 1, 1, 1])

    def test_sort_binary_array_first_one_number_0(self):
        """Тест 3: первый массив пуст"""
        result = sort_binary_array_2([0])
        self.assertEqual(result, [0])

    def test_sort_binary_array_one_number_1(self):
        """Тест 4: массивы с элементами"""
        result = sort_binary_array_2([1])
        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main()
