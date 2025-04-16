import unittest
from t_2 import isMaxHeap, TreeNode


class TestIsMaxHeap(unittest.TestCase):
    def test_empty_tree(self):
        """root is None"""
        self.assertTrue(isMaxHeap(None))

    def test_single_TreeNode(self):
        """один элемент"""
        root = TreeNode(10)
        self.assertTrue(isMaxHeap(root))

    def test_valid_max_heap(self):
        """Правильная куча"""
        #        10
        #       /  \
        #      9    8
        root = TreeNode(10)
        root.left = TreeNode(9)
        root.right = TreeNode(8)
        self.assertTrue(isMaxHeap(root))

    def test_invalid_child_value(self):
        """Левый потомок больше родителя"""
        #        10
        #       /  \
        #      11   8
        root = TreeNode(10)
        root.left = TreeNode(11)
        root.right = TreeNode(8)
        self.assertFalse(isMaxHeap(root))

    def test_missing_left_child(self):
        """Нет левого потомка при наличии правого"""
        #        10
        #         \
        #          8
        root = TreeNode(10)
        root.right = TreeNode(8)
        self.assertFalse(isMaxHeap(root))

    def test_not_complete_tree(self):
        """Нарушение полноты"""
        #        10
        #       /  \
        #      8    9
        #     /      \
        #    7        6
        root = TreeNode(10)
        root.left = TreeNode(8)
        root.right = TreeNode(9)
        root.left.left = TreeNode(7)
        root.right.right = TreeNode(6)
        self.assertFalse(isMaxHeap(root))

    def test_leaf_after_missing_child(self):
        """Лист должен быть после первого отсутствующего узла"""
        #        10
        #       /
        #      9
        #       \
        #        8
        root = TreeNode(10)
        root.left = TreeNode(9)
        root.left.right = TreeNode(8)
        self.assertFalse(isMaxHeap(root))

    def test_deep_valid_heap(self):
        """Правильная куча, но с большей глубиной"""
        #          50
        #        /    \
        #      40      30
        #     /  \    /
        #    20  25  15
        root = TreeNode(50)
        root.left = TreeNode(40)
        root.right = TreeNode(30)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(25)
        root.right.left = TreeNode(15)
        self.assertTrue(isMaxHeap(root))

    def test_deep_invalid_heap(self):
        """Неправильная куча, но с большей глубиной"""
        #          50
        #        /    \
        #      40      30
        #     /  \    /  \
        #    45  25  15  20
        root = TreeNode(50)
        root.left = TreeNode(40)
        root.right = TreeNode(30)
        root.left.left = TreeNode(45)
        root.left.right = TreeNode(25)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(20)
        self.assertFalse(isMaxHeap(root))


if __name__ == "__main__":
    unittest.main()
