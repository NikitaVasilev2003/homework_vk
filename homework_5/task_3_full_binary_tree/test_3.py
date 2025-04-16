import unittest
from t_3 import is_complete_tree, TreeNode


class TestIsCompleteTree(unittest.TestCase):
    def test_empty_tree(self):
        """Пустое дерево считается полным"""
        self.assertTrue(is_complete_tree(None))

    def test_single_Treenode(self):
        """Одиночная нода считается полным деревом"""
        self.assertTrue(is_complete_tree(TreeNode(1)))

    def test_complete_tree(self):
        """Идеально полное дерево"""
        #        1
        #      /   \
        #     2     3
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(is_complete_tree(root))

    def test_not_complete_missing_left(self):
        """Дерево не полное: правый потомок без левого"""
        #        1
        #         \
        #          3
        root = TreeNode(1, None, TreeNode(3))
        self.assertFalse(is_complete_tree(root))

    def test_not_complete_gap(self):
        """Дерево не полное: пропуск в последнем уровне"""
        #        1
        #      /   \
        #     2     3
        #    /       \
        #   4         5
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
        self.assertFalse(is_complete_tree(root))

    def test_complete_with_null_last_level(self):
        """Корректное полное дерево с null в конце"""
        #        1
        #      /   \
        #     2     3
        #    / \   /
        #   4  5 6
        root = TreeNode(
            1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))
        )
        self.assertTrue(is_complete_tree(root))

    def test_not_complete_after_null(self):
        """Узлы после первого null делают дерево неполным"""
        #        1
        #      /   \
        #     2     3
        #    /     /
        #   4     5
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
        self.assertFalse(is_complete_tree(root))

    def test_deep_complete_tree(self):
        """Глубокое полное дерево"""
        #          1
        #        /   \
        #       2     3
        #      / \   / \
        #     4  5 6   7
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertTrue(is_complete_tree(root))

    def test_deep_not_complete(self):
        """Глубокое неполное дерево"""
        #          1
        #        /   \
        #       2     3
        #      / \     \
        #     4  5     7
        root = TreeNode(
            1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7))
        )
        self.assertFalse(is_complete_tree(root))


if __name__ == "__main__":
    unittest.main()
