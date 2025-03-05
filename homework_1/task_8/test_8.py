import unittest

from t_8 import even_first


class TestEvenFirst(unittest.TestCase):
    def test_sort_colors_one_element_odd(self):
        """Тест 1: 1 элемент 1(то есть нечетный)"""
        result = even_first([1])
        self.assertEqual(result, [1])

    def test_sort_colors_1_basic_case(self):
        """Тест 2: есть и четные числа, и другие"""
        result = even_first([3, 2, 4, 1, 11, 8, 9])
        self.assertEqual(result, [2, 4, 8, 1, 11, 3, 9])

    def test_sort_colors_one_element_even(self):
        """Тест 3: 1 элемент 2(то есть четный)"""
        result = even_first([2])
        self.assertEqual(result, [2])

    def test_sort_colors_empty_list(self):
        """Тест 4: 1 элемент 2(то есть четный)"""
        result = even_first([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
