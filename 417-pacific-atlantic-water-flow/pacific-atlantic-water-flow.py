from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(heights)
        cols = len(heights[0])
        
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def bfs(start_nodes, reachable_set):
            queue = deque(start_nodes)
            for r, c in start_nodes:
                reachable_set.add((r, c))
                
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr, dc in dirs:
                    next_r, next_c = curr_r + dr, curr_c + dc
                    
                    if 0 <= next_r < rows and 0 <= next_c < cols:
                        if (next_r, next_c) not in reachable_set:
                            if heights[next_r][next_c] >= heights[curr_r][curr_c]:
                                reachable_set.add((next_r, next_c))
                                queue.append((next_r, next_c))

        pacific_starts = []
        atlantic_starts = []
        
        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows - 1, c))
            
        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, cols - 1))
            
        bfs(pacific_starts, pacific_reachable)
        bfs(atlantic_starts, atlantic_reachable)
        
        return [list(cell) for cell in (pacific_reachable & atlantic_reachable)]
