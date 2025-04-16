# test_3.py
import unittest
from t_3_2 import TreeNode, minDepth

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_3_1 import TreeNode, minDepth


class TestMinDepth(unittest.TestCase):

    def test_empty_tree(self):
        """Пример пустого дерева"""
        self.assertEqual(minDepth(None), 0)

    def test_single_node(self):
        """Пример дерева из одного узла"""
        root = TreeNode(5)
        self.assertEqual(minDepth(root), 1)

    def test_only_left_child(self):
        """Пример, где все узлы имеют только левых потомков"""
        # Структура:
        #     1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(minDepth(root), 3)

    def test_only_right_child(self):
        """Пример, где все узлы имеют только правых потомков"""
        # Структура:
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(minDepth(root), 3)

    def test_balanced_tree(self):
        """Пример сбалансированного дерева"""
        #     1
        #    / \
        #   2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(minDepth(root), 2)

    def test_unbalanced_min_on_right(self):
        """Пример несбалансированного дерева с минимальной глубиной справа"""
        #     1
        #    / \
        #   2   3
        #  /     \
        # 4       5
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4))
        root.right = TreeNode(3, None, TreeNode(5))
        self.assertEqual(minDepth(root), 3)

    def test_early_leaf_in_right(self):
        """Пример раннего листа в правом поддереве"""
        #     1
        #    / \
        #   2   3
        #  /   /
        # 4   5
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4))
        root.right = TreeNode(3, TreeNode(5))
        self.assertEqual(
            minDepth(root), 3
        )  # Минимальный путь: 1 -> 3 -> 5 (глубина 3?), нужен пересмотр

    def test_min_depth_in_middle(self):
        """Пример, где минимальная глубина достигается не на нижнем уровне"""
        #        1
        #       / \
        #      2   3
        #     /   / \
        #    4   5   6
        #   /
        #  7
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4, TreeNode(7)))
        root.right = TreeNode(3, TreeNode(5), TreeNode(6))
        self.assertEqual(minDepth(root), 3)

    def test_complex_tree(self):
        """Пример сложного дерева с разветвлениями"""
        #        1
        #       / \
        #      2   3
        #     / \   \
        #    4   5   6
        #   /       /
        #  7       8
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5))
        root.right = TreeNode(3, None, TreeNode(6, TreeNode(8)))
        self.assertEqual(minDepth(root), 3)

    def test_min_depth_with_single_child(self):
        """Пример, где у корня есть только один потомок, который также имеет один потомок"""
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(minDepth(root), 3)


if __name__ == "__main__":
    unittest.main()
