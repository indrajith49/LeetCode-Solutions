class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        met = set()

        def dfs(r,c,k):

            if k ==len(word):
                return True

            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != word[k] or (r,c) in met:
                return False

            met.add((r,c))

            result = (dfs(r+1,c,k+1) or dfs(r-1,c,k+1) or dfs(r,c+1,k+1) or dfs(r,c-1,k+1))

            met.remove((r,c))
            return result


        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False