class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 0

            grid[r][c]=0

            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)


        for r in range(rows):
            for c in range(cols):

                if grid[r][c]==1:
                    current_island_size = dfs(r,c)
                    if current_island_size>max_area:
                        max_area = current_island_size

        return max_area