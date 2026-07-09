class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n or vis[i][j] or board[i][j] == 'X':
                return
            
            vis[i][j] = True

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            if board[i][0] == 'O' and not vis[i][0]:
                dfs(i, 0)
            if board[i][n - 1] == 'O' and not vis[i][n - 1]:
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O' and not vis[0][j]:
                dfs(0, j)
            if board[m - 1][j] == 'O' and not vis[m - 1][j]:
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'