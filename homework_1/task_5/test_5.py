import unittest

from t_5 import merge


class TestMerge(unittest.TestCase):
    def test_merge_second_empty_array(self):
        """Тест 1: второй массив пуст"""
        result = merge([1], 1, [], 0)
        self.assertEqual(result, [1])

    def test_merge_basic_case(self):
        """Тест 2: массивы с элементами"""
        result = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        self.assertEqual(result, [1, 2, 2, 3, 5, 6])

    def test_merge_first_empty_array(self):
        """Тест 3: первый массив пуст"""
        result = merge([0], 0, [1], 1)
        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main()
