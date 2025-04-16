# test_2.py
import unittest
from t_2_3 import TreeNode, isSymmetric

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_2_1 (или t_2_2) import TreeNode, isSymmetric


class TestSymmetricTree(unittest.TestCase):

    def test_empty_tree(self):
        """Тест 1 пустое дерева"""
        self.assertTrue(isSymmetric(None))

    def test_single_node(self):
        """Тест 2 дерева из одного узла"""
        root = TreeNode(5)
        self.assertTrue(isSymmetric(root))

    def test_symmetric_simple(self):
        """Тест 3 простое симметричное дерево"""
        #     1
        #    / \
        #   2   2
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertTrue(isSymmetric(root))

    def test_asymmetric_simple(self):
        """Тест 4 простое несимметричное дерево"""
        #     1
        #    / \
        #   2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(isSymmetric(root))

    def test_deep_symmetric(self):
        """Тест 5 многоуровневое симметричное дерево"""
        #        1
        #      /   \
        #     2     2
        #    / \   / \
        #   3  4  4  3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertTrue(isSymmetric(root))

    def test_deep_asymmetric_values(self):
        """Тест 6 несимметричные значения на разных уровнях"""
        #        1
        #      /   \
        #     2     2
        #    / \   / \
        #   5  4  4  3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(5), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertFalse(isSymmetric(root))

    def test_structure_asymmetry(self):
        """Тест 7 несимметричная структура ветвей"""
        #     1
        #    / \
        #   2   2
        #  /     \
        # 3       3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3))
        root.right = TreeNode(2, None, TreeNode(3))
        self.assertTrue(isSymmetric(root))

        #     1
        #    / \
        #   2   2
        #  /     \
        # 3       4
        root.right = TreeNode(2, None, TreeNode(4))
        self.assertFalse(isSymmetric(root))

    def test_unbalanced_trees(self):
        """Тест 8 разных вариантов несбалансированных деревьев"""
        # Случай 1
        #     1
        #    /
        #   2
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertFalse(isSymmetric(root))

        # Случай 2
        #     1
        #      \
        #       2
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertFalse(isSymmetric(root))

    def test_complex_symmetry(self):
        """Тест 9 сложной симметрии с чередующимися значениями"""
        #        1
        #      /   \
        #     2     2
        #    /     /
        #   3     3
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3))
        root.right = TreeNode(2, TreeNode(3))
        self.assertFalse(isSymmetric(root))


if __name__ == "__main__":
    unittest.main()
