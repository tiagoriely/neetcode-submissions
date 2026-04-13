class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        
        def dfs(row, col):
            if (min(row, col) < 0 or
                row >= ROWS or col >= COLS or
                grid[row][col] == "0"):
                return

            # Mark as visited by replacing 1 by zero
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        # Looping through the grid to find a "1"
        for r in range(ROWS):
            for c in range(COLS):
                # When zero is found check adjacent vertices until no more "1"
                # is found. This gives you an island
                if grid[r][c] == "1":
                    dfs(r,c)
                    island += 1
        
        return island
    



        
