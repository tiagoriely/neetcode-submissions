# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []    
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            # Initialise to None RightMost
            rightmost = None
            for i in range(len(queue)):
                curr = queue.popleft()
                # Update rightmost: with the current value
                rightmost = curr
                if curr.left:
                    queue.append(curr.left)
                # Must be the last one popped if exists
                if curr.right:
                    queue.append(curr.right)
                
            
            if rightmost:
                ans.append(rightmost.val)

        return ans



        