from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        if grid[0][0] == 0:
            queue.append((0,0))
            visit.add((0, 0))
        else:
            return -1

        def bfs(grid):
            length = 1
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    
                    if r == ROWS - 1 and c == COLS - 1:
                        return length
                    
                    neighbours = [[1, 1], [-1, -1], [-1, 1], [1, -1],
                                  [0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbours:
                        if (min(r + dr, c + dc) < 0 or
                            r + dr >= ROWS or c + dc >= COLS or 
                            (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                            continue
                        queue.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                length += 1
            return -1

        
        return bfs(grid)