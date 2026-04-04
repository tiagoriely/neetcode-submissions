class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low_row, high_row = 0, len(matrix) - 1
        col_max = len(matrix[0]) - 1

        # Find the row using binary search on row only
        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            if matrix[mid_row][0] > target:
                high_row = mid_row - 1
            elif matrix[mid_row][col_max] < target:
                low_row = mid_row + 1
            else:
                break

        # Ensure the low_row is still smaller than high_row
        if not (low_row <= high_row):
            return False
            
        # Row found, so doing binary search on its columns
        left, right = 0, col_max
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[mid_row][mid_col] > target:
                right = mid_col - 1
            elif matrix[mid_row][mid_col] < target:
                left = mid_col + 1
            else:
                return True
        
        return False 