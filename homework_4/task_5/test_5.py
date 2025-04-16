# t_5.py
import unittest
from t_5 import TreeNode, isSameTree


class TestSameTree(unittest.TestCase):

    def test_both_trees_empty(self):
        """Пример 1: Оба дерева пусты"""
        self.assertTrue(isSameTree(None, None))

    def test_one_tree_empty(self):
        """Пример 2: Одно дерево пустое, другое нет"""
        tree1 = TreeNode(1)
        self.assertFalse(isSameTree(tree1, None))
        self.assertFalse(isSameTree(None, tree1))

    def test_single_node_equal(self):
        """Пример 3: Деревья из одного узла с одинаковыми значениями"""
        tree1 = TreeNode(5)
        tree2 = TreeNode(5)
        self.assertTrue(isSameTree(tree1, tree2))

    def test_single_node_not_equal(self):
        """Пример 4: Деревья из одного узла с разными значениями"""
        tree1 = TreeNode(5)
        tree2 = TreeNode(10)
        self.assertFalse(isSameTree(tree1, tree2))

    def test_identical_trees(self):
        """Пример 5: Полностью идентичные деревья"""
        #       1            1
        #      / \          / \
        #     2   3        2   3
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(isSameTree(tree1, tree2))

    def test_different_values(self):
        """Пример 6: Разные значения в узлах"""
        #       1            1
        #      / \          / \
        #     2   3        2   4
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(2), TreeNode(4))
        self.assertFalse(isSameTree(tree1, tree2))

    def test_different_structure(self):
        """Пример 7: Разная структура ветвей"""
        #       1            1
        #      /              \
        #     2                2
        tree1 = TreeNode(1, TreeNode(2))
        tree2 = TreeNode(1, None, TreeNode(2))
        self.assertFalse(isSameTree(tree1, tree2))

    def test_deep_trees_equal(self):
        """Пример 8: Большие идентичные деревья"""
        #          1                 1
        #        /   \            /   \
        #       2     3          2     3
        #      / \   / \        / \   / \
        #     4  5  6  7       4  5  6  7
        tree1 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        tree2 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertTrue(isSameTree(tree1, tree2))

    def test_deep_trees_different(self):
        """Пример 9: Большие деревья с отличием в последнем узле"""
        #          1                 1
        #        /   \            /   \
        #       2     3          2     3
        #      / \   / \        / \   /
        #     4  5  6  7       4  5  6
        tree1 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        tree2 = TreeNode(
            1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))
        )
        self.assertFalse(isSameTree(tree1, tree2))

    def test_mirror_trees(self):
        """Пример 10: Зеркальные деревья (структура симметрична, но не идентичная)"""
        #       1            1
        #      / \          / \
        #     2   3        3   2
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(3), TreeNode(2))
        self.assertFalse(isSameTree(tree1, tree2))


if __name__ == "__main__":
    unittest.main()
