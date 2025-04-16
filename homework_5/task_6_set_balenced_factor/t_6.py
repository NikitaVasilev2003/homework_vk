"""На вход функции передается указатель на корень бинарного дерева поиска.
Необходимо для каждого узла проставить balance factor
*Предполагается, что в структуре узла есть поле balance_factor"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None, balanceFactor=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = balanceFactor


def set_balenced_factor(root: TreeNode):
    def dfs(root: TreeNode):
        if not root:
            return 0
        left, right = dfs(root.left), dfs(root.right)
        root.balance_factor = abs(left - right)

        return 1 + max(left, right)

    dfs(root)
