"""Восстановление бинарного дерева из массива"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    stack = [(root, 0)]

    while stack:
        node, i = stack.pop()

        left_idx = 2 * i + 1
        if left_idx < len(arr):
            node.left = TreeNode(arr[left_idx])
            stack.append((node.left, left_idx))

        right_idx = 2 * i + 2
        if right_idx < len(arr):
            node.right = TreeNode(arr[right_idx])
            stack.append((node.right, right_idx))

    return root
