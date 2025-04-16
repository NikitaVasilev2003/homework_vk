import unittest
from t_7 import TreeNode, CountMirrorTwins


class TestMirrorTwins(unittest.TestCase):

    def test_empty_tree(self):
        """Тест 1: Пустое дерево"""
        self.assertEqual(CountMirrorTwins(None), 0)

    def test_single_node(self):
        """Тест 2: Дерево из одного узла"""
        root = TreeNode(5)
        self.assertEqual(CountMirrorTwins(root), 0)

    def test_two_nodes_mirror(self):
        """Тест 3: Два зеркальных узла"""
        root = TreeNode(1, TreeNode(2), TreeNode(2))
        self.assertEqual(CountMirrorTwins(root), 1)

    def test_two_nodes_not_mirror(self):
        """Тест 4: Два узла с разными значениями"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(CountMirrorTwins(root), 0)

    def test_multilevel_mirror(self):
        """Тест 5: Многоуровневое зеркальное дерево"""
        #      1
        #    /   \
        #   2     2
        #  / \   / \
        # 3  4 4   3
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        )
        self.assertEqual(CountMirrorTwins(root), 3)

    def test_only_left_only_right(self):
        """Тест 6: Только левые и только правые дети"""
        #      1
        #    /   \
        #   2     2
        #  /       \
        # 3         3
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        self.assertEqual(CountMirrorTwins(root), 2)

    def test_mirror(self):
        """Тест 7: Зеркало"""
        #      1
        #    /   \
        #   2     2
        #    \   /
        #     3 3
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3)))
        self.assertEqual(CountMirrorTwins(root), 2)

    def test_deep_nesting(self):
        """Тест 8: Глубокая вложенность, но проверяем также, чтобы не учитывался последний уровень"""
        #          1
        #        /   \
        #       2     2
        #      / \   / \
        #     3  4 4   3
        #    /          /
        #   5          5
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3, TreeNode(5))),
        )
        self.assertEqual(CountMirrorTwins(root), 3)

    def test_only_left_subtree(self):
        """Тест 9: Только левое поддерево"""
        #      1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(CountMirrorTwins(root), 0)


if __name__ == "__main__":
    unittest.main()
