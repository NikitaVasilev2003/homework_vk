import unittest
from t_1_right_bin_search import right_binarySearchSqrt


class TestSearchSqrt(unittest.TestCase):
    def test_True(self):
        """Базовый пример с числом, у которого есть корень"""
        result = right_binarySearchSqrt(16)
        self.assertEqual(4, result)

    def test_number_that_has_no_root(self):
        """Пример с числом, у которого нет корня"""
        result = right_binarySearchSqrt(14)
        self.assertEqual(3, result)

    def test_number_is_zero(self):
        """Проверим число 0"""
        result = right_binarySearchSqrt(0)
        self.assertEqual(0, result)

    def test_number_is_one(self):
        """Проверим число 1"""
        result = right_binarySearchSqrt(1)
        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
