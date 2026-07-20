# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result =[]
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

---------------------------------------------------------ALTERNATIVE---------------------------------------------------------
class Solution:
    def inorderTraversal(self, root):
        result = []
        if not root:
            return []
        result.extend(self.inorderTraversal(root.left))  # Step 1: Go LEFT
        result.append(root.val)                          # Step 2: Visit ROOT
        result.extend(self.inorderTraversal(root.right)) # Step 3: Go RIGHT
        return result
