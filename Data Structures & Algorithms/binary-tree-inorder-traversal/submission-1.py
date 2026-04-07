# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        left = []
        current = []
        rigth = []
        ans = []

        if not root:
            return []

        left = self.inorderTraversal(root.left)
        print(root.val)
        current.append(root.val)
        right = self.inorderTraversal(root.right)

        ans = left + current + right
        return ans


        