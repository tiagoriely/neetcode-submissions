from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0,1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            island_area = 0
            queue = deque()
            grid[r][c] = 0
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (min(nr, nc) < 0 or 
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                    island_area += 1
            return island_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c) + 1)
                    
        
        return area
        