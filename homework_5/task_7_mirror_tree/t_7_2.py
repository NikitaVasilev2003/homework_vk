"""Нужно реализовать алгоритм, который перевернет бинарное
дерево "вверх ногами", т.е. поменяет местами левые и правые
поддеревья каждого узла."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
