from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0,1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
 
        def dfs(r, c):
            if (min(r, c) < 0 or 
                r >= ROWS or c >= COLS or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)
            return area
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
                    
        return area
        