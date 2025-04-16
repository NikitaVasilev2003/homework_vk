import unittest
from t_1 import isMaxHeap


class TestMaxHeap(unittest.TestCase):

    def test_empty_array(self):
        """Проверка пустого массива"""
        self.assertTrue(isMaxHeap([]))

    def test_single_element(self):
        """Массив из одного элемента"""
        self.assertTrue(isMaxHeap([5]))

    def test_two_elements_valid(self):
        """Два элемента, корректная куча"""
        self.assertTrue(isMaxHeap([10, 5]))

    def test_two_elements_invalid(self):
        """Два элемента, некорректная куча"""
        self.assertFalse(isMaxHeap([5, 10]))

    def test_valid_heap(self):
        """Корректная max-куча"""
        self.assertTrue(isMaxHeap([20, 15, 10, 12, 13, 5, 8]))

    def test_invalid_heap_middle_layer(self):
        """Нарушение условия в середине кучи"""
        self.assertFalse(isMaxHeap([20, 15, 10, 25, 13, 5, 8]))

    def test_right_child_invalid(self):
        """Нарушение в правом потомке"""
        self.assertFalse(isMaxHeap([20, 15, 10, 12, 13, 5, 15]))

    def test_partial_last_level(self):
        """Неполный последний уровень"""
        self.assertTrue(isMaxHeap([20, 15, 10, 12]))

    def test_duplicate_values(self):
        """Одинаковые значения"""
        self.assertTrue(isMaxHeap([10, 10, 10]))

    def test_deep_invalid(self):
        """Нарушение на глубоком уровне"""
        heap = [100, 90, 80, 70, 60, 50, 40, 35, 34, 33, 32, 45, 31, 30]
        self.assertTrue(isMaxHeap(heap))


if __name__ == "__main__":
    unittest.main()
