import unittest
from t_4 import max_min_multiplication


class TestMaxMinMultiplication(unittest.TestCase):

    def test_empty_array(self):
        """Тест 1: Пустой массив"""
        self.assertEqual(max_min_multiplication([]), -1)

    def test_single_element(self):
        """Тест 2: 1 элемент"""
        self.assertEqual(max_min_multiplication([5]), -1)

    def test_two_elements(self):
        """Тест 3: 2 элемент"""
        self.assertEqual(max_min_multiplication([10, 5]), 50)

    def test_valid_bst(self):
        """Тест 4: сбалансированное дерево"""
        data = [5, 3, 8, 2, 4, 7, 9]
        self.assertEqual(max_min_multiplication(data), 2 * 9)

    def test_none_in_left_subtree(self):
        """Тест 5: нет левого поддерева"""
        data = [10, None, 15, None, None, 12, 20]
        self.assertEqual(max_min_multiplication(data), 10 * 20)

    def test_none_in_right_subtree(self):
        """Тест 6: нет правого поддерева"""
        data = [10, 5, None, 2, 7]
        self.assertEqual(max_min_multiplication(data), 2 * 10)

    def test_all_left_children(self):
        """Тест 7: все дети слева"""
        data = [1, 2, None, 3, None, None, None, 4]
        self.assertEqual(max_min_multiplication(data), 1 * 4)

    def test_all_right_children(self):
        """Тест 8: все дети слева"""
        data = [
            1,
            None,
            3,
            None,
            None,
            None,
            6,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            9,
        ]
        self.assertEqual(max_min_multiplication(data), 1 * 9)

    def test_min_max_in_middle(self):
        """Тест 9: минимальный элемент в левом поддереве, максимальный — в правом"""
        #        10
        #       /  \
        #      5    20
        #     /      \
        #    2        25
        data = [10, 5, 20, 2, None, None, 25]
        self.assertEqual(max_min_multiplication(data), 2 * 25)


if __name__ == "__main__":
    unittest.main()
