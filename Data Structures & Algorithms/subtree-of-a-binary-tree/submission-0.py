# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Base case 1: empty subRoot is always a subtree of any tree
        if not subRoot:
            return True
        # Base case 2: main tree is empty but subRoot is not, impossible to have a subtree
        if not root:
            return False
        
        # Checking if current node matches subRoot entirely
        if self.isSameTree(root, subRoot):
            return True

        # Recursive Case: search left and right subtrees of main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, root, subRoot):
        # Base case: both empty/None, thus identical
        if not root and not subRoot:
            return True
        
        # Recursive case:
        # Both not empty/exist and value match, check children
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
         
        return False

        