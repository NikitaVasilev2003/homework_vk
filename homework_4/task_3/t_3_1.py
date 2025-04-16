"""Поиск минимальной глубины бинарного дерева
На вход функции подается бинарное дерево. Необходимо найти минимальную глубину дерева.
"""

from collections import deque


# (BFS)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root) -> int:
    if not root:
        return 0
    q = deque([(root, 1)])
    while q:
        cur, depth = q.popleft()
        if not cur.left and not cur.right:
            return depth
        if cur.left:
            q.append((cur.left, depth + 1))
        if cur.right:
            q.append((cur.right, depth + 1))
