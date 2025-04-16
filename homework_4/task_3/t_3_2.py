"""Поиск минимальной глубины бинарного дерева
На вход функции подается бинарное дерево. Необходимо найти минимальную глубину дерева.
"""


# (DFS)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left and not root.right:
        return 1 + minDepth(root.left)
    if root.right and not root.left:
        return 1 + minDepth(root.right)
    return 1 + min(minDepth(root.left), minDepth(root.right))
