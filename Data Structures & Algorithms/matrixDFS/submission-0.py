class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(matrix, r, c, visit):
            ROWS, COLS = len(matrix), len(matrix[0])

            if (min(r, c) < 0 or
                r > ROWS - 1 or c > COLS - 1 or
                (r, c) in visit or matrix[r][c] == 1):
                return 0
            # if row and columns are at the end of the maze
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))
            
            count = 0
            count += dfs(matrix, r + 1, c, visit)
            count += dfs(matrix, r - 1, c, visit)
            count += dfs(matrix, r, c + 1, visit) 
            count += dfs(matrix, r, c - 1, visit)

            visit.remove((r, c))

            return count
        
        return dfs(grid, 0, 0, visit)

        