# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            # Base case
            if not node:
                return 0
            
            # increment the count everytime the node value is the biggest
            # incl. edge case where node val == max value (roots must be counted)
            if node.val >= maxVal:
                res = 1
            # Do nothing is node val is smaller
            else:
                res = 0
            
            # Update the new maxVal if node value is bigger
            maxVal = max(maxVal, node.val)

            # Recursive cases
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, root.val)

        