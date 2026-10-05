# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def bst(node, low, high):
            if not node:
                return True

            if low >= node.val or high <= node.val:
                return False

            lefty = bst(node.left, low, node.val)
            righty = bst(node.right, node.val, high)

            return lefty and righty

        isvalid = bst(root, -float("inf"), float("inf"))
        return isvalid
