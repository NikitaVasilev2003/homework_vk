"""Полное бинарное дерево"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_complete_tree(root: TreeNode) -> bool:
    if not root:
        return True

    q = deque([root])
    seen_null = False

    while q:
        cur = q.popleft()

        if not cur:
            seen_null = True
            continue

        if seen_null:
            return False
        q.append(cur.left)
        q.append(cur.right)
    return True
