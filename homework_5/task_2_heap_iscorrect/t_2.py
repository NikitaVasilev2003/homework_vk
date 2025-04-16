"""Проверка корректности кучи
Через обход в ширину"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMaxHeap(root: TreeNode):
    if not root:
        return True
    q = deque([root])
    shouldBeLeaf = False

    while q:
        current = q.popleft()
        if current.left:
            if shouldBeLeaf or current.left.val > current.val:
                return False
            q.append(current.left)
        else:
            shouldBeLeaf = True

        if current.right:
            if shouldBeLeaf or current.right.val > current.val:
                return False
            q.append(current.right)
        else:
            shouldBeLeaf = True
    return True
