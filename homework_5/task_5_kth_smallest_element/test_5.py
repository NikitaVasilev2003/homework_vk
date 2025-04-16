import unittest
from t_5 import kthSmallest, TreeNode


class TestKthSmallest(unittest.TestCase):
    def test_single_node(self):
        """Дерево из одного узла, k=1"""
        root = TreeNode(5)
        self.assertEqual(kthSmallest(root, 1), 5)

    def test_left_skewed_tree(self):
        """Вырожденное влево дерево"""
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(kthSmallest(root, 1), 1)
        self.assertEqual(kthSmallest(root, 2), 2)
        self.assertEqual(kthSmallest(root, 3), 3)

    def test_right_skewed_tree(self):
        """Вырожденное вправо дерево"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(kthSmallest(root, 1), 1)
        self.assertEqual(kthSmallest(root, 2), 2)
        self.assertEqual(kthSmallest(root, 3), 3)

    def test_balanced_tree(self):
        """Сбалансированное дерево"""
        #        5
        #      /   \
        #     3     8
        #    / \   /
        #   2  4 6
        root = TreeNode(
            5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, TreeNode(6))
        )
        self.assertEqual(kthSmallest(root, 1), 2)
        self.assertEqual(kthSmallest(root, 3), 4)
        self.assertEqual(kthSmallest(root, 5), 6)
        self.assertEqual(kthSmallest(root, 6), 8)

    def test_negative_values(self):
        """Дерево с отрицательными значениями"""
        #       -1
        #      /   \
        #    -3     2
        root = TreeNode(-1, TreeNode(-3), TreeNode(2))
        self.assertEqual(kthSmallest(root, 1), -3)
        self.assertEqual(kthSmallest(root, 2), -1)
        self.assertEqual(kthSmallest(root, 3), 2)

    def test_zero_value(self):
        """Узел со значением 0"""
        root = TreeNode(0)
        self.assertEqual(kthSmallest(root, 1), 0)

    def test_large_tree(self):
        """Большое дерево с несколькими уровнями"""
        #          10
        #        /    \
        #       5      15
        #      / \    / \
        #     3   7  12  18
        #    /   /
        #   2   6
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(7, TreeNode(6))),
            TreeNode(15, TreeNode(12), TreeNode(18)),
        )
        self.assertEqual(kthSmallest(root, 1), 2)
        self.assertEqual(kthSmallest(root, 4), 6)
        self.assertEqual(kthSmallest(root, 7), 12)
        self.assertEqual(kthSmallest(root, 8), 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
