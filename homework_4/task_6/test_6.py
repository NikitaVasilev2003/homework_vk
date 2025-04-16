# t_6.py
import unittest
from t_6 import TreeNode, isSubtree


class TestIsSubtree(unittest.TestCase):

    def test_both_trees_empty(self):
        """Тест 1: Оба дерева пусты"""
        self.assertTrue(isSubtree(None, None))

    def test_subroot_empty(self):
        """Тест 2: Поддерево пустое"""
        root = TreeNode(5)
        self.assertTrue(isSubtree(root, None))

    def test_root_empty_subroot_not(self):
        """Тест 3: Основное дерево пустое, поддерево нет"""
        sub_root = TreeNode(5)
        self.assertFalse(isSubtree(None, sub_root))

    def test_identical_trees(self):
        """Тест 4: Деревья идентичны"""
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        sub_root = TreeNode(10, TreeNode(5), TreeNode(15))
        self.assertTrue(isSubtree(root, sub_root))

    def test_subtree_in_left(self):
        """Тест 5: Поддерево находится в левой ветви"""
        # Основное дерево:
        #       10
        #      /  \
        #     5    15
        #    / \
        #   3   7
        root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15))

        # Поддерево:
        #     5
        #    / \
        #   3   7
        sub_root = TreeNode(5, TreeNode(3), TreeNode(7))
        self.assertTrue(isSubtree(root, sub_root))

    def test_subtree_in_right(self):
        """Тест 6: Поддерево находится в правой ветви"""
        # Основное дерево:
        #       10
        #      /  \
        #     5    15
        #         /  \
        #        12  20
        root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20)))

        # Поддерево:
        #     15
        #    /  \
        #   12  20
        sub_root = TreeNode(15, TreeNode(12), TreeNode(20))
        self.assertTrue(isSubtree(root, sub_root))

    def test_subtree_deep_nesting(self):
        """Тест 7: Поддерево находится на глубоком уровне"""
        # Основное дерево:
        #        1
        #       / \
        #      2   3
        #     /   / \
        #    4   5   6
        #           /
        #          7
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3, TreeNode(5), TreeNode(6, TreeNode(7))),
        )

        # Поддерево:
        #      6
        #     /
        #    7
        sub_root = TreeNode(6, TreeNode(7))
        self.assertTrue(isSubtree(root, sub_root))

    def test_not_subtree_same_values(self):
        """Тест 8: Значения совпадают, но структура разная"""
        # Основное дерево:
        #      1
        #     /
        #    2
        #   /
        #  3
        root = TreeNode(1, TreeNode(2, TreeNode(3)))

        # Поддерево:
        #    2
        #     \
        #      3
        sub_root = TreeNode(2, None, TreeNode(3))
        self.assertFalse(isSubtree(root, sub_root))

    def test_subtree_is_leaf(self):
        """Тест 9: Поддерево - это лист"""
        root = TreeNode(10, TreeNode(5, TreeNode(1)), TreeNode(15))
        sub_root = TreeNode(1)
        self.assertTrue(isSubtree(root, sub_root))

    def test_large_subtree(self):
        """Тест 10: Поддерево больше основного дерева"""
        root = TreeNode(5)
        sub_root = TreeNode(5, TreeNode(3), TreeNode(7))
        self.assertFalse(isSubtree(root, sub_root))

    def test_partial_match(self):
        """Тест 11: Частичное совпадение структуры"""
        # Основное дерево:
        #      5
        #    /   \
        #   3     7
        #  / \   /
        # 2  4  6
        root = TreeNode(
            5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6))
        )

        # Поддерево:
        #      3
        #     /
        #    2
        sub_root = TreeNode(3, TreeNode(2))
        self.assertFalse(isSubtree(root, sub_root))

        # Поддерево:
        #      7
        #       \
        #        6
        sub_root = TreeNode(7, None, TreeNode(6))
        self.assertFalse(isSubtree(root, sub_root))


if __name__ == "__main__":
    unittest.main()
