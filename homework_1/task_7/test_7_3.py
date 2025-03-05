import unittest

from t_7_3 import sort_colors_3


class TestSortColors(unittest.TestCase):
    def test_sort_colors_one_element_0(self):
        """Тест 1: 1 элемент 0"""
        result = sort_colors_3([0])
        self.assertEqual(result, [0])

    def test_sort_colors_1_basic_case_1(self):
        """Тест 2: есть и 0, и 1, и 2"""
        result = sort_colors_3([2, 0, 2, 1, 1, 0])
        self.assertEqual(result, [0, 0, 1, 1, 2, 2])

    def test_sort_colors_1_basic_case_2(self):
        """Тест 3: все значения по одному, проверяет случай, если не написать mid <= high"""
        result = sort_colors_3([2, 0, 1])
        self.assertEqual(result, [0, 1, 2])

    def test_sort_colors_1_two_elements(self):
        """Тест 4: 2 значения"""
        result = sort_colors_3([1, 2])
        self.assertEqual(result, [1, 2])


if __name__ == "__main__":
    unittest.main()
