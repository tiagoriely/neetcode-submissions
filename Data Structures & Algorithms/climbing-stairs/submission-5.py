class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        
        def dfs(i):
            if i >= n:
                # True(1) if landed at the stop | False(0) if overstepped the top
                return i == n 
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)
