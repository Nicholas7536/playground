class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_island = 0
        
        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 0 
            area = 0
            
            while stack:
                cr, cc = stack.pop()
                area += 1
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0 
                        stack.append((nr, nc))
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_island = max(max_island, dfs(r, c))
        
        return max_island