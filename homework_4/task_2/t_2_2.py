"""Симметричное бинарное дерево На вход функции подается бинарное дерево.
Необходимо понять, является ли это дерево симметричным."""


# стек
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root) -> bool:
    if not root:
        return True
    stack = [root.left, root.right]
    while stack:
        n1 = stack.pop()
        n2 = stack.pop()
        if not n1 and not n2:
            continue
        if not n1 or not n2 or n1.val != n2.val:
            return False
        stack.append(n1.left)
        stack.append(n2.right)
        stack.append(n1.right)
        stack.append(n2.left)
    return True
