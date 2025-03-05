import unittest
from t_2 import reverse_array


class TestReverseArray(unittest.TestCase):
    def test_reverse_array_empty_list(self):
        """Тест 1: пустой список"""
        result = reverse_array([])
        self.assertEqual(result, [])

    def test_reverse_array_one_element(self):
        """Тест 2: один элемент"""
        result = reverse_array([1])
        self.assertEqual(result, [1])

    def test_reverse_array_basic_case(self):
        """Тест 3: Массив с элементами"""
        result = reverse_array([1, 2, 3, 4, 5])
        self.assertEqual(result, [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
