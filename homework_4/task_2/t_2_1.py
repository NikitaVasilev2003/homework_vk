"""Симметричное бинарное дерево На вход функции подается бинарное дерево.
Необходимо понять, является ли это дерево симметричным."""


# рекурсия
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root) -> bool:
    def helper(r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return (
            r1.val == r2.val and helper(r1.left, r2.right) and helper(r2.left, r1.right)
        )

    return helper(root, root)
