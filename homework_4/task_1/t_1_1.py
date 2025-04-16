"""Восстановление бинарного дерева из массива"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(arr):
    def dfs(arr, i):
        if i > len(arr) - 1:
            return
        root = TreeNode(arr[i])
        root.left = dfs(arr, 2 * i + 1)
        root.right = dfs(arr, 2 * i + 2)
        return root

    return dfs(arr, 0)
