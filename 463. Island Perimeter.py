class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    perimeter += 4

                    for i_off, j_off in [(0,1), (1,0), (0-1), (-1,0)]:

                        r,c = i+i_off, j+j_off
                        if 0<=r < rows and 0<=c<cols and grid[r][c]:
                            perimeter -=1

        return perimeter


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0
            visited.add((r, c))

            perim = dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

            return perim

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0