import unittest
from t_9 import move_zeros_to_end


class TestMoveZeros(unittest.TestCase):
    def test_nothing_zeros(self):
        """Тест 1: ноль отсутствует"""
        result = move_zeros_to_end([1, 2, 3, 5])
        self.assertEqual(result, [1, 2, 3, 5])

    def test_base_case_1(self):
        """Тест 2: разные элементы и 0"""
        result = move_zeros_to_end([0, 0, 1, 0, 3, 12])
        self.assertEqual(result, [1, 3, 12, 0, 0, 0])

    def test_base_case_2(self):
        """Тест 3: разные элементы и 0"""
        result = move_zeros_to_end([0, 33, 57, 88, 60, 0, 0, 80, 99])
        self.assertEqual(result, [33, 57, 88, 60, 80, 99, 0, 0, 0])

    def test_empty_list(self):
        """Тест 4: пустой список"""
        result = move_zeros_to_end([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
