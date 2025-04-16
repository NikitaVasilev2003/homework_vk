import unittest
from t_4 import merge_k_sorted_arrays  # Замените your_module на имя вашего файла


class TestMergeKSortedArrays(unittest.TestCase):
    def test_empty_input(self):
        """Тест пустого списка массивов"""
        self.assertEqual(merge_k_sorted_arrays([]), [])

    def test_single_array(self):
        """Тест одного массива"""
        self.assertEqual(merge_k_sorted_arrays([[1, 2, 3]]), [1, 2, 3])
        self.assertEqual(merge_k_sorted_arrays([[]]), [])

    def test_arrays_with_varying_lengths(self):
        """Тест массивов разной длины"""
        self.assertEqual(
            merge_k_sorted_arrays([[1, 3, 5, 7], [2, 4], [8, 9, 10, 11, 12]]),
            [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12],
        )

    def test_duplicate_elements(self):
        """Тест с дублирующимися элементами"""
        self.assertEqual(
            merge_k_sorted_arrays([[2, 2, 3], [1, 4, 4, 5], [2, 5, 6]]),
            [1, 2, 2, 2, 3, 4, 4, 5, 5, 6],
        )

    def test_all_empty_arrays(self):
        """Тест всех пустых массивов"""
        self.assertEqual(merge_k_sorted_arrays([[], [], []]), [])

    def test_mixed_order(self):
        """Тест сохранения порядка при равных элементах"""
        self.assertEqual(
            merge_k_sorted_arrays([[5, 5, 5], [4, 5, 5], [3, 5, 6]]),
            [3, 4, 5, 5, 5, 5, 5, 5, 6],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
