import unittest
from t_7_1 import invertTree, TreeNode


class TestInvertTree(unittest.TestCase):
    def test_empty_tree(self):
        """Проверка пустого дерева"""
        self.assertIsNone(invertTree(None))

    def test_single_node(self):
        """Дерево из одного узла"""
        root = TreeNode(5)
        inverted = invertTree(root)
        self.assertEqual(inverted.val, 5)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

    def test_two_levels(self):
        """
        Исходное дерево:
            1
           / \
          2   3

        Ожидаемое после инвертирования:
            1
           / \
          3   2
        """
        original = TreeNode(1, TreeNode(2), TreeNode(3))
        inverted = invertTree(original)

        self.assertEqual(inverted.val, 1)
        self.assertEqual(inverted.left.val, 3)
        self.assertEqual(inverted.right.val, 2)

    def test_three_levels(self):
        """
        Исходное дерево:
              4
             / \
            2   7
           / \ / \
          1 3 6 9

        Ожидаемое после инвертирования:
              4
             / \
            7   2
           / \ / \
          9 6  3  1
        """
        original = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
        inverted = invertTree(original)

        # Проверка первого уровня
        self.assertEqual(inverted.val, 4)

        # Проверка второго уровня
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)

        # Проверка третьего уровня
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertEqual(inverted.right.right.val, 1)

    def test_left_skewed_tree(self):
        """
        Исходное дерево:
            1
           /
          2
         /
        3

        Ожидаемое после инвертирования:
            1
             \
              2
               \
                3
        """
        original = TreeNode(1, TreeNode(2, TreeNode(3)))
        inverted = invertTree(original)

        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertEqual(inverted.right.val, 2)
        self.assertIsNone(inverted.right.left)
        self.assertEqual(inverted.right.right.val, 3)

    def test_right_skewed_tree(self):
        """
        Исходное дерево:
            1
             \
              2
               \
                3

        Ожидаемое после инвертирования:
            1
           /
          2
         /
        3
        """
        original = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        inverted = invertTree(original)

        self.assertEqual(inverted.val, 1)
        self.assertEqual(inverted.left.val, 2)
        self.assertIsNone(inverted.right)
        self.assertEqual(inverted.left.left.val, 3)

    def test_mixed_tree(self):
        """
        Исходное дерево:
              10
            /    \
           5     15
            \   / \
             7 12 20
                     \
                      25

        Ожидаемое после инвертирования:
              10
            /    \
           15     5
          / \     /
        20  12    7
        /
        25
        """
        original = TreeNode(
            10,
            TreeNode(5, None, TreeNode(7)),
            TreeNode(15, TreeNode(12), TreeNode(20, None, TreeNode(25))),
        )
        inverted = invertTree(original)

        # Проверка корня
        self.assertEqual(inverted.val, 10)

        # Левый подкорень (бывший правый)
        self.assertEqual(inverted.left.val, 15)
        self.assertEqual(inverted.left.left.val, 20)
        self.assertEqual(inverted.left.right.val, 12)

        # # Правый подкорень (бывший левый)
        self.assertEqual(inverted.right.val, 5)
        self.assertEqual(inverted.right.left.val, 7)

        # # Проверка глубокого узла
        self.assertEqual(inverted.left.left.left.val, 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
