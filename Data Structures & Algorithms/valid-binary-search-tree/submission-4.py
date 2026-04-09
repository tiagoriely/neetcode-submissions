# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):
            # Base case 1: if does not exit/empty valid
            if not node:
                return True
            
            # Early exit: check is value is between lower(left) and upper(right) bound
            if not (left < node.val < right):
                return False
            
            # Recursive Case
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        # Start from -inf to inf for root
        return dfs(root, float("-inf"), float("inf"))
        