# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''DFS solution (recursive)'''
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Base case 1: both None, trees are identical up to this point
        if not p and not q:
            return True

        # Recursive case: both exist and values match, check children
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # Base case 2 - one is None or values differ, mismatch
            return False