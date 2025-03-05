import unittest
from t_1 import two_sum


class TestTwoSum(unittest.TestCase):

    def test_two_sum_found(self):
        """Тест 1: положительные числа"""
        result = two_sum([1, 2, 3, 4, 5, 6], 10)
        self.assertEqual(result, (3, 5))

    def test_two_sum_found_negative(self):
        """Тест 2: отрицательные числа"""
        result = two_sum([-5, -3, -2, -1], -5)
        self.assertEqual(result, (1, 2))

    def test_two_sum_not_found(self):
        """Тест 3: не найдено подходящих чисел"""
        result = two_sum([1, 2, 3, 4, 5], 10)
        self.assertEqual(result, [])

    def test_two_sum_two_elements(self):
        """Тест 4: массив из двух элементов"""
        result = two_sum([1, 9], 10)
        self.assertEqual(result, (0, 1))

    def test_two_sum_empty_list(self):
        """Тест 5: пустой спискок"""
        result = two_sum([], 34)
        self.assertEqual(result, [])

    def test_two_sum_one_element(self):
        """Тест 6: 1 элемент"""
        result = two_sum([1], 10)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
