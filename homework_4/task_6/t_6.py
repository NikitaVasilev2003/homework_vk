"""На вход функции подается два бинарных дерева. Необходимо
вернуть true, если дерево B является поддеревом для A"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def sameTree(p: TreeNode, q: TreeNode):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)
