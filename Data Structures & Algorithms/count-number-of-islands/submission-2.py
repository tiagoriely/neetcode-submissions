from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            # Mark the initial position as visited
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if (min(newRow, newCol) < 0 or
                        newRow >= ROWS or newCol >= COLS or
                        grid[newRow][newCol] == "0"):
                        continue
                    queue.append((newRow, newCol))
                    grid[newRow][newCol] = "0" # Mark as visited
            
        # Go through the whole and look for "1" (land)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands

        