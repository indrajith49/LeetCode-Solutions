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



1. Edge Case: If the tree is empty, return an empty list. Nothing to traverse.

2. Initialize: Create a result list to store all levels. Create a queue and add the root node to it.

3. Loop Until Empty: While there are nodes in the queue, process one entire level at a time.

4. Count the Level: Check the current size of the queue. This tells us exactly how many nodes are in the current level.

5. Prepare a Bucket: Create an empty list called level (or inner) to hold all the values for this level.

6. Process Nodes in the Level: Loop exactly level_size times. For each node:

7. Remove the node from the front of the queue.

8. Add its value to the level list.

9. If the node has a left child, add it to the back of the queue for the next level.

10. If the node has a right child, add it to the back of the queue for the next level.

11. Store the Level: After processing all nodes in the level, add the level list to the result list.

12. Continue: Repeat steps 3–7 until the queue is empty.

13. Return: Return the result list containing all levels.
