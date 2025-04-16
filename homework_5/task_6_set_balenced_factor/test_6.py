import unittest
from t_6 import set_balenced_factor, TreeNode


class TestSetBalanceFactor(unittest.TestCase):
    def test_empty_tree(self):
        """Проверка пустого дерева"""
        set_balenced_factor(None)

    def test_single_node(self):
        """Одиночный узел"""
        root = TreeNode(5)
        set_balenced_factor(root)
        self.assertEqual(root.balance_factor, 0)

    def test_perfect_balanced_tree(self):
        """Идеально сбалансированное дерево"""
        #      10
        #    /   \
        #   5    15
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        set_balenced_factor(root)

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 0)
        self.assertEqual(root.right.balance_factor, 0)

    def test_left_heavy_tree(self):
        """Перевес в левом поддереве"""
        #      10
        #     /
        #    5
        #   /
        #  2
        root = TreeNode(10, TreeNode(5, TreeNode(2)))
        set_balenced_factor(root)

        self.assertEqual(root.balance_factor, 2)
        self.assertEqual(root.left.balance_factor, 1)
        self.assertEqual(root.left.left.balance_factor, 0)

    def test_right_heavy_tree(self):
        """Перевес в правом поддереве"""
        #      10
        #        \
        #         20
        #           \
        #            30
        root = TreeNode(10, None, TreeNode(20, None, TreeNode(30)))
        set_balenced_factor(root)

        self.assertEqual(root.balance_factor, 2)
        self.assertEqual(root.right.balance_factor, 1)
        self.assertEqual(root.right.right.balance_factor, 0)

    def test_complex_tree(self):
        """Сложное дерево с разными балансами"""
        #          20
        #        /   \
        #       10    30
        #      /     /
        #     5     25
        #    /       \
        #   1         28
        root = TreeNode(
            20,
            TreeNode(10, TreeNode(5, TreeNode(1))),
            TreeNode(30, TreeNode(25, None, TreeNode(28))),
        )
        set_balenced_factor(root)

        self.assertEqual(root.balance_factor, 0)
        self.assertEqual(root.left.balance_factor, 2)
        self.assertEqual(root.right.balance_factor, 2)
        self.assertEqual(root.left.left.balance_factor, 1)
        self.assertEqual(root.right.left.balance_factor, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
