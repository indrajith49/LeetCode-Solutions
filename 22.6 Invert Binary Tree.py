#"The function calls itself on the left and right children, which then call themselves on their children, until the entire tree is inverted."
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

1. Base Case: If the current node is empty (None), return None. There is nothing to invert.

2. Swap Children: Swap the left and right children of the current node.

3. Recurse Left: Call invertTree on the new left child (the original right child). This will invert the entire left subtree.

4. Recurse Right: Call invertTree on the new right child (the original left child). This will invert the entire right subtree.

5. Return the Root: After both subtrees are inverted, return the root of the tree.
--------------------------------------------WITHOUT RECURSION--------------------------------------------
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        queue = [root]

        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
