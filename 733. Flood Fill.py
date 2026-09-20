from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        # if already same color, directly return
        if original_color == color:
            return image

        
        def dfs(r, c):
            # ========== RECURSION BASE CASE (STOP RULE) ==========
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original:
                return  # stop! no more work for this cell

            # ========== NORMAL WORK: if we did NOT stop, paint cell ==========
            image[r][c] = color

            # ========== RECURSIVE STEP: visit four neighbour cells ==========
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        dfs(sr, sc)
        return image
