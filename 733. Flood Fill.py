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
            # Stop if out of bounds OR pixel is not original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            # paint this pixel
            image[r][c] = color

            # visit 4 directions: down, up, right, left
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
