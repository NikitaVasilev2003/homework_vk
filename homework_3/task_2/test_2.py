import unittest
from t_2 import copyTime


class TestCopyTime(unittest.TestCase):
    def test_True(self):
        """Базовый пример с семинара"""
        result = copyTime(5, 1, 2)
        self.assertEqual(4, result)

    def test_number_is_zero(self):
        """Пример с 0"""
        result = copyTime(0, 10, 20)
        self.assertEqual(0, result)

    def test_number_is_one(self):
        """Пример с 1"""
        result = copyTime(1, 10, 20)
        self.assertEqual(10, result)


if __name__ == "__main__":
    unittest.main()
