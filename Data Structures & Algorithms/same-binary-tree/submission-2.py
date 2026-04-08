# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        queueP = deque()
        queueQ = deque ()

        queueP.append(p)
        queueQ.append(q)
        while len(queueP) > 0:
            for i in range(len(queueP)):
                currP = queueP.popleft()
                currQ = queueQ.popleft()

                if currP is None and currQ is None:
                    continue
                if currP is None or currQ is None or currP.val != currQ.val:
                    return False
                queueP.append(currP.left)
                queueQ.append(currQ.left)
                queueP.append(currP.right)
                queueQ.append(currQ.right)
        return True