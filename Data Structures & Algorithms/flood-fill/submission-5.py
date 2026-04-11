class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Early exit if starting pixel is already the target color
        if image[sr][sc] == color:
            return image
        
        # Setting max boundaries
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c, originalColor):            
            if (min(r, c) < 0 or
                r > ROWS - 1 or c > COLS - 1 or
                image[r][c] != originalColor):
                return None
            
            # Change color
            image[r][c] = color

            # Change adjacent colors
            dfs(r + 1, c, originalColor)
            dfs(r - 1, c, originalColor)
            dfs(r, c + 1, originalColor)
            dfs(r , c - 1, originalColor)

        dfs(sr, sc, image[sr][sc])
        return image

        