from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''dfs (keep original gid, but lower space complexity)'''
        directions = [[1, 0], [-1, 0], [0,1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):

            if (min(r, c) < 0 or 
                r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == 0):
                return 0
            
            visit.add((r, c))
            
            
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
        