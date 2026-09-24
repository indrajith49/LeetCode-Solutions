=====================CORE IDEA=====================
Our job:
Paint **all 4-connected cells that have the SAME OLD COLOR as the starting pixel** into the new color.

Steps:

1. Save the old color of starting pixel into variable original_image = image[sr][sc]
2. Check: if original_image == color (old color already equals new color)
   - If yes → return image immediately, no work needed.
3. Else, call `dfs(sr, sc)` to start our search from the starting point.

Inside dfs(r,c):
4. Base case:
If

- `r` out of bounds OR
- `c` out of bounds OR
- `image[r][c] != original_image` (cell’s color is NOT the old starting color)
→ return, stop this path.

5. If we pass base case:
   - Paint current cell to new color
   - Call DFS for four neighbors: up `(r-1,c)`, down `(r+1,c)`, left `(r,c-1)`, right `(r,c+1)`
6. After DFS finishes completely → return modified image.


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
