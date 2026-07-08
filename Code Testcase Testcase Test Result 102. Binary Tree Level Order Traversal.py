from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue1 = deque([root])

        while queue1:
            level = []
            level_size = len(queue1)

            for _ in range(level_size):
                node = queue1.popleft()
                level.append(node.val)

                if node.left:
                    queue1.append(node.left)

                if node.right:
                    queue1.append(node.right)

            result.append(level)
        return result
