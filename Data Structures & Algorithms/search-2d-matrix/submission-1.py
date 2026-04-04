class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low_row, high_row = 0, len(matrix) - 1
        col_max = len(matrix[0]) - 1

        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            if matrix[mid_row][0] > target:
                high_row = mid_row - 1
            elif matrix[mid_row][col_max] < target:
                low_row = mid_row + 1
            else:
                break

        if low_row > high_row:
            return False
        
        row = (low_row + high_row) // 2
            
        left, right = 0, col_max
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[row][mid_col] > target:
                right = mid_col - 1
            elif matrix[row][mid_col] < target:
                left = mid_col + 1
            else:
                return True
        
        return False 