# test_1.py
import unittest
from t_1_2 import buildTree

# я не писал два файла для тестов, но назвал фунции одинаково, поэтому для текстирования
# другого случая достаточно написать
# from t_1_1 import buildTree


class TestBuildTree(unittest.TestCase):

    def test_empty_array(self):
        """Тест 1 пустой массив"""
        arr = []
        root = buildTree(arr)
        self.assertIsNone(root)

    def test_single_element(self):
        """Тест 2 один элемент"""
        arr = [5]
        root = buildTree(arr)
        self.assertEqual(root.val, 5)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_full_tree(self):
        """Тест 3 полное бинарное дерево."""
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr)
        # Проверка обхода в ширину (BFS)
        expected = arr
        result = self.tree_to_bfs_array(root)
        self.assertEqual(result, expected)

    def test_incomplete_tree(self):
        """Тест 4 неполное бинарное дерево."""
        arr = [1, 2, 3, 4]
        root = buildTree(arr)
        expected = arr
        result = self.tree_to_bfs_array(root)
        self.assertEqual(result, expected)

    # можно делать и так, но это долго, поэтому проще через готовую функцию делать как в прошлом Тест е
    def test_custom_array(self):
        """Тест 5 с семинара"""
        arr = [21, 19, 18, 11, 12, 15, 16, 9, 8, 10]
        root = buildTree(arr)

        # Проверка корня
        self.assertEqual(root.val, 21)

        # Проверка левого потомка корня (индекс 1)
        self.assertEqual(root.left.val, 19)

        # Проверка правого потомка корня (индекс 2)
        self.assertEqual(root.right.val, 18)

        # Проверка узла с индексом 3 (значение 11)
        node_11 = root.left.left
        self.assertEqual(node_11.val, 11)

        # Проверка правого потомка узла 11 (индекс 8)
        self.assertEqual(node_11.right.val, 8)

        # Проверка узла с индексом 4 (значение 12)
        node_12 = root.left.right
        self.assertEqual(node_12.val, 12)

        # Проверка левого потомка узла 12 (индекс 9)
        self.assertEqual(node_12.left.val, 10)

        # Проверка отсутствия правого потомка у узла 12 (индекс 10)
        self.assertIsNone(node_12.right)

    def tree_to_bfs_array(self, root):
        """Преобразует дерево в массив через обход в ширину (BFS)."""
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


if __name__ == "__main__":
    unittest.main()
