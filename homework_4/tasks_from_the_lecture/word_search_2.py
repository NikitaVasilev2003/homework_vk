# https://leetcode.com/problems/word-search-ii/description/


class TreeNode:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TreeNode()
            cur = cur.children[w]
        cur.isword = True


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    root = TreeNode()
    for w in words:
        root.addword(w)
    rows, cols = len(board), len(board[0])
    res, visit = set(), set()

    def dfs(r, c, node: TreeNode, word):
        if (
            not (0 <= r < rows)
            or not (0 <= c < cols)
            or board[r][c] not in node.children
            or (r, c) in visit
        ):
            return
        visit.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.isword:
            res.add(word)
        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r, c + 1, node, word)
        dfs(r, c - 1, node, word)
        visit.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "")
    return list(res)
