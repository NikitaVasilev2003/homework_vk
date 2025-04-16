"""Симметричное бинарное дерево На вход функции подается бинарное дерево.
Необходимо понять, является ли это дерево симметричным."""

from collections import deque


# очередь (BFS)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root) -> bool:
    if not root:
        return True

    q = deque([root.left, root.right])

    while q:
        if len(q) % 2 != 0:
            return False

        left = q.popleft()
        right = q.pop()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False

        q.appendleft(left.left)
        q.append(right.right)
        q.appendleft(left.right)
        q.append(right.left)

    return True
