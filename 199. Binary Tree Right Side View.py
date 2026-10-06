class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []
        def dfs(node, level):
            if not node:
                return
            # if length == level → means we haven't added anything for this level
            if len(res) == level:
                res.append(node.val)
            # Visit RIGHT FIRST, so right node gets added first for this level
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return res
