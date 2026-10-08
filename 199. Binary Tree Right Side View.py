====================CORE IDEA=====================
We traverse the tree right-first. At each level, the first node we visit is the rightmost node at that level (because we go right before left).
We detect this "first visit" with len(res) == level — if true, we append it.

level is determined by the recursion depth (we pass level + 1 into child calls), not by appending.
The append and level just happen to stay in sync along the rightmost path.

If a right child doesn't exist at some level, the DFS naturally backtracks and visits the left child at the same level,
which then becomes the first visit for that level and gets appended — so it's still the rightmost visible node from the right side.



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
