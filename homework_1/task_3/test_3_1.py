import unittest
from t_3_with_extra_memory_1 import rotate_1


class TestRotateArray(unittest.TestCase):
    def test_rotate_one_element(self):
        """Тест 1: один элемент"""
        result = rotate_1([1], 3)
        self.assertEqual(result, [1])

    def test_rotate_basic_case(self):
        """Тест 2: Массив с элементами"""
        result = rotate_1([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [4, 5, 1, 2, 3])

    def test_rotate_k_more_n(self):
        """Тест 3: k больше n"""
        result = rotate_1([1, 2, 3, 4, 5], 8)
        self.assertEqual(result, [3, 4, 5, 1, 2])

    def test_rotate_k_equal_0(self):
        """Тест 4: k равно 0"""
        result = rotate_1([1, 2, 3, 4, 5], 0)
        self.assertEqual(result, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
