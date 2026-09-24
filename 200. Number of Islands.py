=======================================CORE IDEA=========================================
1. We scan every cell one by one with two nested loops.
2. When we find a cell equal to `"1"`:
   - This is the **first cell we found of a brand new island** → `count += 1`
   - Run DFS starting at this cell.
3. What DFS does:
   - Base case: stop if out of bounds OR cell is not `"1"`
   - If it is `"1"`: set it to `"0"` (mark visited)
   - Then explore **only up, down, left, right (4 directions)**. Diagonals are ignored automatically, DFS never checks diagonal cells.
4. After DFS finishes, **all connected "1"s of this island have been changed to "0"**.
5. The outer for loop continues moving to next cells. Since those land cells are now `"0"`, they will NOT trigger another `count +=1`.
6. If later the loop finds another `"1"` somewhere else (separate island), repeat the whole process, increase count again.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid), len(grid[0])

        count = 0

        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != "1":
                return

            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count
