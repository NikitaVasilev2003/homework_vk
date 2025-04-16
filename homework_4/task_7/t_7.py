"""Дано бинарное дерево. Необходимо подсчитать количество зеркальных узлов в нем"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def CountMirrorTwins(root: TreeNode) -> int:
    if not root:
        return 0

    count = 0

    def dfs(r1: TreeNode, r2: TreeNode):
        nonlocal count
        if not r1 or not r2:
            return

        if r1.val == r2.val:
            count += 1

        dfs(r1.left, r2.right)
        dfs(r1.right, r2.left)

    dfs(root.left, root.right)

    return count
